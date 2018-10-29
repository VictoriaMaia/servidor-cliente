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
        return ("nome: " + self.nome + "; Contato: " + self.contato + "; Login: " + self.login + "; Senha: " + self.senha)

    def setLogin(self, newLogin):
        self.login = newLogin

    def setSenha(self, newSenha):
        self.senha = newSenha
    
    def setContato(self, newContato):
        self.contato = newContato