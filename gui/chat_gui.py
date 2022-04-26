from tkinter import *
from tkinter import font
from tkinter import ttk

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
                              bg = "#17202A")
        self.headLabel = Label(self.rootWindow,
                             bg = "#17202A",
                              fg = "#EAECEE",
                              text = self.username ,
                               font = "Helvetica 13 bold",
                               pady = 5)
         
        self.headLabel.place(relwidth = 1)
        self.line = Label(self.rootWindow,
                          width = 450,
                          bg = "#ABB2B9")
         
        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)
         
        self.textCons = Text(self.rootWindow,
                             width = 20,
                             height = 2,
                             bg = "#17202A",
                             fg = "#EAECEE",
                             font = "Helvetica 14",
                             padx = 5,
                             pady = 5)
         
        self.textCons.place(relheight = 0.745,
                            relwidth = 1,
                            rely = 0.08)
         
        self.bottomLabel = Label(self.rootWindow,
                                 bg = "#ABB2B9",
                                 height = 80)
         
        self.bottomLabel.place(relwidth = 1,
                               rely = 0.825)
         
        self.messageEntry = Entry(self.bottomLabel,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
         
        # place the given widget
        # into the gui window
        self.messageEntry.place(relwidth = 0.74,
                            relheight = 0.06,
                            rely = 0.008,
                            relx = 0.011)
         
        self.messageEntry.focus()
         
        # create a Send Button
        self.sendButton = Button(self.bottomLabel,
                                text = "Send",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButtonOnClick(self.messageEntry.get()))
         
        self.sendButton.place(relx = 0.77,
                             rely = 0.008,
                             relheight = 0.06,
                             relwidth = 0.22)
         
        self.textCons.config(cursor = "arrow")
         
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
        
        scrollbar.place(relheight = 1,
                        relx = 0.974)
         
        scrollbar.config(command = self.textCons.yview)
         
        self.textCons.config(state = DISABLED)


    # function to basically start the thread for sending messages
    def sendButtonOnClick(self, msg):
        # TODO @Marcel.Bieniek
        return 1
