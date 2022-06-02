import socket
import threading
from tkinter import *
from styles.styles import *
import tqdm
import os

SERVER = "192.168.178.25"
PORT = 9090
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step


class ClientNetworkController:
    def __init__(self, clientName):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")

        self.clientName = clientName
        self.serverAddr = SERVER
        self.serverPort = PORT
        self.view = None
        self.running = True

        self.s.connect((self.serverAddr, self.serverPort))
        print(f"Connected to server {self.serverAddr}:{self.serverPort}")

    def startCommunication(self):
        # function to basically start the thread for sending messages
        self.thread = threading.Thread(target=self.receiveMessages, args=())
        self.thread.start()

    def stopCommunication(self):
        # send close connection command to server (for that client)
        self.s.send("!CLOSE".encode())

        # close connection
        self.running = False
        self.s.close()
        print("Disconnecting...")
        self.view.rootWindow.destroy()

    def receiveMessages(self):
        if self.view is None:
            print("Chat view isn't assigned!")
            return

        while self.running:
            try:
                message = self.s.recv(BUFFER_SIZE).decode()
                if SEPARATOR in message: 
                    # receive the file infos
                    # receive using client socket, not server socket
                    filename, filesize = message.split(SEPARATOR)
                    # remove absolute path if there is
                    filename = os.path.basename(filename)
                    # convert to integer
                    filesize = int(filesize)
                    # start receiving the file from the socket
                    # and writing to the file stream
                    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=BUFFER_SIZE)
                    if not os.path.exists(self.clientName):
                        os.makedirs(self.clientName)
                    with open(self.clientName + "\\" + filename, "wb") as f:
                        while True:
                            # read bytes from the socket (receive)
                            bytes_read = self.s.recv(BUFFER_SIZE)
                            if not bytes_read:    
                                # nothing is received
                                # file transmitting is done
                                f.close()
                                break
                            # write to the file the bytes we just received
                            f.write(bytes_read)
                            # update the progress bar
                            progress.update(len(bytes_read))

                self.view.displayMessage(message)
                # print(message)
            except:
                # an error will be printed on the command line or console if there's an error
                # print("An error occured!")
                # self.s.close()
                # self.stopCommunication()
                break

    def sendMessage(self, msg):
        if self.view is None:
            print("Chat view isn't assigned!")
            return
        
        message = f"{self.clientName}: {msg}"
        self.s.send(message.encode())
    
    def sendFile(self, path):
        if self.view is None:
            print("Chat view isn't assigned!")
            return
        
        filesize = os.path.getsize(path)
        # send the filename and filesize
        self.s.send(f"{path}{SEPARATOR}{filesize}".encode())
        # start sending the file
        progress = tqdm.tqdm(range(filesize), f"Sending {path}", unit="B", unit_scale=True, unit_divisor=BUFFER_SIZE)
        with open(path, "rb") as f:
            while True:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                self.s.send(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
    
    def addView(self, view):
        self.view = view
