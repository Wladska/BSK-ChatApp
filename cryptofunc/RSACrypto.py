from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import hashlib
import cryptofunc.AESCrypto as AESCrypto


def generateKeyPair():
    key = RSA.generate(2048)

    private = key.export_key()
    public = key.public_key().export_key()

    # print(private)
    # print(public)

    return private, public


def generateHash(password):
    return hashlib.blake2s(bytes(password, "utf-8"), digest_size=32).digest()


# encrypts and saves key to file
def saveKey(key, hashed, path):
    aesKey = hashed[0:16]
    aesIV = hashed[16:32]

    encrypted = AESCrypto.encrypt(key, aesKey, aesIV)

    with open(path+"key", "w+b") as f:
        f.write(encrypted)


# decrypts the key and returns it
def getKey(hashed, path):
    aesKey = hashed[0:16]
    aesIV = hashed[16:32]

    with open(path+"key", "r+b") as f:
        data = f.read()
        return AESCrypto.decrypt(data, aesKey, aesIV)


def encrypt(data, key):
    rsaKey = RSA.import_key(key)
    cipher = PKCS1_OAEP.new(rsaKey)
    encrypted = cipher.encrypt(data)

    return encrypted


def decrypt(data, key):
    rsaKey = RSA.import_key(key)
    cipher = PKCS1_OAEP.new(rsaKey)
    decrypted = cipher.decrypt(data)

    return decrypted
