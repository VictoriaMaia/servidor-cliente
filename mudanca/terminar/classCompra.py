from classProduto import Produto

class Compra():
    def __init__(self):
        self.listaprodutos = []
        self.total = 0
    
    def inserirProduto(self, produto):
        self.listaprodutos.append(produto)
        self.total = self.total + produto.preco

    # def removerProduto(self, produto):
    #     self.listaprodutos.

    #def finalizarCompra():

