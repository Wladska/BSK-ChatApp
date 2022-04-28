from gui.chat_gui import *
from gui.styles import *

class LoginWidget:

    def __init__(self, window):
        window.withdraw()
        
        self.loginWindow = Toplevel()
        self.loginWindow.title("Login")
        self.loginWindow.resizable(width = False, height = False)
        self.loginWindow.configure(width = 400, height = 300, background=dark_blue)
        
        self.description = Header1(self.loginWindow, darkmode=True,
                                    text = "Please login to continue",
                                    justify = CENTER)
         
        self.description.place(relheight = 0.15,
                       relx = 0.2,
                       rely = 0.07)
        #Username
        self.usernameLabel = Header2(self.loginWindow, darkmode=True, text = "Username: ", justify=LEFT)
        self.usernameLabel.place(relheight = 0.2,
                                    relx = 0.15,
                                    rely = 0.2)
        
        self.usernameField = TextField(self.loginWindow)
         
        self.usernameField.place(relwidth = 0.4,
                             relheight = 0.12,
                             relx = 0.4,
                             rely = 0.25)
        #Password
        self.pswdLabel = Header2(self.loginWindow, darkmode=True, text = "Password: ", justify=LEFT)
        self.pswdLabel.place(relheight = 0.2,
                                    relx = 0.15,
                                    rely = 0.35)
        
        self.pswdField = TextField(self.loginWindow)
         
        self.pswdField.place(relwidth = 0.4,
                             relheight = 0.12,
                             relx = 0.4,
                             rely = 0.4)
        
        self.usernameField.focus()
        self.pswdField.focus()

        # TODO password is currrently not passed to the function we may change that a bit later 
        self.loginWindow.bind('<Return>', (lambda event:self.validateUserInput(self.usernameField.get(),window)))
        self.loginButton = CustomButton(self.loginWindow,
                         text = "Login",
                         width = 25,
                         command = lambda: self.validateUserInput(self.usernameField.get(),window))
         
        self.loginButton.place(relx = 0.15, rely = 0.60)

    def validateUserInput(self, name, window):
        #add some user validation idk
        self.loginWindow.destroy()
        ChatGUI(window, name)