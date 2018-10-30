import socket

class Cliente():
    def __init__(self):
        self.HOST = ''
        self.PORT = 5000
        self.addrComunic = (self.HOST, self.PORT)
        self.socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketClient.connect(self.addrComunic)

    def enviarRequisicao(self, msg):
        self.socketClient.send(msg.encode())

    def recebeResposta(self):
        return self.socketClient.recv(2048).decode()

    def fechaConexao(self):
        self.socketClient.close()