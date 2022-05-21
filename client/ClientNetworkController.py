import socket
from gui.styles import *
from tkinter import *
from fileupload.fileuploader import *
import threading

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

        self.s.connect((self.serverAddr, self.serverPort))
        print(f"Connected to server {self.serverAddr}:{self.serverPort}")

    def startCommunication(self):
        # function to basically start the thread for sending messages
        thread = threading.Thread(target=self.receiveMessages, args=())
        thread.start()

    def receiveMessages(self):
        if self.view is None:
            print("Chat view isn't assigned!")
            return
        
        while True:
            try:
                message = self.s.recv(1024).decode()

                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    self.s.send(self.clientName.encode())
                else:
                    self.view.displayMessage(message)
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                self.s.close()
                break

    def sendMessage(self, msg):
        if self.view is None:
            print("Chat view isn't assigned!")
            return
        
        self.view.textCons.config(state=DISABLED)
        while True:
            message = f"{self.clientName}: {msg}"
            self.s.send(message.encode())
            break
    
    def addView(self, view):
        self.view = view
