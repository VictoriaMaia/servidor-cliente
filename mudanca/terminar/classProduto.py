class Produto():
    def __init__(self, identificador, nome, quantidade, preco):
        self.id = identificador
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def setQuantidade(self, quant):
        self.quantidade = self.quantidade - quant

    #pode querer setar o preço

