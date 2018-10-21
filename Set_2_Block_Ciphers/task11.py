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


def ecb_cbc_detection():
    ptext = b'X' * 256
    ctext = encryption_oracle(ptext)
    print("Ciphertext length:", len(ctext))
    blocks = [bytes(ctext[i:i + 15]) for i in range(0, len(ctext), 16)]
    for x, y in enumerate(blocks):
        print("Block: ", x, ":", y)
    if blocks[1] == blocks[2]:
        return 'ECB'
    else:
        return 'CBC'

if __name__ == '__main__':
    print(random_AES_key())
    for x in range(20):
        print(ecb_cbc_detection())
        print("")