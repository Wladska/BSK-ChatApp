from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(data, key, iv, mode="CBC"):
    if mode == "ECB":
        secretKey = b'' + key + iv
        cipher = AES.new(bytes(secretKey), AES.MODE_ECB)
    else:
        cipher = AES.new(bytes(key), AES.MODE_CBC, bytes(iv))

    encrypted = cipher.encrypt(pad(data, AES.block_size))

    print(f"encrypted: {encrypted}")

    return encrypted


def decrypt(data, key, iv, mode="CBC"):
    if mode == "ECB":
        secretKey = b'' + key + iv
        cipher = AES.new(bytes(secretKey), AES.MODE_ECB)
    else:
        cipher = AES.new(bytes(key), AES.MODE_CBC, bytes(iv))

    try:
        decrypted = unpad(cipher.decrypt(data), AES.block_size)
    except ValueError:
        decrypted = cipher.decrypt(data)
        print("Wrong key & iv!")

    print(f"decrypted: {decrypted}")

    return decrypted
