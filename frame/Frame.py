from frame.FrameType import *
import pickle


class Frame:
    def __init__(self, frameType: FrameType, data, user="", fileName=""):
        self.type = frameType
        self.data = data
        self.user = user
        self.fileName = fileName

    def serialize(self):
        return pickle.dumps(self)
