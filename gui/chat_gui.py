from tkinter import *
from tkinter import font
from tkinter import ttk
from gui.styles import *
from fileupload.fileuploader import *

class ChatGUI:

    def __init__(self, window, username):
        self.rootWindow = window
        self.username = username
        
        self.rootWindow.deiconify()
        self.rootWindow.title("BSK-ChatApp")
        self.rootWindow.resizable(width = False,
                              height = False)
        self.rootWindow.configure(width = 470,
                              height = 550,
                              bg = black)
        self.headLabel = Header1B(self.rootWindow, darkmode = True,
                                text = self.username ,
                                pady = 5)
         
        self.headLabel.place(relwidth = 1)
        self.line = Label(self.rootWindow,
                          width = 450,
                          bg = blue)
         
        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)
         
        self.textCons = MessageConsole(self.rootWindow,
                             width = 20,
                             height = 2,
                             padx = 5,
                             pady = 5)
         
        self.textCons.place(relheight = 0.745,
                            relwidth = 1,
                            rely = 0.08)
         
        self.bottomLabel = Label(self.rootWindow,
                                 bg = blue,
                                 height = 80)
         
        self.bottomLabel.place(relwidth = 1,
                               rely = 0.825)
         
        self.messageEntry = MultiLineTextFiled(self.bottomLabel)
         
        # place the given widget
        # into the gui window
        self.messageEntry.place(relwidth = 0.74,
                            relheight = 0.06,
                            rely = 0.008,
                            relx = 0.011)
         
        self.messageEntry.focus()
         
        # Send Button
        self.sendButton = CustomButton(self.bottomLabel,
                                text = "Send",
                                width = 20,
                                command = lambda : self.sendButtonOnClick(self.messageEntry.get()))
         
        self.sendButton.place(relx = 0.77,
                             rely = 0.008,
                             relheight = 0.03,
                             relwidth = 0.22)
        # Add file Button
        self.addFileButton = CustomButton(self.bottomLabel,
                                text = "Add file",
                                width = 20,
                                command = lambda : self.addFileButtonOnClick())
         
        self.addFileButton.place(relx = 0.77,
                             rely = 0.040,
                             relheight = 0.03,
                             relwidth = 0.22)
         
        self.textCons.config(cursor = "arrow")
         
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
        
        scrollbar.place(relheight = 1,
                        relx = 0.974)
         
        scrollbar.config(command = self.textCons.yview)
         
        self.textCons.config(state = DISABLED)

    # function to basically start the thread for sending messages
    def addFileButtonOnClick(self):
        FileUploader()

    # function to basically start the thread for sending messages
    def sendButtonOnClick(self, msg):
        # TODO @Marcel.Bieniek
        return 1
