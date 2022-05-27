from tkinter import *
from client.Client import *


if __name__ == '__main__':
    rootWindow = Tk()

    client = Client(rootWindow)
    client.start()
    
    rootWindow.mainloop()
