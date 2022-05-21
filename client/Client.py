from tkinter import *
from client.ClientNetworkController import ClientNetworkController
from client.ClientChatView import ClientChatView
from client.ClientLoginView import ClientLoginView


class Client:
    def __init__(self, window):
        self.window = window

        self.name = ""
        self.password = ""
    
    def start(self):
        self.displayLoginGUI()

    def displayLoginGUI(self):
        ClientLoginView(self)
    
    def startMainApp(self, name, password):
        self.name = name
        self.password = password

        self.controller = ClientNetworkController(self.name)
        self.chatView = ClientChatView(self.window, self.name, self.controller)

        self.controller.addView(self.chatView)
        # self.chatView.addController(self.controller)

        self.controller.startCommunication()
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def setPassword(self, password):
        self.password = password
    
    def getWindow(self):
        return self.window
