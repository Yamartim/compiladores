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
                        "INVALIDO": ["inteiro", "real", "literal", "INVALIDO"],
                        "registro" : ["registro"]}
    
    def construtor(self, tabelaCriada):
        self.tabela = TabelaDeSimbolos()
        self.tabela.concatenar(tabelaCriada.Tabela)

    def separaIdentDimensao(self, ctx:AlgumaParser.IdentificadorContext):
        listaIDENT = []
        listaDimensao = []

        if type(ctx) is str:
            temp = ctx.split('[', 1)
            listaIDENT = temp[0]
            if len(temp) > 1:
                temp[1].replace(']', '')
                listaDimensao = temp[1].split('[')
        else:
                
            i=0
            while ctx.IDENT(i) != None:
                listaIDENT.append(ctx.IDENT(i).getText())
                i += 1
            
            i = 0
            while ctx.dimensao().exp_aritmetica(i) != None:
                listaDimensao.append(ctx.dimensao().exp_aritmetica(i))
                i += 1

        return listaIDENT, listaDimensao
 
    # Visit a parse tree produced by AlgumaParser#programa.
    def visitPrograma(self, ctx:AlgumaParser.ProgramaContext, parser):
        self.tabela = TabelaDeSimbolos()
        self.funcoes = TabelaDeSimbolos()
        lista = listaErros()
        AlgumaVisitor.parser = parser
        return self.visitChildren(ctx)

#region metodos nao usados 1

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
            if self.tabela.existe(ident.text):
                listaErros.adicionarErroSemantico(ident, 'identificador '+ ident.text + ' ja declarado anteriormente')
                continue
            _, dimensao = self.separaIdentDimensao(t)
            tipoVar = ctx.tipo().getText()
            if tipoVar[0] == '^' :
                ponteiro = True
                tipoVar = tipoVar[1:]
            else:
                ponteiro = False
            
            

            if ctx.tipo().registro() is not None:
                j = 0
                tipoVar = TabelaDeSimbolos()
                while ctx.tipo().registro().variavel(j) is not None:
                    aux = self.visitVariavelAux(ctx.tipo().registro().variavel(j))
                    if aux != {}:
                        tipoVar.concatenar(aux)
                    j += 1

            elif tipoVar not in self.tiposCompativeis and not self.tabela.existe(tipoVar) and not tabelaTemp.existe(tipoVar):
                listaErros.adicionarErroSemantico(ident, 'tipo ' + tipoVar + ' nao declarado')
                tipoVar = "INVALIDO"

            else:
                for parte in dimensao:
                    #cada parte é uma expressao aritmetica, como definem o tamanho de um vetor
                    #devem ser inteiros
                    aux = self.verificarTipo(parte, "inteiro")
                    if aux != "inteiro":
                        #colocar erro porque exp nao inteiras estao sendo utilizadas em dimensoes
                        #sem implementação porque nao há caso de teste para isto
                        pass
                    else:
                        ponteiro = True
                
            tabelaTemp.inserir(ident.text, [tipoVar, ponteiro])

        return tabelaTemp.retornarTabela()
#endregion

    # Visit a parse tree produced by AlgumaParser#declaracao_local.
    def visitDeclaracao_local(self, ctx:AlgumaParser.Declaracao_localContext):
        ponteiro = False
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
                    if aux != {}:
                        dictTemp.concatenar(aux)
                    i += 1

                self.tabela.inserir(ident.text, [dictTemp, ponteiro])
        else:
            #constantes
            ident = ctx.IDENT().getSymbol()
            tipo = ctx.tipo_basico().getText()
            if tipo.startswith('^'):
                ponteiro = True
            self.tabela.inserir(ident.text, [tipo, ponteiro])

        return self.visitChildren(ctx)

