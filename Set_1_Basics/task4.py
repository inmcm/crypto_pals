import string
from binascii import unhexlify

freqs = {'a': 6.51738, 'b': 1.24248, 'c': 2.17339, 'd': 3.49835, 'e': 0.41442,
         'f': 1.97881, 'g': 1.58610, 'h': 4.92888, 'i': 5.58094, 'j': 0.09033, 
         'k': 0.50529, 'l': 3.31490, 'm': 2.02124, 'n': 5.64513, 'o': 5.96302, 
         'p': 1.37645, 'q': 0.08606, 'r': 4.97563, 's': 5.15760, 't': 7.29357,
         'u': 2.25134, 'v': 0.82903, 'w': 1.71272, 'x': 0.13692, 'y': 1.45984,
         'z': 0.07836, ' ': 19.18182}

best = (0,0,0)
with open('4.txt') as test_file:
    samples = test_file.read().splitlines()

for sample_string in samples:
    sample_bytes = unhexlify(sample_string)
    for xor_key in range(256):
        test_bytes = bytes([xor_key ^ c for c in sample_bytes])
        total_chars = sum([test_bytes.count(x) for x in string.printable.encode()])
        if total_chars == len(test_bytes):
            test_string = test_bytes.decode()
            score = sum([freqs[x] for x in test_string if x in freqs])
            if score > best[1]:
                best = (xor_key, score, test_string, sample_string)

    
print("Best XOR Key:", hex(best[0]))
print("Score:",best[1])
print("Encoded String:",best[3])
print("Decoded String:",best[2])
