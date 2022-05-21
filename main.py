from tkinter import *
from client.Client import *


if __name__ == '__main__':
    mainWindow = Tk()
    client = Client(mainWindow)
    client.start()
    mainWindow.mainloop()
