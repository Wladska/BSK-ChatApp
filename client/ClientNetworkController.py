import socket
import threading
from tkinter import *
from styles.styles import *

SERVER = "192.168.1.100"
PORT = 9090


class ClientNetworkController:
    def __init__(self, clientName):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")

        self.clientName = clientName
        self.serverAddr = SERVER
        self.serverPort = PORT
        self.view = None
        self.running = True

        self.s.connect((self.serverAddr, self.serverPort))
        print(f"Connected to server {self.serverAddr}:{self.serverPort}")

    def startCommunication(self):
        # function to basically start the thread for sending messages
        self.thread = threading.Thread(target=self.receiveMessages, args=())
        self.thread.start()

    def stopCommunication(self):
        # send close connection command to server (for that client)
        self.s.send("!CLOSE".encode())

        # close connection
        self.running = False
        self.s.close()
        print("Disconnecting...")
        self.view.rootWindow.destroy()

    def receiveMessages(self):
        if self.view is None:
            print("Chat view isn't assigned!")
            return

        while self.running:
            try:
                message = self.s.recv(1024).decode()

                self.view.displayMessage(message)
                # print(message)
            except:
                # an error will be printed on the command line or console if there's an error
                # print("An error occured!")
                # self.s.close()
                # self.stopCommunication()
                break

    def sendMessage(self, msg):
        if self.view is None:
            print("Chat view isn't assigned!")
            return
        
        while True:
            message = f"{self.clientName}: {msg}"
            self.s.send(message.encode())
            break
    
    def addView(self, view):
        self.view = view
