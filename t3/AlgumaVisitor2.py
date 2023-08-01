# Generated from Alguma.g4 by ANTLR 4.13.0
from antlr4 import *

from AlgumaParser import AlgumaParser
from listaErros import listaErros
#from TabelaDeSimbolos import TabelaDeSimbolos

# This class defines a complete generic visitor for a parse tree produced by AlgumaParser.

class AlgumaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgumaParser#programa.
    def visitPrograma(self, ctx:AlgumaParser.ProgramaContext, parser):
        #tabela = TabelaDeSimbolos()
        
        self.tabela = dict()

        self.parser = parser

        self.erros = listaErros()

        self.tiposCompativeis = {"inteiro" : ["inteiro"],
                            "real" : ["inteiro", "real"],
                            "literal" : ["literal"],
                            "logico" : ["logico", "inteiro", "real"],
                            "INVALIDO": ["inteiro", "real", "literal", "INVALIDO"]}

        print(ctx.declaracoes())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#declaracoes.
    def visitDeclaracoes(self, ctx:AlgumaParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#decl_local_global.
    def visitDecl_local_global(self, ctx:AlgumaParser.Decl_local_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgumaParser#declaracao_local.
    def visitDeclaracao_local(self, ctx:AlgumaParser.Declaracao_localContext):
        
        #print(dir(ctx))
        if ctx.IDENT() == None:
            #Caso 1, declaração de uma variavel
            
            i = 0
            while ctx.variavel().identificador(i) != None:
                t = ctx.variavel().identificador(i)
                
                ident = ctx.variavel().identificador(i).IDENT(0).getSymbol()
                i += 1
                tipoVar = None
                if ctx.variavel().tipo().tipo_estendido().tipo_basico_ident().IDENT() != None:
                    tipoVar = ctx.variavel().tipo().tipo_estendido().tipo_basico_ident().IDENT()
                    if tipoVar != None:
                        tipoVar = tipoVar.getSymbol()

                        # if not TabelaDeSimbolos.existe(ident.text):
                        if not tipoVar.text in self.tabela:
                        
                            #listaErros.adicionarErroSemantico(tipoVar, 'tipo ' + tipoVar.text + ' nao declarado')
                            self.erros.adicionarErroVarNaoDecl(t)
                            tipoVar.text = "INVALIDO"
                        #TabelaDeSimbolos.inserir(ident.text, tipoVar.text)
                        self.tabela[ident.text] = tipoVar.text

                        #print('++++++',self.parser.RULE_tipo_basico)
                        #tipoVar = tipoVar.getToken(AlgumaParser.RULE_tipo_basico,0)
                else:
                    #só vai cair aqui se o tipo for um dos tipos basicos declarados
                    tipoVar = ctx.variavel().tipo().tipo_estendido().tipo_basico_ident().tipo_basico()

                    #if TabelaDeSimbolos.existe(ident.text):
                    if ident.text in self.tabela:
                        #printar erro porque a variavel ja foi declarada
                        #listaErros.adicionarErroSemantico(ident, f'identificador '+ ident.text + ' ja declarado anteriormente')
                        self.erros.adicionarErroSemantico(ident, f'identificador {ident.text} ja declarado anteriormente')

                    else:
                        #TabelaDeSimbolos.inserir(ident.text, tipoVar.getText())
                        self.tabela[ident.text] = tipoVar.getText()
                        

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
            #if not TabelaDeSimbolos.existe(t.text):
            if not t.text in self.tabela:
                #listaErros.adicionarErroSemantico(t,  'identificador ' + t.text + ' nao declarado')
                self.erros.adicionarErroVarNaoDecl(t)

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
        
        
        #if TabelaDeSimbolos.existe(ident.text):
        if ident.text in self.tabela:
            #existe e entao, verificar qual tipo
            #tipo = TabelaDeSimbolos.verificar(ident.text)
            tipo = self.tabela[ident.text]

            #dar um jeito de ver se a expressao só faz operações com o mesmo tipo
            exp_aritimetica_temp = ctx.expressao().termo_logico(0).fator_logico(0).parcela_logica().exp_relacional()
            aux = self.verificarTipo(exp_aritimetica_temp, tipo)
            if aux != tipo:
                #listaErros.adicionarErroSemantico(ident, "atribuicao nao compativel para " + ident.text)
                self.erros.adicionarErroSemantico(ident, f"atribuicao nao compativel para {ident.text}")
                                

        else:
            #nao existe, colocar erro
            #listaErros.adicionarErroSemantico(ident, 'identificador ' + ident.text + ' nao declarado')
            self.erros.adicionarErroVarNaoDecl(ident)


        
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
                
            elif ctx.parcela_unario().identificador() != None or ctx.parcela_unario().IDENT() != None:
                if ctx.parcela_unario().identificador() != None:
                    ident = ctx.parcela_unario().identificador().IDENT(0).symbol
                else:
                    ident = ctx.parcela_unario().IDENT(0).symbol
                                    

                #if TabelaDeSimbolos.existe(ident.text):
                if ident.text in self.tabela:
                    #return TabelaDeSimbolos.verificar(ident.text)
                    return self.tabela[ident.text]
                else:
                    #identificador nao existe, adicionar erro
                    #listaErros.adicionarErroSemantico(ident, "identificador " + ident.text + " nao declarado")
                    self.erros.adicionarErroVarNaoDecl(ident)

                    #TabelaDeSimbolos.inserir(ident.text, "INVALIDO")
                    self.tabela[ident.text] = "INVALIDO"
                    return "INVALIDO"
            elif ctx.parcela_unario().NUM_INT() != None:
                
                return "inteiro"
            else:
                
                return "real"
            

        if ctx_type is self.parser.Exp_relacionalContext:
            children = ctx.exp_aritmetica
        elif ctx_type is self.parser.Exp_aritmeticaContext:
            children = ctx.termo
        elif ctx_type is self.parser.TermoContext:
            children = ctx.fator
        elif ctx_type is self.parser.FatorContext:
            children = ctx.parcela
        

        while flag:
            aux = self.verificarTipo(children(i), tipo)
            if aux == None or aux == []:
                flag = False
            elif aux not in AlgumaVisitor.tiposCompativeis[tipo]:
                return aux
            i += 1

        return tipo
        


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
        if ctx.identificador() != None:            
            t = ctx.identificador().IDENT(0).getSymbol()
            #if not TabelaDeSimbolos.existe(t.text):
            if t.text not in self.tabela:
                #listaErros.adicionarErroSemantico(t,  'identificador ' + t.text + ' nao declarado')
                self.erros.adicionarErroVarNaoDecl(t)

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