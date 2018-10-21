''' Task12.py '''

import base64
from random import randint
from task9 import pad_bytes_size
from task11 import ecb_cbc_detection, random_AES_key
from Crypto.Cipher import AES


secret_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
secret_string_decode = base64.b64decode(secret_string)
secret_string_len = len(secret_string_decode)
print("Length of secret string:", secret_string_len)
secret_key = random_AES_key()


my_test_string="Hello, I like cake"


def encrypt_ecb(plaintext, aes_key):
    complete_payload = pad_bytes_size(plaintext, 16)
    cipher = AES.new(aes_key, AES.MODE_ECB)
    ciphertext = bytearray()
    for x in range(0, len(complete_payload), 16):
        ciphertext += cipher.encrypt(complete_payload[x:x + 16])
    return ciphertext

def discover_block_size():
    test_key = random_AES_key()
    test_ptext = encrypt_ecb(b'A', test_key)
    return len(test_ptext)


def generate_block_last_block_dict(known_input, aes_key):
    results = []
    for x in range(256):
        payload = known_input + bytes([x])
        ctext = encrypt_ecb(payload, aes_key)
        results.append(ctext)
    return results


if __name__ == '__main__':
    print("AES BLOCK SIZE: ", discover_block_size())
    const_char = b'A'
    attack_str_size = 159
    recovered_secret = b''
    for _ in range(len(secret_string_decode)):
        attack_string = (const_char * (attack_str_size - len(recovered_secret))) + recovered_secret
        block_lookup = generate_block_last_block_dict(attack_string[-15:], secret_key)
        complete_ctext = encrypt_ecb(attack_string + secret_string_decode[len(recovered_secret):], secret_key)
        recovered_byte = bytes([block_lookup.index(complete_ctext[9 * 16:(9 * 16) + 16])])
        recovered_secret += recovered_byte
    print(recovered_secret)