#region metodos nao usados 2

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
        ident = ctx.IDENT().symbol
        tipoFunc = None
        if self.tabela.existe(ident.text):
            #adicionar erro porque esse identificador já está em uso
            listaErros.adicionarErroSemantico(ident, 'identificador '+ ident.text + ' ja declarado anteriormente')

        else:
            if ctx.parametros() != None:
                i = 0
                t = TabelaDeSimbolos()
                #t.concatenar(self.tabela.Tabela)
                while ctx.parametros().parametro(i)!= None:
                    tipo = ctx.parametros().parametro(i).tipo_estendido().getText()
                    j = 0
                    while ctx.parametros().parametro(i).identificador(j) != None:
                        t.inserir(ctx.parametros().parametro(i).identificador(j).getText(), [tipo, False])
                        j += 1
                    i += 1
                aux = AlgumaVisitor()
                tParam = TabelaDeSimbolos()
                tParam.concatenar(t.Tabela)
                tParam.concatenar(self.tabela.Tabela)
                aux.construtor(tParam)
                '''
                print('**************************************************')
                print('definição da funcao ', ident.text)
                print(t.Tabela)
                print('**************************************************')
                '''

            #adicionar a função/procedimento na tabela de simbolos
            if ctx.tipo_estendido() != None:
                tipoFunc = ctx.tipo_estendido().getText()
                tipoVerificar = tipo
                if tipo[0] == '^':
                    tipoVerificar = tipo[1:]
                if tipoVerificar in self.tiposCompativeis or self.tabela.existe(tipoVerificar):
                    self.funcoes.inserir(ident.text, [t ,tipoFunc])
                else:
                    #adicionar erro pois tipo não existe
                    listaErros.adicionarErroSemantico(ident, 'tipo ' + tipo + ' nao declarado')
            else:
                self.funcoes.inserir(ident.text, [t, None]) # em vez de None, também poderia ser o tipoFunc porque também
                                                            # seria None caso chegasse nesse ponto

            i = 0
            while ctx.declaracao_local(i) != None:
                aux.visitDeclaracao_local(ctx.declaracao_local(i))
                i += 1

            i = 0
            while ctx.cmd(i) != None:
                aux.visitCmd(ctx.cmd(i))
                if ctx.cmd(i).cmdRetorne() != None:
                    if tipoFunc == None:
                        listaErros.adicionarErroSemantico(ctx.cmd(i).cmdRetorne().start ,'comando retorne nao permitido nesse escopo')
                    else:
                        print('tipo : ', tipo)
                        auxTipo = aux.resolveRetorne(ctx.cmd(i).cmdRetorne(), tipo)
                        print('auxTipo : ', auxTipo)
                        token = ctx.cmd(i).cmdRetorne().start
                        print(token.line)
                        #nodes = pctx.getTokens(pctx.getStart(), pctx.getStop())
                        #print(nodes)


                i += 1
            
 
        #return self.visitChildren(ctx)


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

#endregion

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
            text = ctx.identificador(i).getText()
            if not self.tabela.existe(t.text):
                #se o primeiro IDENT não existir, adicione erro
                listaErros.adicionarErroSemantico(t,  'identificador ' + text + ' nao declarado')
            else:
                var = self.tabela.verificar(t.text)
                if ctx.identificador(i).IDENT(1) != None:
                    ident1 = ctx.identificador(i).IDENT(1).getText()
                    var = var[0]
                    if type(var) is str and var not in AlgumaVisitor.tiposCompativeis:
                        if self.tabela.existe(var):
                            var = self.tabela.verificar(var)
                            var = var[0]
                    if type(var) is TabelaDeSimbolos and not var.existe(ident1):
                        #este if verifica 3 coisas, 
                        #1 se o identificador está acessando algo com mais de 1 IDENT
                        #2 se o tipo retornado é um registro, neste caso, uma outra TabelaDeSimbolos (registros são armazenados assim)
                        #3 se o tipo acessado dentro do registro não existe
                        #caso tudo isso seja verdade, então deve-se adicionar o erro
                        listaErros.adicionarErroSemantico(t,  'identificador ' + text + ' nao declarado')
            i += 1
        return

#region metodos nao usados 3

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

