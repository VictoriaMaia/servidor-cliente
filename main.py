from threading import Thread
from sistemaSupermercado import Sistema

if __name__ == "__main__":
    sys = Sistema()
    while True:
        sockClient = sys.S.conectar()
        Thread(target=sys.GerenciaLogin, args=(sockClient,)).start()
    