from email import message
from http import server
import socket
import threading

class Client:
    def __init__(self, serverAddr, serverPort, clientName):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")

        self.clientName = clientName
        self.serverAddr = serverAddr
        self.serverPort = serverPort

        self.s.connect((self.serverAddr, self.serverPort))
        print(f"Connected to server {self.serverAddr}:{self.serverPort}")

        #self.s.send(clientName.encode())

        #self.receiveMessage()

    def receiveMessage(self):
        message = self.s.recv(1024).decode()
        print (f"message from server: {message}")
        self.s.send("No problem".encode())

        self.s.close()

def startClient(serverAddr, serverPort, username):
    client = Client(serverAddr, serverPort, username)