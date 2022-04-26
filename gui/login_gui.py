from gui.chat_gui import *

class LoginWidget:

    def __init__(self, window):
        window.withdraw()
        
        self.loginWindow = Toplevel()
        self.loginWindow.title("Login")
        self.loginWindow.resizable(width = False,
                             height = False)
        self.loginWindow.configure(width = 400,
                             height = 300)
        
        self.description = Label(self.loginWindow,
                       text = "Please login to continue",
                       justify = CENTER,
                       font = "Helvetica 14 bold")
         
        self.description.place(relheight = 0.15,
                       relx = 0.2,
                       rely = 0.07)
        
        self.usernameLabel = Label(self.loginWindow,
                               text = "Name: ",
                               font = "Helvetica 12")
         
        self.usernameLabel.place(relheight = 0.2,
                             relx = 0.1,
                             rely = 0.2)
        
        self.usernameField = Entry(self.loginWindow,
                             font = "Helvetica 14")
         
        self.usernameField.place(relwidth = 0.4,
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.2)
        
        self.usernameField.focus()
         
        self.loginButton = Button(self.loginWindow,
                         text = "Login",
                         font = "Helvetica 14 bold",
                         command = lambda: self.validateUserInput(self.usernameField.get(),window))
         
        self.loginButton.place(relx = 0.4,
                      rely = 0.55)

    def validateUserInput(self, name, window):
        #add some user validation idk
        self.loginWindow.destroy()
        ChatGUI(window, name)