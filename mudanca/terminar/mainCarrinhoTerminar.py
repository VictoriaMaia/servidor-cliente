import socket
import FuncsComuns as fc
from classCompra import Compra
from classClient import Cliente

if __name__ == "__main__":
    cli = Cliente()
    compra = Compra()
    #tela inicial, conseguiu conectar
    print(cli.recebeResposta())
    fc.TelaLogin(cli)
    print("Começar a compra!")
    sair = 0
    while sair == 0:
        produtoAnalisado = input() #numero identificador
        #mando para o servidor identificar o produto, retorna o objeto produto
        #se tag = 0 (entrar) chamada a função adicionar produto
        #se tag = 1 (sair) chamada a função remover produto
        #como vou saber que esta saindo do carrinho
        #quando sair do supermercado, sair = 1

    #manda o objeto compra para o servidor
    #o servidor trata a compra modificando as quantidades dos produtos e mandando um e-mail com a nota fiscal

    cli.fechaConexao()

    #o cariinho vai ter uma lista de ids de produtos, quando sair ele manda a lista para o servidor que identifica osp rdutos pelos ids e soma, altera o estoque e manda o total nota fiscal
    #FAIXA DE VALORES PARA PRODUTOS, SE TIVER FORA DESSA FAIXA NOTIFICAR "ERRO DE LEITRUA, TENTE NOVAMENTE"