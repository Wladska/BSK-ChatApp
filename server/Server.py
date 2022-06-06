import socket
import threading

BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"

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
        connected = True

        while connected:
            # receive message
            message = conn.recv(BUFFER_SIZE)
            packets = []
            if message.decode() == "!CLOSE":
                # close the connection
                conn.close()
                self.clients.remove((conn, addr))
                connected = False
                print(f"Client {addr} disconnected!")
                break
            if SEPARATOR in message.decode():
                filename, filesize, user = message.decode().split(SEPARATOR)
                filesize = int(filesize)
                while True:
                    bytes_read = conn.recv(BUFFER_SIZE)
                    packets.append(bytes_read)
                    filesize = filesize - len(bytes_read)
                    if filesize <= 0:
                        break
            # broadcast message
            self.broadcastMessage(message)
            for packet in packets:
                self.broadcastMessage(packet)

    def broadcastMessage(self, message):
        for client in self.clients:
            client[0].send(message)
            # print(f"sending message to client {client[1]}")

def startServer(addr, port):
    server = Server(addr, port)
