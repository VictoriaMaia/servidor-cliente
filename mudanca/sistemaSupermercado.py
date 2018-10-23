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
                    self.S.enviaRespostaRequisicao(sockCli, "Achei")
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
    def SystemFunc(self, funcionario):
        print("entrei?")
        msgInit = "Olá " + funcionario.nome
        self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, msgInit)
        while True:
            requisicao = self.S.recebeRequisicao(funcionario.socketCliSuper)
            print(requisicao)
            infos = requisicao.split('!')
            operacao = infos[0]
            dados = infos[1]
            infD = dados.split(':')
            if(operacao == "01" or operacao == "03"):
                self.listaUsuario.append(ClienteSuper(infD[0], infD[1], infD[2], infD[3], infD[4]))
                self.S.enviaRespostaRequisicao(funcionario.socketCliSuper, "Cadastro feito com sucesso")
            
            if(operacao == "00"):
                #self.S.fecharConecServer(funcionario.socketCliSuper)
                break
        return 



##########     SUBSISTEMA CARRINHO     ##########
    #def SystemCar(self)