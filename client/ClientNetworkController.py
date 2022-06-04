import socket
import threading
from styles.styles import *
import tqdm
import os

SERVER = "172.18.176.1" # "192.168.178.25"
PORT = 9090
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 # send 1024 bytes each time step


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
        # function to basically start the thread for receiving messages
        self.receivingThread = threading.Thread(target=self.receiveMessages, args=())
        self.receivingThread.start()

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
                    filename, filesize, user = message.split(SEPARATOR)
                    filename = os.path.basename(filename)
                    filesize = int(filesize)
                    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=BUFFER_SIZE)
                    uploadDir = "downloads\\" + self.clientName
                    if not os.path.exists(uploadDir):
                        os.makedirs(uploadDir)
                    with open(uploadDir + "\\" + filename, "wb") as f:
                        while True:
                            bytes_read = self.s.recv(BUFFER_SIZE)
                            f.write(bytes_read)
                            progress.update(len(bytes_read))
                            filesize = filesize - len(bytes_read)
                            if filesize <= 0:
                                break
                    message = user + ": Transferred " + filename
                self.view.displayMessage(message)
            except:
                print("An error occured!")
                self.s.close()
                self.stopCommunication()
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
        self.s.send(f"{path}{SEPARATOR}{filesize}{SEPARATOR}{self.clientName}".encode())
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
