# task13.py

import base64
from random import randint
from task9 import pad_bytes_size
from task11 import random_AES_key
from task12 import encrypt_ecb
from Crypto.Cipher import AES

secret_key = random_AES_key()


def decode_profile(profile_str):
    return {x.split(b'=')[0]: x.split(b'=')[1] for x in profile_str.split(b'&')}


def profile_for(user_email):
    excluded = b'&='
    if any([(c in user_email) for c in excluded]):
        return None
    return b'email=' + user_email + b'&uid=10&role=user'


def encrypt_profile(user_email, secret_key):
    profile = profile_for(user_email)
    ctext = encrypt_ecb(profile, secret_key)
    return ctext


def strip_padding(raw_message, block_size=16):
    pad_byte = raw_message[-1]
    padding_size = int(pad_byte)
    if padding_size == 0 or \
        padding_size > block_size or \
        len(raw_message) < padding_size or \
       (len(raw_message) % block_size) != 0:
            return raw_message
    if all((x == pad_byte) for x in raw_message[-padding_size:]):
        return raw_message[:-padding_size]
    return raw_message


def decrypt_ecb(ciphertext, aes_key):
    cipher = AES.new(aes_key, AES.MODE_ECB)
    plaintext = bytearray()
    for x in range(0, len(ciphertext), 16):
        plaintext += cipher.decrypt(ciphertext[x:x + 16])
    plaintext = strip_padding(plaintext)
    return plaintext


def decrypt_profile(ctext, secret_key):
    plaintext = decrypt_ecb(bytes(ctext), secret_key)
    return decode_profile(bytes(plaintext))


if __name__ == '__main__':

    # ATTACK!
    target_block = pad_bytes_size(b'admin')
    admin_ciphertext = encrypt_profile(b'0000000000' + target_block, secret_key)
    attack_account = b'attack@me.com'
    attack_user_ciphertext = encrypt_profile(attack_account, secret_key)
    cooked_ciphertext = attack_user_ciphertext[:32] + admin_ciphertext[16:32]
    print(decrypt_profile(cooked_ciphertext, secret_key))
