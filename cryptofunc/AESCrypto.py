from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(data, secretKey, mode="CBC"):
    if isinstance(data, str):
        data = bytes(data, encoding='utf-8')

    if mode == "CBC":
        key = secretKey[0:16]
        iv = secretKey[16:32]
        cipher = AES.new(bytes(key), AES.MODE_CBC, bytes(iv))
    else:
        cipher = AES.new(bytes(secretKey), AES.MODE_ECB)

    # try:
    #     encrypted = cipher.encrypt(pad(data, AES.block_size))
    # except TypeError:
    #     data = bytes(data, encoding='utf-8')
    encrypted = cipher.encrypt(pad(data, AES.block_size))
    # encrypted = cipher.encrypt(data)
    # print(f"encrypted: {encrypted}")

    return encrypted


def decrypt(data, secretKey, mode="CBC"):
    if mode == "CBC":
        key = secretKey[0:16]
        iv = secretKey[16:32]
        cipher = AES.new(bytes(key), AES.MODE_CBC, bytes(iv))
    else:
        cipher = AES.new(bytes(secretKey), AES.MODE_ECB)

    # try:
    #     decrypted = unpad(cipher.decrypt(data), AES.block_size)
    # except ValueError:
    #     decrypted = unpad(cipher.decrypt(data), AES.block_size)
    #     print("Wrong key!")

    decrypted = unpad(cipher.decrypt(data), AES.block_size)

    return decrypted
