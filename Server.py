import socket
import threading


class Server:
    def __init__(self, addr, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")

        self.s.bind((addr, port))
        print(f"socket bound to port {port}")

        self.s.listen()    
        print("socket is listening")

        self.clients = []
        self.isRunning = True

        self.connectClients()

    def connectClients(self):
        while self.isRunning:
            conn, addr = self.s.accept()
            thread = threading.Thread(target=self.handleClient, args=(conn, addr))
            thread.start()
            self.clients.append((conn, addr))
            print("New connection from ", addr)

    def handleClient(self, conn, addr):
        self.s.recv()
        print(f"client #{addr[1]}: ")
        pass
        # conn.close()


def startServer(addr, port):
    server = Server(addr, port)
