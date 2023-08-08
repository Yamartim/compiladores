# Generated from Alguma.g4 by ANTLR 4.13.0
from antlr4 import *

from AlgumaParser import AlgumaParser
from listaErros import listaErros
from TabelaDeSimbolos import TabelaDeSimbolos

# This class defines a complete generic visitor for a parse tree produced by AlgumaParser.

class AlgumaVisitor(ParseTreeVisitor):
    tabela = None
    parser = None
    tiposCompativeis = {"inteiro" : ["inteiro"],
                        "real" : ["inteiro", "real"],
                        "literal" : ["literal"],
                        "logico" : ["logico", "inteiro", "real"],
                        "INVALIDO": ["inteiro", "real", "literal", "INVALIDO"]}

    # Visit a parse tree produced by AlgumaParser#programa.
    def visitPrograma(self, ctx:AlgumaParser.ProgramaContext, parser):
        self.tabela = TabelaDeSimbolos()
        lista = listaErros()
        AlgumaVisitor.parser = parser
        print(ctx.declaracoes())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#declaracoes.
    def visitDeclaracoes(self, ctx:AlgumaParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#decl_local_global.
    def visitDecl_local_global(self, ctx:AlgumaParser.Decl_local_globalContext):
        return self.visitChildren(ctx)

    def visitVariavelAux(self, ctx:AlgumaParser.VariavelContext):
        i = 0
        tabelaTemp = TabelaDeSimbolos()
        while ctx.identificador(i) != None:
            t = ctx.identificador(i)
                
            ident = ctx.identificador(i).IDENT(0).getSymbol()
            i += 1
            
            tipoVar = ctx.tipo().getText()
            if tipoVar[0] == '^':
                ponteiro = '&'

            if tipoVar not in self.tiposCompativeis or self.tabela.existe(ident.text) or tabelaTemp.existe(ident.text):
                listaErros.adicionarErroSemantico(ident, 'tipo ' + tipoVar + ' nao declarado')
                tipoVar = "INVALIDO"
            tabelaTemp.inserir(ident.text, tipoVar)

        return tabelaTemp.retornarTabela()

    # Visit a parse tree produced by AlgumaParser#declaracao_local.
    def visitDeclaracao_local(self, ctx:AlgumaParser.Declaracao_localContext):
        ponteiro = ''
        #print(dir(ctx))
        if ctx.variavel() != None:
            #Caso 1, declaração de uma variavel
            temp = self.visitVariavelAux(ctx.variavel())
            if temp != {}:
                self.tabela.concatenar(temp)
            
        elif ctx.tipo() != None:
            ident = ctx.IDENT().getSymbol()
            if self.tabela.existe(ident.text):
                listaErros.adicionarErroSemantico(ident, 'identificador '+ ident.text + ' ja declarado anteriormente')

            elif ctx.tipo().registro() != None:
                #iterar pelos elementos do registro
                dictTemp = TabelaDeSimbolos()
                aux = None
                i = 0
                while ctx.tipo().registro().variavel(i) != None:
                    aux = self.visitVariavelAux(ctx.tipo().registro().variavel(i))
                    print()
                    if aux != {}:
                        keys = list(aux)
                        for key in keys:
                            print(aux)
                            self.tabela.inserir(ident.text + "." + key, aux[key])
                    i += 1
                self.tabela.inserir(ident.text, "registro")
            else:
                tipo = ctx.tipo_basico().getText()
                self.tabela.inserir(ident.text, tipo)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#variavel.
    def visitVariavel(self, ctx:AlgumaParser.VariavelContext):
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


    # Visit a parse tree produced by AlgumaParser#cmd.
    def visitCmd(self, ctx:AlgumaParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdLeia.
    def visitCmdLeia(self, ctx:AlgumaParser.CmdLeiaContext):

        self.verificarIdentVariavel(ctx)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdEscreva.
    def visitCmdEscreva(self, ctx:AlgumaParser.CmdEscrevaContext):


        return self.visitChildren(ctx)

    def verificarIdentVariavel(self, ctx):
        i = 0
        while ctx.identificador(i) != None:
            t = ctx.identificador(i).IDENT(0).getSymbol()
            if not self.tabela.existe(t.text):
                listaErros.adicionarErroSemantico(t,  'identificador ' + t.text + ' nao declarado')
            i += 1
        return

    # Visit a parse tree produced by AlgumaParser#cmdSe.
    def visitCmdSe(self, ctx:AlgumaParser.CmdSeContext):
        return self.visitChildren(ctx)


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
        #print(dir(ctx))
        ident = ctx.identificador().IDENT(0).symbol
        string = ctx.getText()

        
        
        if self.tabela.existe(ident.text):
            #existe e entao, verificar qual tipo
            tipo = self.tabela.verificar(ident.text)
            if string[0] == '^':
                ident.text = '^' + ident.text
                if tipo[0] == '&':
                    tipo = tipo[1:]
            #dar um jeito de ver se a expressao só faz operações com o mesmo tipo
            exp_aritimetica_temp = ctx.expressao().termo_logico(0).fator_logico(0)
            aux = self.verificarTipo(exp_aritimetica_temp, tipo)
            if aux != tipo:
                listaErros.adicionarErroSemantico(ident, "atribuicao nao compativel para " + ident.text)
                                

        else:
            #nao existe, colocar erro
            listaErros.adicionarErroSemantico(ident, 'identificador ' + ident.text + ' nao declarado')

        
        return self.visitChildren(ctx)
    
    def verificarTipo(self, ctx, tipo):
        i = 0
        flag = True
        ret = None
        ctx_type = type(ctx)
        children = None


        if ctx == None:
            return None

        if ctx_type is self.parser.ParcelaContext:
            if ctx.parcela_nao_unario() != None:
                if ctx.parcela_nao_unario().CADEIA() != None:
                    return 'literal'
                else:
                    ident = ctx.parcela_nao_unario().identificador().IDENT(0).symbol
                    if self.tabela.existe(ident.text):
                        return '&' + self.tabela.verificar(ident.text)
                    else:
                        listaErros.adicionarErroSemantico(ident, "identificador " + ident.text + " nao declarado")
                        self.tabela.inserir(ident.text, "INVALIDO")
                        return "INVALIDO"
                
            elif ctx.parcela_unario().identificador() != None or ctx.parcela_unario().IDENT() != None:
                if ctx.parcela_unario().identificador() != None:
                    ident = ctx.parcela_unario().identificador().IDENT(0).symbol
                else:
                    ident = ctx.parcela_unario().IDENT(0).symbol
                                    

                if self.tabela.existe(ident.text):
                    return self.tabela.verificar(ident.text)
                else:
                    #identificador nao existe, adicionar erro
                    listaErros.adicionarErroSemantico(ident, "identificador " + ident.text + " nao declarado")
                    self.tabela.inserir(ident.text, "INVALIDO")
                    return "INVALIDO"
            elif ctx.parcela_unario().NUM_INT() != None:
                
                return "inteiro"
            else:
                
                return "real"
            
        if ctx_type is self.parser.Fator_logicoContext:
            children = ctx.parcela_logica
            flag = False
        elif ctx_type is self.parser.Parcela_logicaContext:
            children = ctx.exp_relacional
            flag = False
        elif ctx_type is self.parser.Exp_relacionalContext:
            children = ctx.exp_aritmetica
        elif ctx_type is self.parser.Exp_aritmeticaContext:
            children = ctx.termo
        elif ctx_type is self.parser.TermoContext:
            children = ctx.fator
        elif ctx_type is self.parser.FatorContext:
            children = ctx.parcela
        

        if not flag:
            aux = self.verificarTipo(children(), tipo)
            if aux == None or aux == []:
                flag = False
            elif aux != tipo and aux not in AlgumaVisitor.tiposCompativeis[tipo]:
                return aux
        else:
            while flag:
                aux = self.verificarTipo(children(i), tipo)
                if aux == None or aux == []:
                    flag = False
                elif aux != tipo and aux not in AlgumaVisitor.tiposCompativeis[tipo]:
                    return aux
                i += 1

        return tipo
        


    # Visit a parse tree produced by AlgumaParser#cmdChamada.
    def visitCmdChamada(self, ctx:AlgumaParser.CmdChamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#cmdRetorne.
    def visitCmdRetorne(self, ctx:AlgumaParser.CmdRetorneContext):
        print(TabelaDeSimbolos.Tabela)
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
        if ctx.identificador() != None:            
            t = ctx.identificador().IDENT(0).getSymbol()
            if not self.tabela.existe(t.text):
                listaErros.adicionarErroSemantico(t,  'identificador ' + t.text + ' nao declarado')
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