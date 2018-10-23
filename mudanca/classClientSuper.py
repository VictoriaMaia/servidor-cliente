import socket

class ClienteSuper():
    def __init__(self, nome, contato, login, senha, tipo):
        self.nome = nome
        self.contato = contato
        self.login = login
        self.senha = senha
        #tipo 0-funcionario 1-comprador
        self.tipoCliente = tipo
        self.socketCliSuper = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.addrComunic = ('', 0)

    def toString(self):
        print(self.nome + " : " + self.contato + " : " + self.login + " : " + self.senha + " : " + self.tipoCliente)

