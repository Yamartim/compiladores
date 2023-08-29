# Generated from Alguma.g4 by ANTLR 4.13.0
from antlr4 import *
from AlgumaParser import AlgumaParser
from listaErros import listaErros
from TabelaDeSimbolos import TabelaDeSimbolos

# This class defines a complete generic visitor for a parse tree produced by AlgumaParser.

class GeradorCodigo(ParseTreeVisitor):

    #construtor para a classe

    def __init__(self, parser):
        self.tabela = TabelaDeSimbolos()
        self.funcoes = TabelaDeSimbolos()
        self.saida = ""
        self.parser = parser

    # Visit a parse tree produced by AlgumaParser#programa.
    def visitPrograma(self, ctx:AlgumaParser.ProgramaContext):
        self.saida += "#include <stdio.h>\n"
        self.saida += "#include <stdlib.h>\n"
        self.saida += "\n"
        # self.visitDeclaracoes aqui para procedimentos, implementar depois
        self.saida += "\n"
        self.saida += "int main() {\n"
        self.visitCorpo(ctx.corpo())
        self.saida += "}\n"
        return 


    # Visit a parse tree produced by AlgumaParser#declaracoes.
    def visitDeclaracoes(self, ctx:AlgumaParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#decl_local_global.
    def visitDecl_local_global(self, ctx:AlgumaParser.Decl_local_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#declaracao_local.
    def visitDeclaracao_local(self, ctx:AlgumaParser.Declaracao_localContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#variavel.
    def visitVariavel(self, ctx:AlgumaParser.VariavelContext):
        tipo = ctx.tipo().getText()
        dimensao = ""
        if tipo == "inteiro":
            tipo = "int"
        elif tipo == "real":
            tipo = "float"
        elif tipo == "literal":
            tipo = "char"
            dimensao = "[80]"

        self.saida += tipo + " "
        i = 0
        while ctx.identificador(i) != None:
            self.saida += ctx.identificador(i).getText() + dimensao + ','
            self.tabela.inserir(ctx.identificador(i).getText(), [tipo + dimensao, False])
            i += 1
        self.saida = self.saida[:-1] + ";\n"
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#identificador.
    def visitIdentificador(self, ctx:AlgumaParser.IdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#dimensao.
    def visitDimensao(self, ctx:AlgumaParser.DimensaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#tipo.
    def visitTipo(self, ctx:AlgumaParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#tipo_basico.
    def visitTipo_basico(self, ctx:AlgumaParser.Tipo_basicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#tipo_basico_ident.
    def visitTipo_basico_ident(self, ctx:AlgumaParser.Tipo_basico_identContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#tipo_estendido.
    def visitTipo_estendido(self, ctx:AlgumaParser.Tipo_estendidoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#valor_constante.
    def visitValor_constante(self, ctx:AlgumaParser.Valor_constanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#registro.
    def visitRegistro(self, ctx:AlgumaParser.RegistroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#declaracao_global.
    def visitDeclaracao_global(self, ctx:AlgumaParser.Declaracao_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#parametro.
    def visitParametro(self, ctx:AlgumaParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#parametros.
    def visitParametros(self, ctx:AlgumaParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#corpo.
    def visitCorpo(self, ctx:AlgumaParser.CorpoContext):
        return self.visitChildren(ctx)


    def verificarTipo(self, ctx):
        i = 0
        flag = True
        conversao = False
        ctx_type = type(ctx)
        children = None
        if ctx == None:
            return None
        

        if ctx_type is self.parser.ParcelaContext:
            if ctx.parcela_nao_unario() != None:
                if ctx.parcela_nao_unario().CADEIA() != None:
                    return "string"
                else:
                    ident = ctx.parcela_nao_unario().identificador().IDENT(0).symbol
                    return '&' + self.tabela.verificar(ident.text)[0]
                
            elif ctx.parcela_unario().identificador() != None:
                ident = ctx.parcela_unario().identificador().IDENT(0).symbol
                tipo = self.tabela.verificar(ident.text)[0]
                print(tipo)
                if (type(tipo) is TabelaDeSimbolos or self.tabela.existe(tipo)) and ctx.parcela_unario().identificador().IDENT(1) != None:
                    #entao temos uma segunda parte no ident
                    ident2 = ctx.parcela_unario().identificador().IDENT(1).symbol
                    if self.tabela.existe(tipo):
                        tipo = self.tabela.verificar(tipo)[0] # recupera a tabela de simbolos do registro

                    if type(tipo) is TabelaDeSimbolos: #acessa a tabela de simbolos do registro e recupera a parte solicitada
                        tipo = tipo.verificar(ident2.text)[0]
                        
                return tipo
    
            elif ctx.parcela_unario().NUM_INT() != None:
                return "int"
            
            elif ctx.parcela_unario().NUM_REAL() != None:
                return "float"
            
            elif ctx.parcela_unario().IDENT() != None:
                #entao é uma chamada, verificar tipo na tabela de funções
                ident = ctx.parcela_unario().IDENT().symbol
                return self.funcoes.verificar(ident.text)[1]
            else:
                #ultimo caso possível, é o de uma expressao entre parenteses, resolver essa expressao
                return self.verificarTipo(ctx.parcela_unario().expressao(0))
            
        if ctx_type is self.parser.ExpressaoContext:
            children = ctx.termo_logico
            if ctx.op_logico_1(0) != None:
                conversao = True
        elif ctx_type is self.parser.Termo_logicoContext:
            children = ctx.fator_logico
            if ctx.op_logico_2(0) != None:
                conversao = True
        elif ctx_type is self.parser.Fator_logicoContext:
            children = ctx.parcela_logica
            flag = False
        elif ctx_type is self.parser.Parcela_logicaContext:
            children = ctx.exp_relacional
            flag = False
        elif ctx_type is self.parser.Exp_relacionalContext:
            children = ctx.exp_aritmetica
            if ctx.op_relacional() != None:
                conversao = True
        elif ctx_type is self.parser.Exp_aritmeticaContext:
            children = ctx.termo
        elif ctx_type is self.parser.TermoContext:
            children = ctx.fator
        elif ctx_type is self.parser.FatorContext:
            children = ctx.parcela
            
        

        if not flag: #flag para verificar o tipo de chamamendo de children
            aux = self.verificarTipo(children())
        else:
            while children(i) != None:
                aux = self.verificarTipo(children(i))
                if aux == None or aux == []:
                    flag = False
                i += 1
                
        #se chegou aqui, então os filhos são compatíveis aos tipos passados
        #caso alguns dos operadores relacionais ou logicos forem utilizados
        #converter o tipo para logico
        if conversao:
            return 'bool'

        print(type(ctx))
        return aux
    
    def conversaoOperadorC(self, operator):
        #converte os diferentes operadores para os correspondentes em C
        if operator == '=':
            return '=='
        elif operator == '<>':
            return '!='
        elif operator == 'ou':
            return '||'
        elif operator == 'e':
            return '&&'
        else:
            return operator
    
    def expresaoToString(self, ctx):
        ctx_type = type(ctx)
        flag = True
        operator = None
        operator2 = False
        i = 0
        if ctx == None:
            return None

        if ctx_type is self.parser.ParcelaContext:
            if ctx.parcela_unario() != None and ctx.parcela_unario().expressao(0) != None:
                print ('string ', ctx.parcela_unario().expressao(0).getText())
                if ctx.parcela_unario().expressao(0).getText().startswith('('):
                    return "(" + self.expresaoToString( ctx.parcela_unario().expressao(0)) + ")"
                
            return ctx.getText()
            
        if ctx_type is self.parser.ExpressaoContext:
            children = ctx.termo_logico
            operator = ctx.op_logico_1
                
        elif ctx_type is self.parser.Termo_logicoContext:
            children = ctx.fator_logico
            operator = ctx.op_logico_2
        elif ctx_type is self.parser.Fator_logicoContext:
            children = ctx.parcela_logica
            flag = False
        elif ctx_type is self.parser.Parcela_logicaContext:
            children = ctx.exp_relacional
            flag = False
        elif ctx_type is self.parser.Exp_relacionalContext:
            children = ctx.exp_aritmetica
            operator = ctx.op_relacional
            operator2 = True
        elif ctx_type is self.parser.Exp_aritmeticaContext:
            children = ctx.termo
            operator = ctx.op1
        elif ctx_type is self.parser.TermoContext:
            children = ctx.fator
            operator = ctx.op2
        elif ctx_type is self.parser.FatorContext:
            children = ctx.parcela
            operator = ctx.op3
        

        if not flag: #flag para verificar o tipo de chamamendo de children
            aux = self.expresaoToString(children())

        else:
            aux = self.expresaoToString(children(0))
            aux2 = ""
            i = 0
            if operator2:
                if operator() != None:
                    aux2 = self.expresaoToString(children(1))
                    aux += ' ' + self.conversaoOperadorC(operator().getText()) + ' ' + aux2
            else:
                while operator(i) != None:
                    aux2 = self.expresaoToString(children(i+1))
                    aux += ' ' + self.conversaoOperadorC(operator(i).getText()) + ' ' + aux2
                    i += 1

        return aux

    # Visit a parse tree produced by AlgumaParser#cmd.
    def visitCmd(self, ctx:AlgumaParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdLeia.
    def visitCmdLeia(self, ctx:AlgumaParser.CmdLeiaContext):
        i = 0
        while ctx.identificador(i) != None:
            
            tipo = self.tabela.verificar(ctx.identificador(i).getText())[0]
            print(tipo)
            
            self.saida += 'scanf(\"' + self.retornarTipoScan(tipo) + '\", &' + ctx.identificador(i).getText() + ');\n'
            i += 1
        return self.visitChildren(ctx)

    def retornarTipoScan(self, tipo):
        if tipo == 'int':
            return '%d'
        elif tipo == 'float':
            return '%f'
        elif tipo == 'string' or tipo.startswith('char['):
            return '%s'
        elif tipo == 'bool':
            return '%d'
        else:
            return ''

    # Visit a parse tree produced by AlgumaParser#cmdEscreva.
    def visitCmdEscreva(self, ctx:AlgumaParser.CmdEscrevaContext):
        i = 0
        while ctx.expressao(i) != None:
            tipo = self.verificarTipo(ctx.expressao(i))
            print('tipo :', tipo)
            self.saida += "printf(\"" + self.retornarTipoScan(tipo) + "\"," + self.expresaoToString(ctx.expressao(i)) + ");\n"
            i += 1
        return self.visitChildren(ctx)


    

    # Visit a parse tree produced by AlgumaParser#cmdSe.
    def visitCmdSe(self, ctx:AlgumaParser.CmdSeContext):
        
        self.saida += 'if (' + self.expresaoToString(ctx.expressao()) + ') {\n'
        i = 0
        while ctx.cmd(i) != None:
            self.visitCmd(ctx.cmd(i))
            i += 1
        self.saida += '}\n'
        if ctx.cmdSenao() != None:
            self.saida += 'else {\n'
            i = 0
            while ctx.cmdSenao().cmd(i) != None:
                self.visitCmd(ctx.cmdSenao().cmd(i))
                i += 1
            self.saida += '}\n'
        
    # Visit a parse tree produced by AlgumaParser#cmdCaso.
    def visitCmdCaso(self, ctx:AlgumaParser.CmdCasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdPara.
    def visitCmdPara(self, ctx:AlgumaParser.CmdParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdEnquanto.
    def visitCmdEnquanto(self, ctx:AlgumaParser.CmdEnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdFaca.
    def visitCmdFaca(self, ctx:AlgumaParser.CmdFacaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdAtribuicao.
    def visitCmdAtribuicao(self, ctx:AlgumaParser.CmdAtribuicaoContext):
        self.saida += ctx.identificador().getText() + ' = ' + self.expresaoToString(ctx.expressao()) + ';\n'
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdChamada.
    def visitCmdChamada(self, ctx:AlgumaParser.CmdChamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdRetorne.
    def visitCmdRetorne(self, ctx:AlgumaParser.CmdRetorneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#selecao.
    def visitSelecao(self, ctx:AlgumaParser.SelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#item_selecao.
    def visitItem_selecao(self, ctx:AlgumaParser.Item_selecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#constantes.
    def visitConstantes(self, ctx:AlgumaParser.ConstantesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#numero_intervalo.
    def visitNumero_intervalo(self, ctx:AlgumaParser.Numero_intervaloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#op_unario.
    def visitOp_unario(self, ctx:AlgumaParser.Op_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#exp_aritmetica.
    def visitExp_aritmetica(self, ctx:AlgumaParser.Exp_aritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#termo.
    def visitTermo(self, ctx:AlgumaParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#fator.
    def visitFator(self, ctx:AlgumaParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#op1.
    def visitOp1(self, ctx:AlgumaParser.Op1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#op2.
    def visitOp2(self, ctx:AlgumaParser.Op2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#op3.
    def visitOp3(self, ctx:AlgumaParser.Op3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#parcela.
    def visitParcela(self, ctx:AlgumaParser.ParcelaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#parcela_unario.
    def visitParcela_unario(self, ctx:AlgumaParser.Parcela_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#parcela_nao_unario.
    def visitParcela_nao_unario(self, ctx:AlgumaParser.Parcela_nao_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#exp_relacional.
    def visitExp_relacional(self, ctx:AlgumaParser.Exp_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#op_relacional.
    def visitOp_relacional(self, ctx:AlgumaParser.Op_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#expressao.
    def visitExpressao(self, ctx:AlgumaParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#termo_logico.
    def visitTermo_logico(self, ctx:AlgumaParser.Termo_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#fator_logico.
    def visitFator_logico(self, ctx:AlgumaParser.Fator_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#parcela_logica.
    def visitParcela_logica(self, ctx:AlgumaParser.Parcela_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#op_logico_1.
    def visitOp_logico_1(self, ctx:AlgumaParser.Op_logico_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#op_logico_2.
    def visitOp_logico_2(self, ctx:AlgumaParser.Op_logico_2Context):
        return self.visitChildren(ctx)



del AlgumaParser