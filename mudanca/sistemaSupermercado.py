import time
from classCompra import Compra
from classProduto import Produto
from classServer import Server
from classClientSuper import ClienteSuper

class Sistema():
    def __init__(self):
        #banco de dados
        self.listaUsuario = [] #fazer a classe usuário
        self.listaProdutos = []
        self.S = Server()
        self.listaUsuario.append(ClienteSuper("Administrador", "...", "admin", "admin", "0"))
        self.listaUsuario.append(ClienteSuper("Lucas", "...","lu", "cas", "1"))
        self.listaProdutos.append(Produto("001", "Bolacha", 3, "10.00"))

##########     TELA INICIAL     ##########
    def GerenciaLogin(self, sockCli):
        self.S.enviaRespostaRequisicao(sockCli, "Bem vindo ao sistema JUST TAKE ;)")
        achou = 0
        while True:
            dadosRecv = self.S.recebeRequisicao(sockCli)
            informacoesLogin = dadosRecv.split(':')
            #login:senha
            login = informacoesLogin[0]
            senha = informacoesLogin[1]
            print("recebi: " + login + " : " + senha)
            for cli in self.listaUsuario:
                if login == cli.login and senha == cli.senha:
                    achou = 1
                    self.S.enviaRespostaRequisicao(sockCli, ".")
                    time.sleep(1)
                    cli.socketCliSuper = sockCli
                    if cli.tipoCliente == "0":  #subsistema FUNCIONARIO                      
                        self.SystemFunc(cli)
                    if cli.tipoCliente == "1":  #subsistema CARRINHO
                        self.SystemCar(cli)
                    break
            if achou == 1:
                break
            msgErro = "Desculpe, login ou senha incorreta. Tente novamente \nSe esqueceu a senha, por favor contate um dos nossos atendentes\n\n"
            self.S.enviaRespostaRequisicao(sockCli, msgErro)
            
        self.S.fecharConecServer(sockCli)


##########     SUBSISTEMA FUNCIONARIO     ##########    
    def mostratodos(self, tipo, socEnviar):
        for cli in self.listaUsuario:
            if cli.tipoCliente == tipo:
                self.S.enviaRespostaRequisicao(socEnviar, cli.toString())     
        time.sleep(1)               
        self.S.enviaRespostaRequisicao(socEnviar, "acabou")
        return


    def SystemFunc(self, funcionario):
        msgInit = "Olá " + funcionario.nome
        self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, msgInit)
        while True:
            requisicao = self.S.recebeRequisicao(funcionario.socketCliSuper)
            #print(requisicao)
            infos = requisicao.split('!')
            operacao = infos[0]
            dados = infos[1]
            infD = dados.split(':')
            
            #### FECHAR CONEXÃO #### 
            if(operacao == "00"):
                #self.S.fecharConecServer(funcionario.socketCliSuper)
                break
            
            
            #### ADICIONAR #### 
                #usuários
            if(operacao == "01" or operacao == "03"): 
                self.listaUsuario.append(ClienteSuper(infD[0], infD[1], infD[2], infD[3], infD[4]))
                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Cadastro feito com sucesso")            
            
                #produtos
            if(operacao == "02"):
                self.listaProdutos.append(Produto(infD[0], infD[1], infD[2], infD[3]))
                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Cadastro feito com sucesso")

            #### MODIFICAR ####
                #usuários
            # 04x!modificado:pessoa  -> infD[0] = modificado e infD[1] = pessoa
            elif(operacao == "04"):
                achou = 0
                for user in self.listaUsuario:
                    if(user.nome == infD[0]):
                        achou = 1
                        self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "1")
                        while True:
                            novaRequisicao = self.S.recebeRequisicao(funcionario.socketCliSuper)
                            infos = novaRequisicao.split('!')
                            novaOperacao = infos[0]
                            novosDados = infos[1]    
                            print(novaOperacao)                    
                            #infDadosnovos = novosDados.split(':')
                            if(novaOperacao == "041"): #login
                                user.setLogin(novosDados)
                                user.toString()
                                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Modificação feita com sucesso")
                                
                            elif(novaOperacao == "042"): #senha
                                user.setSenha(novosDados)
                                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Modificação feita com sucesso")
                                
                            elif(novaOperacao == "043"): #contato
                                user.setContato(novosDados)
                                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Modificação feita com sucesso")
                            
                            elif(novaOperacao == "00"):
                                break

                if(achou == 0):
                    self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "0")
                
            #produtos
            elif(operacao == "05"):
                achou = 0
                for prod in self.listaProdutos:
                    if(prod.id == infD[0]):
                        achou = 1
                        self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "1")
                        while True:
                            novaRequisicao = self.S.recebeRequisicao(funcionario.socketCliSuper)
                            infos = novaRequisicao.split('!')
                            novaOperacao = infos[0]
                            novosDados = infos[1]                        
                            infDadosnovos = novosDados.split(':')
                            if(novaOperacao == "051"):
                                #quantidade
                                prod.setQuantidade(infDadosnovos[0])
                                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Modificação feita com sucesso")
                            elif(novaOperacao == "052"):
                                #preço
                                prod.setPreco(infDadosnovos[0])
                                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Modificação feita com sucesso")
                            
                            elif(novaOperacao == "00"):
                                break
                
                if(achou == 0):
                    self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "0")


            #### REMOVER ####
            elif(operacao == "06"):
                achou = 0
                for cli in self.listaUsuario:
                    if(cli.nome == infD[0]):
                        achou = 1
                        self.listaUsuario.remove(cli)
                        self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Usuário removido com sucesso")
                        break
                if achou == 0:
                    self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Usuário não cadastrado")
            
            elif(operacao == "08"):
                achou = 0
                for prod in self.listaProdutos:
                    if(prod.id == infD[0]):
                        achou = 1
                        self.listaProdutos.remove(prod)
                        self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Produto removido com sucesso")
                        break
                if achou == 0:
                    self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Produto não cadastrado")
            

            #### MOSTRAR ####
                #usuários
            elif(operacao == "09"):
                self.mostratodos(infD[0], funcionario.socketCliSuper)
                
                #produtos
            elif(operacao == "11"):
                for p in self.listaProdutos:
                    self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, p.toString())
                time.sleep(1)
                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "acabou")

                
        return 
        


##########     SUBSISTEMA CARRINHO     ##########
    def alterarQuantidade(self, produto):
        for p in self.listaProdutos:
            if p.id == produto.id:
                p.setQuantidade(p.quantidade-1)
                break


    def SystemCar(self, comprador):
        msgInit = "Olá " + comprador.nome
        self.S.enviaRespostaRequisicao(comprador.socketCliSuper, msgInit)
        compra = Compra()
        while True:
            achou = 0
            produto = self.S.recebeRequisicao(comprador.socketCliSuper)
            if produto == "sair": 
                for prod in compra.listaprodutos:
                    print(prod.toStringCompra())
                    self.alterarQuantidade(prod)
                print(compra.total)    
                break
            for p in self.listaProdutos:
                if p.id == produto:
                    achou = 1
                    compra.inserirProduto(p)
                    msgCompra = p.nome + " R$: " + p.preco
                    self.S.enviaRespostaRequisicao(comprador.socketCliSuper, msgCompra)
            if achou == 0:
                self.S.enviaRespostaRequisicao(comprador.socketCliSuper, "Produto não cadastrado")
            

        for prod in self.listaProdutos:
            print(prod.toString())
        return