#endregion

    # Visit a parse tree produced by AlgumaParser#cmdAtribuicao.
    def visitCmdAtribuicao(self, ctx:AlgumaParser.CmdAtribuicaoContext):
        ponteiro = ''
        if ctx.getText()[0] == '^':
            ponteiro = '&'
            ponteiro2 = '^'
        else:
            ponteiro2 = ''
        
        ident = ctx.identificador().getText()
        partes, dimensao = self.separaIdentDimensao(ctx.identificador())

        #partes = ident.split('.')

        if self.tabela.existe(partes[0]):

            tipoVar = self.tabela.verificar(partes[0])
            if len(partes) > 1:
                #print('é um tipo diferente')
                if type(tipoVar[0]) is not TabelaDeSimbolos: #caso seja um tipo declarado anteriormente,
                                                             #recupere-o
                    tipoVar = self.tabela.verificar(tipoVar[0])
                
                tipoVar = tipoVar[0].verificar(partes[1]) #acesse a segunda parte do identificador
                
            if tipoVar == None:
                #retornou None nas verificações acima, tipo não declarado
                listaErros(ctx.getToken(), 'identificador ' + ident + ' nao declarado')
                return self.visitChildren(ctx)
                    
            if tipoVar[1] and (ponteiro == '&' or len(dimensao) > 0):
                ponteiro = ''
            
            
            #dar um jeito de ver se a expressao só faz operações com o mesmo tipo
            exp_aritimetica_temp = ctx.expressao()
            aux = self.verificarTipo(exp_aritimetica_temp, ponteiro + tipoVar[0])
            if aux[0] == '&' and tipoVar[1]:
                aux = aux[1:]

            if aux != tipoVar[0] and not (tipoVar[0] in self.tiposCompativeis and aux in self.tiposCompativeis[tipoVar[0]]):
                print('aux eh ', aux)
                print('tipo esperado era ', tipoVar[0])
                listaErros.adicionarErroSemantico(ctx.identificador().IDENT(0).symbol, "atribuicao nao compativel para " + ponteiro2 + ident)
                                

        else:
            #nao existe esse identificador, colocar erro
            token = ctx.identificador().IDENT(0).getSymbol()
            mensagem = 'identificador ' + ident + ' nao declarado'
            listaErros.adicionarErroSemantico(token, mensagem)

        
        return self.visitChildren(ctx)
    

    def verificarTipo(self, ctx, tipo):
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
                    return 'literal'
                else:
                    ident = ctx.parcela_nao_unario().identificador().IDENT(0).symbol
                    if self.tabela.existe(ident.text):
                        return '&' + self.tabela.verificar(ident.text)[0]
                    else:
                        listaErros.adicionarErroSemantico(ident, "identificador " + ident.text + " nao declarado")
                        self.tabela.inserir(ident.text, "INVALIDO")
                        return "INVALIDO"
                
            elif ctx.parcela_unario().identificador() != None:
                if ctx.parcela_unario().identificador() != None:
                    ident = ctx.parcela_unario().identificador().IDENT(0).symbol
                else:
                    ident = ctx.parcela_unario().IDENT().symbol
                
                                    

                if self.tabela.existe(ident.text):
                    return self.tabela.verificar(ident.text)[0]
                elif self.funcoes.existe(ident.text):
                    return self.funcoes.verificar(ident.text)[1]
                else:
                    #identificador nao existe, adicionar erro
                    listaErros.adicionarErroSemantico(ident, "identificador " + ident.text + " nao declarado")
                    self.tabela.inserir(ident.text, "INVALIDO")
                    return "INVALIDO"
            elif ctx.parcela_unario().NUM_INT() != None:
                return "inteiro"
            
            elif ctx.parcela_unario().NUM_REAL() != None:
                return "real"
            
            elif ctx.parcela_unario().IDENT() != None:
                #entao é uma chamada, verificar tipo na tabela de funções
                ident = ctx.parcela_unario().IDENT().symbol
                
                if self.funcoes.existe(ident.text):
                    return self.funcoes.verificar(ident.text)[1]
                else:
                    #chamada de uma função na declarada, portanto, adicionar erro
                    listaErros.adicionarErroSemantico(ident, 'funcao ' + ident.text + ' nao declarada')
                    self.funcoes.inserir(ident.text, [None, "INVALIDO"])
                    return "INVALIDO"
            
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
            aux = self.verificarTipo(children(), tipo)
            if aux == None or aux == []:
                flag = False
            elif aux != tipo and tipo not in AlgumaVisitor.tiposCompativeis:
                return aux
            elif aux in AlgumaVisitor.tiposCompativeis: #significa que o tipo é um dos tipos básicos,
                                                        #deve-se analisar a compatibilidade
                if aux not in AlgumaVisitor.tiposCompativeis[tipo]: #verificar se o tipo não aceita aux
                    return aux #se não aceitar, retorne aux (todas as chamadas anteriores retornarão aux)
            aux2 = aux
        else:
            while flag:
                aux = self.verificarTipo(children(i), tipo)
                if aux == None or aux == []:
                    flag = False
                    aux2 = self.verificarTipo(children(i-1), tipo)
                elif aux != tipo and tipo not in AlgumaVisitor.tiposCompativeis:
                    return aux
                elif aux in AlgumaVisitor.tiposCompativeis: #mesma explicação acima
                    if aux not in AlgumaVisitor.tiposCompativeis[tipo]: #verificar se o tipo não aceita aux
                        return aux #se não aceitar, retorne aux (todas as chamadas anteriores retornarão aux)
                i += 1

        #se chegou aqui, então os filhos são compatíveis aos tipos passados
        #caso alguns dos operadores relacionais ou logicos forem utilizados
        #converter o tipo para logico
        if conversao:
            return 'logico'

        return aux2
        

