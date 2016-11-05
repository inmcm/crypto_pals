''' Task10.py '''
import base64
from operator import xor
from Crypto.Cipher import AES


class MyCBC(object):
    """
    CBC Block Mode
    """
    def __init__(self, init_vector, my_key):
        self.iv = init_vector
        self.cbc_cipher = AES.new(my_key, AES.MODE_ECB)

    def encrypt(self, plaintext):
        """
        Encrypt input byes with CBC mode
        """
        obfuscated_text = bytes(map(xor, plaintext, self.iv))
        ciphertext = self.cbc_cipher.encrypt(obfuscated_text)
        self.iv = ciphertext
        return ciphertext

    def decrypt(self, ciphertext):
        """
        Decrypt input byes with CBC mode
        """
        obfuscated_text = self.cbc_cipher.decrypt(ciphertext)
        plaintext = bytes(map(xor, obfuscated_text, self.iv))
        self.iv = ciphertext
        return plaintext

if __name__ == '__main__':

    with open('10.txt', 'rb') as b64_input:
        ctext = base64.b64decode(b64_input.read())

    key = b'YELLOW SUBMARINE'
    iv = bytes([0 for _ in range(16)])
    cipher = MyCBC(iv, key)

    for x in range(0, len(ctext), 16):
        plain = cipher.decrypt(ctext[x:x+16])
        print(plain)
