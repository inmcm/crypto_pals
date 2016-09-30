import string
from binascii import unhexlify

freqs = {'a': 6.51738, 'b': 1.24248, 'c': 2.17339, 'd': 3.49835, 'e': 0.41442,
         'f': 1.97881, 'g': 1.58610, 'h': 4.92888, 'i': 5.58094, 'j': 0.09033, 
         'k': 0.50529, 'l': 3.31490, 'm': 2.02124, 'n': 5.64513, 'o': 5.96302, 
         'p': 1.37645, 'q': 0.08606, 'r': 4.97563, 's': 5.15760, 't': 7.29357,
         'u': 2.25134, 'v': 0.82903, 'w': 1.71272, 'x': 0.13692, 'y': 1.45984,
         'z': 0.07836, ' ': 19.18182}

test = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
sample_bytes = unhexlify(test)
best = (0,0,0)
for xor_key in range(256):
    test_bytes = bytes([xor_key ^ c for c in sample_bytes])
    total_chars = sum([test_bytes.count(x) for x in string.printable.encode()])
    if total_chars == len(test_bytes):
        test_string = test_bytes.decode()
        score = sum([freqs[x] for x in test_string if x in freqs])
        if score > best[1]:
            best = (xor_key, score, test_string)

    
print("Best XOR Key:", hex(best[0]))
print("Score:",best[1])
print("Decoded String:",best[2])
