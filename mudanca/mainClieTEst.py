import os
import time
import socket
import FuncsComuns as fc
from classClient import Cliente

def menuPrincipal():
    print("00 - Sair")
    print("01 - Cadastrar funcionário \n02 - Cadastrar produto \n03 - Cadastrar cliente")
    print("04 - Alterar cadastro \n05 - Alterar Produto")
    print("06 - Remover funcionário \n07 - Remover cliente \n08 - Remover produto")
    print("09 - Mostrar funcionários \n10 - Mostrar clientes \n11 - Mostrar produtos")

def menuAlterarCadastro():
    print("00 - Voltar \n01 - Alterar Login \n02 - Alterar Senha \n03 - Alterar contato")

def menuAlterarProduto():
    print("00 - Voltar \n01 - Alterar Quantidade \n02 - Alterar Preço")

def montarRequisicao(quant, parametros):
    infosPedir = parametros.split(':')
    requisit = input(infosPedir[0]+": ")
    i = 1
    while i < quant:
        ler = input(infosPedir[i]+": ")
        requisit += ":" + ler
        i = i+1
    
    return requisit
     

if __name__ == "__main__":
    cli = Cliente()
    #tela inicial, conseguiu conectar
    print(cli.recebeResposta())
    fc.TelaLogin(cli)
    print(cli.recebeResposta())
    #conseguiLogar
    
    while True:        
        time.sleep(2)
        os.system("clear")
        print("Bem vindo ao sistema de funcionários!")
        menuPrincipal()
        op = input("Digite a opção que deseja realizar: ")
        if(op == "00"):
            requisicao = "00!"
            requisicao += " "
            cli.enviarRequisicao(requisicao)
            break
        
        if(op == "01"):
            requisicao = "01!"
            requisicao += montarRequisicao(4, "nome:contato:login:senha")
            requisicao = requisicao + ":0"
            cli.enviarRequisicao(requisicao)
            print(cli.recebeResposta())

        elif(op == "02"):
            requisicao = "02!"
            requisicao += montarRequisicao(4, "id:nome:quantidade:preço")
            cli.enviarRequisicao(requisicao)
            print(cli.recebeResposta())
        
        elif(op == "03"):
            requisicao = "03!"
            requisicao += montarRequisicao(4, "nome:contato:login:senha")
            requisicao = requisicao + ":1"
            cli.enviarRequisicao(requisicao)
            print(cli.recebeResposta())
        
        elif(op == "04"):
            #verificar se a pessoa existe antes de perguntar o que deseja alterar!
            alterarPess = input("Digite o nome do usuário que deseja alterar as informações: ")
            requisicao = "04!" + alterarPess
            cli.enviarRequisicao(requisicao)
            existeUser = cli.recebeResposta()
            if existeUser == "1":
                while True:
                    time.sleep(2)
                    os.system("clear")            
                    print("Deseja modificar qual informação do usuário " + alterarPess + "?")
                    menuAlterarCadastro()
                    op2 = input()
                    if(op2 == "00"):
                        cli.enviarRequisicao("00!")
                        break
                    if(op2 == "01"):
                        requisicao = "041!"
                        requisicao += montarRequisicao(1, "Novo login")
                        cli.enviarRequisicao(requisicao)
                        print(cli.recebeResposta())

                    elif(op2 == "02"):
                        requisicao = "042!"
                        requisicao += montarRequisicao(1, "Nova senha")
                        cli.enviarRequisicao(requisicao)
                        print(cli.recebeResposta())

                    elif(op2 == "03"):
                        requisicao = "043!"
                        requisicao += montarRequisicao(1, "Novo Contato")
                        cli.enviarRequisicao(requisicao)
                        print(cli.recebeResposta())

                    else:
                        print("Opção inválida")
            else:
                print("Usuário não cadastrado")

        
        elif(op == "05"):
            alterarProd = input("Digite o id do produto que deseja alterar as informações: ")
            requisicao = "05!" + alterarProd
            cli.enviarRequisicao(requisicao)
            existeProduto = cli.recebeResposta()
            if existeProduto == "1":
                while True:
                    time.sleep(2)
                    os.system("clear")
                    print("Deseja modificar qual informação do produto " + alterarProd + "?")
                    menuAlterarProduto()
                    op2 = input()
                    if(op2 == "00"):
                        cli.enviarRequisicao("00!")
                        break
                    if(op2 == "01"):
                        requisicao = "051!"
                        requisicao += montarRequisicao(1, "Nova Quantidade")
                        print(requisicao)
                        cli.enviarRequisicao(requisicao)
                        print(cli.recebeResposta())
                    elif(op2 == "02"):
                        requisicao = "052!"
                        requisicao += montarRequisicao(1, "Novo Preço")
                        cli.enviarRequisicao(requisicao)
                        print(cli.recebeResposta())
            else:
                print("Produto não cadastrado")

        
        elif(op == "06" or op == "07"):
            requisicao = "06!"
            alterarPess = input("Digite o nome do usuário que deseja remover: ")
            requisicao += alterarPess
            cli.enviarRequisicao(requisicao)
            print(cli.recebeResposta())

        elif(op == "08"):
            requisicao = "08!"
            alterarProd = input("Digite o id do produto que deseja remover: ")
            requisicao += alterarProd
            cli.enviarRequisicao(requisicao)
            print(cli.recebeResposta())

        elif(op == "09" or op == "10"): #mostrar funcionarios
            if op == "09":
                requisicao = "09!0"
            elif op == "10":
                requisicao = "09!1"
            cli.enviarRequisicao(requisicao)
            while True:
                receber = cli.recebeResposta()
                if receber == "acabou":
                    break
                print (receber)
            input("Para voltar aperte o ENTER")
                   
        elif(op == "11"):
            requisicao = "11!"
            cli.enviarRequisicao(requisicao)
            while True:
                receber = cli.recebeResposta()
                if receber == "acabou":
                    break
                print(receber)
            input("Para voltar aperte o ENTER")
        
        else:
            print("Oção inválida")
        
    cli.fechaConexao()