import time
from classServer import Server
from classClientSuper import ClienteSuper

class Sistema():
    def __init__(self):
        #banco de dados
        self.listaUsuario = [] #fazer a classe usuário
        self.listaUsuario.append(ClienteSuper("Administrador", "...", "admin", "admin", "0"))
        self.S = Server()
        #tem também os produtos, mas vamos com calma, primeiro ver se funciona

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
                    self.S.enviaRespostaRequisicao(sockCli, ".")
                    time.sleep(1)
                    cli.socketCliSuper = sockCli
                    if cli.tipoCliente == "0":  #subsistema FUNCIONARIO                      
                        self.SystemFunc(cli)
                    #if cli.tipoCliente == 1: #subsistema CARRINHO
                    achou = 1
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
            if(operacao == "01" or operacao == "03"): 
                self.listaUsuario.append(ClienteSuper(infD[0], infD[1], infD[2], infD[3], infD[4]))
                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Cadastro feito com sucesso")            
            
            #### MODIFICAR ####
            # 04x!modificado:pessoa  -> infD[0] = modificado e infD[1] = pessoa
            elif(operacao == "041"): #login
                for cli in self.listaUsuario:
                    if (cli.nome == infD[1]):
                        cli.login = infD[0]
                        cli.toString()
                        self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Modificação feita com sucesso")
                        break
                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Usuário não cadastrado")
                
            elif(operacao == "042"): #senha
                for cli in self.listaUsuario:
                    if (cli.nome == infD[1]):
                        cli.senha = infD[0]
                        cli.toString()
                        self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Modificação feita com sucesso")
                        break
                    self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Usuário não cadastrado")

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
            

            #### MOSTRAR ####
            elif(operacao == "09"):
                self.mostratodos(infD[0], funcionario.socketCliSuper)
            

            
        return 
        


##########     SUBSISTEMA CARRINHO     ##########
    #def SystemCar(self)