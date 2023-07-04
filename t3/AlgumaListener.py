# Generated from Alguma.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .AlgumaParser import AlgumaParser
else:
    from AlgumaParser import AlgumaParser

# This class defines a complete listener for a parse tree produced by AlgumaParser.
class AlgumaListener(ParseTreeListener):

    # Enter a parse tree produced by AlgumaParser#programa.
    def enterPrograma(self, ctx:AlgumaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by AlgumaParser#programa.
    def exitPrograma(self, ctx:AlgumaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by AlgumaParser#declaracoes.
    def enterDeclaracoes(self, ctx:AlgumaParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by AlgumaParser#declaracoes.
    def exitDeclaracoes(self, ctx:AlgumaParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by AlgumaParser#decl_local_global.
    def enterDecl_local_global(self, ctx:AlgumaParser.Decl_local_globalContext):
        pass

    # Exit a parse tree produced by AlgumaParser#decl_local_global.
    def exitDecl_local_global(self, ctx:AlgumaParser.Decl_local_globalContext):
        pass


    # Enter a parse tree produced by AlgumaParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:AlgumaParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by AlgumaParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:AlgumaParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by AlgumaParser#variavel.
    def enterVariavel(self, ctx:AlgumaParser.VariavelContext):
        pass

    # Exit a parse tree produced by AlgumaParser#variavel.
    def exitVariavel(self, ctx:AlgumaParser.VariavelContext):
        pass


    # Enter a parse tree produced by AlgumaParser#identificador.
    def enterIdentificador(self, ctx:AlgumaParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by AlgumaParser#identificador.
    def exitIdentificador(self, ctx:AlgumaParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by AlgumaParser#dimensao.
    def enterDimensao(self, ctx:AlgumaParser.DimensaoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#dimensao.
    def exitDimensao(self, ctx:AlgumaParser.DimensaoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#tipo.
    def enterTipo(self, ctx:AlgumaParser.TipoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#tipo.
    def exitTipo(self, ctx:AlgumaParser.TipoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#tipo_basico.
    def enterTipo_basico(self, ctx:AlgumaParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#tipo_basico.
    def exitTipo_basico(self, ctx:AlgumaParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:AlgumaParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by AlgumaParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:AlgumaParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by AlgumaParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:AlgumaParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:AlgumaParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#valor_constante.
    def enterValor_constante(self, ctx:AlgumaParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by AlgumaParser#valor_constante.
    def exitValor_constante(self, ctx:AlgumaParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by AlgumaParser#registro.
    def enterRegistro(self, ctx:AlgumaParser.RegistroContext):
        pass

    # Exit a parse tree produced by AlgumaParser#registro.
    def exitRegistro(self, ctx:AlgumaParser.RegistroContext):
        pass


    # Enter a parse tree produced by AlgumaParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:AlgumaParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by AlgumaParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:AlgumaParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by AlgumaParser#parametro.
    def enterParametro(self, ctx:AlgumaParser.ParametroContext):
        pass

    # Exit a parse tree produced by AlgumaParser#parametro.
    def exitParametro(self, ctx:AlgumaParser.ParametroContext):
        pass


    # Enter a parse tree produced by AlgumaParser#parametros.
    def enterParametros(self, ctx:AlgumaParser.ParametrosContext):
        pass

    # Exit a parse tree produced by AlgumaParser#parametros.
    def exitParametros(self, ctx:AlgumaParser.ParametrosContext):
        pass


    # Enter a parse tree produced by AlgumaParser#corpo.
    def enterCorpo(self, ctx:AlgumaParser.CorpoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#corpo.
    def exitCorpo(self, ctx:AlgumaParser.CorpoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmd.
    def enterCmd(self, ctx:AlgumaParser.CmdContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmd.
    def exitCmd(self, ctx:AlgumaParser.CmdContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdLeia.
    def enterCmdLeia(self, ctx:AlgumaParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdLeia.
    def exitCmdLeia(self, ctx:AlgumaParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:AlgumaParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:AlgumaParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdSe.
    def enterCmdSe(self, ctx:AlgumaParser.CmdSeContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdSe.
    def exitCmdSe(self, ctx:AlgumaParser.CmdSeContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdCaso.
    def enterCmdCaso(self, ctx:AlgumaParser.CmdCasoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdCaso.
    def exitCmdCaso(self, ctx:AlgumaParser.CmdCasoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdPara.
    def enterCmdPara(self, ctx:AlgumaParser.CmdParaContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdPara.
    def exitCmdPara(self, ctx:AlgumaParser.CmdParaContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:AlgumaParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:AlgumaParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdFaca.
    def enterCmdFaca(self, ctx:AlgumaParser.CmdFacaContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdFaca.
    def exitCmdFaca(self, ctx:AlgumaParser.CmdFacaContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdAtribuicao.
    def enterCmdAtribuicao(self, ctx:AlgumaParser.CmdAtribuicaoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdAtribuicao.
    def exitCmdAtribuicao(self, ctx:AlgumaParser.CmdAtribuicaoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdChamada.
    def enterCmdChamada(self, ctx:AlgumaParser.CmdChamadaContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdChamada.
    def exitCmdChamada(self, ctx:AlgumaParser.CmdChamadaContext):
        pass


    # Enter a parse tree produced by AlgumaParser#cmdRetorne.
    def enterCmdRetorne(self, ctx:AlgumaParser.CmdRetorneContext):
        pass

    # Exit a parse tree produced by AlgumaParser#cmdRetorne.
    def exitCmdRetorne(self, ctx:AlgumaParser.CmdRetorneContext):
        pass


    # Enter a parse tree produced by AlgumaParser#selecao.
    def enterSelecao(self, ctx:AlgumaParser.SelecaoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#selecao.
    def exitSelecao(self, ctx:AlgumaParser.SelecaoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#item_selecao.
    def enterItem_selecao(self, ctx:AlgumaParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#item_selecao.
    def exitItem_selecao(self, ctx:AlgumaParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#constantes.
    def enterConstantes(self, ctx:AlgumaParser.ConstantesContext):
        pass

    # Exit a parse tree produced by AlgumaParser#constantes.
    def exitConstantes(self, ctx:AlgumaParser.ConstantesContext):
        pass


    # Enter a parse tree produced by AlgumaParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:AlgumaParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by AlgumaParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:AlgumaParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by AlgumaParser#op_unario.
    def enterOp_unario(self, ctx:AlgumaParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by AlgumaParser#op_unario.
    def exitOp_unario(self, ctx:AlgumaParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by AlgumaParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:AlgumaParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by AlgumaParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:AlgumaParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by AlgumaParser#termo.
    def enterTermo(self, ctx:AlgumaParser.TermoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#termo.
    def exitTermo(self, ctx:AlgumaParser.TermoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#fator.
    def enterFator(self, ctx:AlgumaParser.FatorContext):
        pass

    # Exit a parse tree produced by AlgumaParser#fator.
    def exitFator(self, ctx:AlgumaParser.FatorContext):
        pass


    # Enter a parse tree produced by AlgumaParser#op1.
    def enterOp1(self, ctx:AlgumaParser.Op1Context):
        pass

    # Exit a parse tree produced by AlgumaParser#op1.
    def exitOp1(self, ctx:AlgumaParser.Op1Context):
        pass


    # Enter a parse tree produced by AlgumaParser#op2.
    def enterOp2(self, ctx:AlgumaParser.Op2Context):
        pass

    # Exit a parse tree produced by AlgumaParser#op2.
    def exitOp2(self, ctx:AlgumaParser.Op2Context):
        pass


    # Enter a parse tree produced by AlgumaParser#op3.
    def enterOp3(self, ctx:AlgumaParser.Op3Context):
        pass

    # Exit a parse tree produced by AlgumaParser#op3.
    def exitOp3(self, ctx:AlgumaParser.Op3Context):
        pass


    # Enter a parse tree produced by AlgumaParser#parcela.
    def enterParcela(self, ctx:AlgumaParser.ParcelaContext):
        pass

    # Exit a parse tree produced by AlgumaParser#parcela.
    def exitParcela(self, ctx:AlgumaParser.ParcelaContext):
        pass


    # Enter a parse tree produced by AlgumaParser#parcela_unario.
    def enterParcela_unario(self, ctx:AlgumaParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by AlgumaParser#parcela_unario.
    def exitParcela_unario(self, ctx:AlgumaParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by AlgumaParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:AlgumaParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by AlgumaParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:AlgumaParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by AlgumaParser#exp_relacional.
    def enterExp_relacional(self, ctx:AlgumaParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by AlgumaParser#exp_relacional.
    def exitExp_relacional(self, ctx:AlgumaParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by AlgumaParser#op_relacional.
    def enterOp_relacional(self, ctx:AlgumaParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by AlgumaParser#op_relacional.
    def exitOp_relacional(self, ctx:AlgumaParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by AlgumaParser#expressao.
    def enterExpressao(self, ctx:AlgumaParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#expressao.
    def exitExpressao(self, ctx:AlgumaParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#termo_logico.
    def enterTermo_logico(self, ctx:AlgumaParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#termo_logico.
    def exitTermo_logico(self, ctx:AlgumaParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#fator_logico.
    def enterFator_logico(self, ctx:AlgumaParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by AlgumaParser#fator_logico.
    def exitFator_logico(self, ctx:AlgumaParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by AlgumaParser#parcela_logica.
    def enterParcela_logica(self, ctx:AlgumaParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by AlgumaParser#parcela_logica.
    def exitParcela_logica(self, ctx:AlgumaParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by AlgumaParser#op_logico_1.
    def enterOp_logico_1(self, ctx:AlgumaParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by AlgumaParser#op_logico_1.
    def exitOp_logico_1(self, ctx:AlgumaParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by AlgumaParser#op_logico_2.
    def enterOp_logico_2(self, ctx:AlgumaParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by AlgumaParser#op_logico_2.
    def exitOp_logico_2(self, ctx:AlgumaParser.Op_logico_2Context):
        pass



del AlgumaParser