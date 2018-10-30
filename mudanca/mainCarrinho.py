import time
import socket
import os
import FuncsComuns as fc
from classClient import Cliente

cli = Cliente()


def caixinhaPreta():
    #loop do código do JP que identifica o produto
    #fazer funções para ele usar
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
    #cli = Cliente()
    #tela inicial, conseguiu conectar
    print(cli.recebeResposta())
    fc.TelaLogin(cli)
    print(cli.recebeResposta())
    #conseguiLogar
    caixinhaPreta()
    print("Obrigada por comprar aqui!! Au revoir")
    cli.fechaConexao()
    