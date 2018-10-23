import socket
import FuncsComuns as fc
from classClient import Cliente

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
    #conseguiLogar
    print("Bem vindo ao sistema de funcionários!")
    while True:
        print("00 - Sair \n01 - Cadastrar funcionário \n02 - Cadastrar produto \n03 - Cadastrar cliente\n")
        #print("04 - Alterar senha \n")
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
            print(requisicao)
            cli.enviarRequisicao(requisicao)
            print(cli.recebeResposta())

        elif(op == "02"):
            print("Opção ainda em desenvolvimento")
        
        elif(op == "03"):
            requisicao = "03!"
            requisicao += montarRequisicao(4, "nome:contato:login:senha")
            requisicao = requisicao + ":1"
            print(requisicao)
            cli.enviarRequisicao(requisicao)
            print(cli.recebeResposta())
        
        else:
            print("Oção inválida")
    cli.fechaConexao()
    
    
    
    # while True:        
    #     #menu de funções 
    #     op = input("Operação: ")
    #     #recebe uma tupla (quantidade, paramentros, mensagem)
        #printo mensagem
        #split nos paramentros
        #primeiro info
        # msg = input(parametros[0])
        # i = 1
        # while i < quantidade:
        #     info = input(paramentros[i] + ":")
        #     dados = ":" + info
            

# adicionar Func
# (4,"nome:contato:login:senha","Digite as informações do novo funcionario")



    