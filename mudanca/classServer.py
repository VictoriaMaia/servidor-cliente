import socket

class Server():
    def __init__(self):
        self.HOST = ''
        self.PORT = 5000
        self.serverAddr = (self.HOST, self.PORT)
        self.socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketServer.bind(self.serverAddr)
        self.socketServer.listen(5)

    def conectar(self):
        sock, addr = self.socketServer.accept()
        print("Cliente conectado")
        return sock
            
    def recebeRequisicao(self, Sk):
        return Sk.recv(2048).decode()

    def enviaRespostaRequisicao(self, Sk, resposta):
        Sk.send(resposta.encode())

    def fecharConecServer(self, Sk):
        Sk.close()






    

