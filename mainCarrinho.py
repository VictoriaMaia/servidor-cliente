import time
import socket
import os
from classClient import Cliente
import tecladoArq as teclado

cli = Cliente()

def TelaLogin():
    while True:
        print("Login: ")
        login = "774"
        # login = teclado.lerTeclado()
        # time.sleep(1)
        print("Senha: ")
        senha = "774"
        # senha = teclado.lerTeclado()
        
        dados = str(login) + ":" + str(senha) + ":" + "1"
        print(dados)
        cli.enviarRequisicao(dados)
        data = cli.recebeResposta() 
        if data == ".":            
            return
        else:
            print(data)
            time.sleep(1)


def caixinhaPreta():
    #loop do codigo do JP que identifica o produto
    #fazer funcoes para ele usar
    sair = 0
    while True:        
        # time.sleep(2)
        # os.system("clear")
        produtoLido = input("Produto: ")
        if produtoLido == "sair":
            #se RFID disser saiu ; sair = 1
            sair = 1
        if sair == 1:
            cli.enviarRequisicao("sair")
            return
        idProduto = int(produtoLido)
        if idProduto > 0 and idProduto < 20: #valores fixos que JP tem que decidir
            cli.enviarRequisicao(produtoLido)
            print(cli.recebeResposta())
        else:
            print("Leitura incorreta, por favor coloque novamente o produto!")




if __name__ == "__main__":
    # teclado.iniciar()
    #tela inicial, conseguiu conectar
    print(cli.recebeResposta())
    TelaLogin()
    print("consegui logar")
    print(cli.recebeResposta())
    #conseguiLogar
    caixinhaPreta()
    print("Obrigada por comprar aqui!! Au revoir")
    cli.fechaConexao()
    