#region metodos nao usados 3

    # Visit a parse tree produced by AlgumaParser#cmdChamada.
    def visitCmdChamada(self, ctx:AlgumaParser.CmdChamadaContext):
        ident = ctx.IDENT().symbol
        if not self.funcoes.existe(ident.text):
            listaErros.adicionarErroSemantico(ident, "procedimento " + ident.text + "não declarado")
        else:
            #por enquanto, só verificaremos por erros
            lista = self.funcoes.verificar(ident.text)
            tabela = lista[0]
            itens = list(tabela.Tabela)
            
            '''
            print('---------------------------------------')
            print('PARAMETROS')
            print(tabela.Tabela)
            print('---------------------------------------')
            '''

            for i in range(0,len(tabela.Tabela)):
                #print('ITEM -> ', itens[i], ' ', i, '/', len(tabela.Tabela))
                expr = ctx.expressao(i)
                tipoParam = tabela.verificar(itens[i])
                if expr == None:
                    listaErros.adicionarErroSemantico(ident, 'incompatibilidade de parametros na chamada de ' + ident.text)
                    break
                else:
                    expr = ctx.expressao(i)
                    aux = self.verificarTipo(expr, tipoParam[0])
                    if aux == None or aux != tipoParam[0]:
                        #se os tipos forem diferentes, adicione erro
                        listaErros.adicionarErroSemantico(ident, 'incompatibilidade de parametros na chamada de ' + ident.text)
                        break

            
        return self.visitChildren(ctx)


    # uma pequena função para resolver o tipo do Retorne.
    def resolveRetorne(self, ctx:AlgumaParser.CmdRetorneContext, tipo):
        exp_aritimetica_temp = ctx.expressao()            
        aux = self.verificarTipo(exp_aritimetica_temp, tipo)
        return aux

    # Visit a parse tree produced by AlgumaParser#selecao.
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

#endregion

    # Visit a parse tree produced by AlgumaParser#parcela_unario.
    def visitParcela_unario(self, ctx:AlgumaParser.Parcela_unarioContext):
        if ctx.identificador() != None:            
            t = ctx.identificador().IDENT(0).getSymbol()
            text = ctx.identificador().getText()
            
            partes, dimensao = self.separaIdentDimensao(ctx.identificador())
            if not self.tabela.existe(partes[0]):
                listaErros.adicionarErroSemantico(t,  'identificador ' + text + ' nao declarado')
            tipo = self.tabela.verificar(partes[0])

            if tipo == None:
                listaErros.adicionarErroSemantico(t,  'identificador ' + text + ' nao declarado')
            elif len(partes) > 1:
                '''
                print('partes : ', partes)
                print('tipo : ', tipo)
                print(self.tabela.Tabela)
                '''
                if type(tipo[0]) is not TabelaDeSimbolos and self.tabela.existe(tipo[0]): #caso seja um tipo registro declarado anteriormente,
                                                          #recupere-o
                    tipo = self.tabela.verificar(tipo[0])

                if type(tipo[0]) is TabelaDeSimbolos:
                    tipo = tipo[0].verificar(partes[1]) #acesse a segunda parte do identificador
                #print('texto eh ', text)
                #print('linha : ', t.line, ' retornou ', tipo)
                
                if tipo is None: #quer dizer que alguma verificação acima retornou Falso
                    listaErros.adicionarErroSemantico(t,  'identificador ' + text + ' nao declarado')
        elif ctx.IDENT() != None:
            #entao é uma chamada, passar contexto para ela
            self.visitCmdChamada(ctx)
                
        return self.visitChildren(ctx)

#region metodos nao usados 4

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

#endregion

del AlgumaParser