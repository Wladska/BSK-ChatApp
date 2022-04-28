import socket
from gui.styles import *
from tkinter import *
from fileupload.fileuploader import *
import threading


class Client:
    def __init__(self, serverAddr, serverPort, clientName, window):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")

        self.clientName = clientName
        self.serverAddr = serverAddr
        self.serverPort = serverPort

        self.s.connect((self.serverAddr, self.serverPort))
        print(f"Connected to server {self.serverAddr}:{self.serverPort}")

        self.rootWindow = window
        self.username = clientName

        self.rootWindow.deiconify()
        self.rootWindow.title("BSK-ChatApp")
        self.rootWindow.resizable(width=False,
                                  height=False)
        self.rootWindow.configure(width=470,
                                  height=550,
                                  bg=black)
        self.headLabel = Header1B(self.rootWindow, darkmode=True,
                                  text=self.username,
                                  pady=5)

        self.headLabel.place(relwidth=1)
        self.line = Label(self.rootWindow,
                          width=450,
                          bg=blue)

        self.line.place(relwidth=1,
                        rely=0.07,
                        relheight=0.012)

        self.textCons = MessageConsole(self.rootWindow,
                                       width=20,
                                       height=2,
                                       padx=5,
                                       pady=5)

        self.textCons.place(relheight=0.745,
                            relwidth=1,
                            rely=0.08)

        self.bottomLabel = Label(self.rootWindow,
                                 bg=blue,
                                 height=80)

        self.bottomLabel.place(relwidth=1,
                               rely=0.825)

        self.messageEntry = MultiLineTextFiled(self.bottomLabel)

        # place the given widget
        # into the gui window
        self.messageEntry.place(relwidth=0.74,
                                relheight=0.06,
                                rely=0.008,
                                relx=0.011)

        self.messageEntry.focus()

        # Send Button
        self.sendButton = CustomButton(self.bottomLabel,
                                       text="Send",
                                       width=20,
                                       command=lambda: self.sendMessage(self.messageEntry.get()))

        self.sendButton.place(relx=0.77,
                              rely=0.008,
                              relheight=0.03,
                              relwidth=0.22)
        # Add file Button
        self.addFileButton = CustomButton(self.bottomLabel,
                                          text="Add file",
                                          width=20,
                                          command=lambda: self.addFileButtonOnClick())

        self.addFileButton.place(relx=0.77,
                                 rely=0.040,
                                 relheight=0.03,
                                 relwidth=0.22)

        self.textCons.config(cursor="arrow")

        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)

        scrollbar.place(relheight=1,
                        relx=0.974)

        scrollbar.config(command=self.textCons.yview)

        self.textCons.config(state=DISABLED)

        # function to basically start the thread for sending messages
        thread = threading.Thread(target=self.receiveMessages, args=())
        thread.start()

    def addFileButtonOnClick(self):
        FileUploader()

        # function to basically start the thread for sending messages

    # def sendButtonOnClick(self, msg):
    #     return 1

    def receiveMessages(self):
        while True:
            try:
                message = self.s.recv(1024).decode()

                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    self.s.send(self.clientName.encode())
                else:
                    # insert messages to text box
                    self.textCons.config(state=NORMAL)
                    self.textCons.insert(END,
                                         message + "\n\n")

                    self.textCons.config(state=DISABLED)
                    self.textCons.see(END)
            except:
                # an error will be printed on the command line or console if there's an error
                print("An error occured!")
                self.s.close()
                break

    def sendMessage(self, msg):
        self.textCons.config(state=DISABLED)
        while True:
            message = f"{self.clientName}: {msg}"
            self.s.send(message.encode())
            break

def startClient(serverAddr, serverPort, username, window):
    client = Client(serverAddr, serverPort, username, window)
