from operator import xor
from binascii import unhexlify, hexlify
in_1 = '1c0111001f010100061a024b53535009181c'
in_2 = '686974207468652062756c6c277320657965'
out = '746865206b696420646f6e277420706c6179'


def xor_bytes(in_b1, in_b2):
    b1 = unhexlify(in_b1)
    b2 = unhexlify(in_b2)
    xord = bytearray(map(xor,b1,b2))
    return hexlify(xord).decode()

if __name__ == '__main__':
    f = xor_bytes(in_1, in_2)
    #ßassert f == out
    print(f)