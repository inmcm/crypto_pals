''' Task11.py '''

from random import randint
from task9 import pad_bytes_size
from task10 import MyCBC
from Crypto.Cipher import AES

def random_AES_key():
    return bytes([randint(0, 255) for _ in range(16)])

def encryption_oracle(plaintext):

    new_key = random_AES_key()
    new_iv = bytes([randint(0, 255) for _ in range(16)])

    header = bytes([randint(0, 255)]) * randint(5, 10)
    trailer = bytes([randint(0, 255)]) * randint(5, 10)
    complete_payload = pad_bytes_size(header + plaintext + trailer, 16)

    if randint(0, 1):
        print('Encrypting CBC!')
        cipher = MyCBC(bytes([randint(0, 255) for _ in range(16)]), new_key)
    else:
        print('Encrypting ECB!')
        cipher = AES.new(new_key, AES.MODE_ECB)

    ciphertext = bytearray()
    for x in range(0, len(complete_payload), 16):
        ciphertext += cipher.encrypt(complete_payload[x:x+16])

    return ciphertext
    

if __name__ == '__main__':

    print(random_AES_key())

    ptext = b'X' * 256

    print(encryption_oracle(ptext))

