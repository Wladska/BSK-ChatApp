from os import path, makedirs
import cryptofunc.RSACrypto as RSACrypto

KEYS_PATH = "keys\\"
PRIVATE_KEY_PATH = "\\private\\"
PUBLIC_KEY_PATH = "\\public\\"


class ClientKeyController:
    def __init__(self, name, password):
        self.name = name
        self.password = password

        self.keyPath = KEYS_PATH + name
        self.privateKeyPath = self.keyPath + PRIVATE_KEY_PATH
        self.publicKeyPath = self.keyPath + PUBLIC_KEY_PATH

    def getKeys(self):
        hashed = RSACrypto.generateHash(self.password)

        if not path.exists(self.keyPath):
            makedirs(self.privateKeyPath)
            makedirs(self.publicKeyPath)

            private, public = RSACrypto.generateKeyPair()

            RSACrypto.saveKey(private, hashed, self.privateKeyPath)
            RSACrypto.saveKey(public, hashed, self.publicKeyPath)

            return private, public
        else:
            private = RSACrypto.getKey(hashed, self.privateKeyPath)
            public = RSACrypto.getKey(hashed, self.publicKeyPath)

            return private, public
