from tkinter import *
from client.Client import *


def main():
    pass


if __name__ == '__main__':
    # mainWindow = Tk()
    # LoginWidget(mainWindow)
    # mainWindow.mainloop()
    mainWindow = Tk()
    client = Client(mainWindow)
    client.start()
    mainWindow.mainloop()
    # main()
