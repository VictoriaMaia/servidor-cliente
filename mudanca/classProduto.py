class Produto():
    def __init__(self, ident, nome, quantidade, preco):
        self.id = ident
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def setQuantidade(self, quant):
        if quant < 0:
            self.quantidade = 0
        else:
            self.quantidade = quant

    def setPreco(self, preco):
        self.preco = preco

    def toString(self):
        return ("Id: " + self.id + " ;Nome: " + self.nome + " ;Quant: " + str(self.quantidade) + " ;Preço: " + self.preco + "\n")
    
    def toStringCompra(self):
        return ("Id: " + self.id + " ;Nome: " + self.nome + " ;Preço: " + self.preco + "\n")
