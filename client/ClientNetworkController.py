import socket
import threading
from styles.styles import *
from tkinter import ttk
import tqdm
import os
from frame.Frame import *
import struct

SERVER = "172.18.176.1" # "192.168.178.25"
PORT = 9090


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
        self.sendFrame(Frame(FrameType.CLOSE, ""))

        # close connection
        self.running = False
        self.s.close()
        print("Disconnecting...")
        self.view.rootWindow.destroy()

    def receiveMessages(self):
        if self.view is None:
            print("Chat view isn't assigned!")
            return

        default_size = len(Frame(FrameType.SIZE, struct.pack('I', 420)).serialize())
        size = default_size

        while self.running:
            try:
                message = self.s.recv(size)
                recvFrame = pickle.loads(message)
                size = default_size

                if recvFrame.type == FrameType.SIZE:
                    size = struct.unpack('I', recvFrame.data)
                    size = size[0]
                elif recvFrame.type == FrameType.ACK:
                    self.view.displayAcknowledgement(recvFrame.user)
                elif recvFrame.type == FrameType.FILE_END:
                    self.view.displayMessage(f"{recvFrame.user}:Sent {recvFrame.fileName}")
                    self.sendAcknowledgement()
                elif recvFrame.type == FrameType.MSG:
                    self.view.displayMessage(f"{recvFrame.user}:{recvFrame.data}")
                    self.sendAcknowledgement()
                elif recvFrame.type == FrameType.FILE:
                    uploadDir = "downloads\\" + self.clientName
                    if not os.path.exists(uploadDir):
                        os.makedirs(uploadDir)
                    with open(uploadDir + "\\" + recvFrame.fileName, "a+b") as f:
                        f.write(recvFrame.data)
            except:
                print("An error occured!")
                self.s.close()
                self.stopCommunication()
                break

    def sendMessage(self, msg):
        if self.view is None:
            print("Chat view isn't assigned!")
            return

        self.sendFrame(Frame(FrameType.MSG, msg, self.clientName))

    def sendAcknowledgement(self):
        if self.view is None:
            print("Chat view isn't assigned!")
            return

        self.sendFrame(Frame(FrameType.ACK, self.clientName, self.clientName))

    def sendFile(self, path):
        if self.view is None:
            print("Chat view isn't assigned!")
            return
        filesize = os.path.getsize(path)
        self.sendFrame(Frame(FrameType.FILE, b"", self.clientName, os.path.basename(path)))
        # start sending the file
        progress = tqdm.tqdm(range(filesize), f"Sending {os.path.basename(path)}", unit="B", unit_scale=True, unit_divisor=BUFFER_SIZE)
        progressBarPopup = Toplevel()
        progressBarPopup.geometry('50x80')
        Label(progressBarPopup, text="Files are being sent").grid(row=0, column=0)
        barProgress = 0
        progress_var = DoubleVar()
        progress_bar = ttk.Progressbar(progressBarPopup, variable=progress_var, maximum=int(filesize))
        progress_bar.grid(row=1, column=0)
        progressBarPopup.pack_slaves()
        with open(path, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break

                self.sendFrame(Frame(FrameType.FILE, bytes_read, self.clientName, os.path.basename(path)))
                progress.update(len(bytes_read))
                progressBarPopup.update()
                barProgress += BUFFER_SIZE
                progress_var.set(barProgress)
        self.sendFrame(Frame(FrameType.FILE_END, b"", self.clientName, os.path.basename(path)))

    def sendFrame(self, frame):
        serialized = frame.serialize()
        sizeFrame = Frame(FrameType.SIZE, struct.pack('I', len(serialized)))
        self.s.sendall(sizeFrame.serialize())
        self.s.sendall(serialized)

    def addView(self, view):
        self.view = view
