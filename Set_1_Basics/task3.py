import string
from binascii import unhexlify
letter_order = 'etaoinshrdlcumwfgypbvkjxqz'

freq = {'e': 12.702, 't': 9.056, 'a': 8.167, 'o': 7.507, 'i': 6.966, 'n': 6.749, 's': 6.327,
        'h': 6.094, 'r': 5.987, 'd': 4.253, 'l': 4.025, 'c': 2.782,	'u': 2.758,	'm': 2.406,
        'w': 2.360,	'f': 2.228,	'g': 2.015,	'y': 1.974,	'p': 1.929,	'b': 1.492,	'v': 0.978,
        'k': 0.772,	'j': 0.153,	'x': 0.150,	'q': 0.095,	'z': 0.074}

def score_bytes(l_string):
    score = 0.0
    t = {x:(l_string.lower().count(x) / total_chars)*100 for x in string.ascii_lowercase}
    for x in t.keys():
        score += t[x] / freq[x]
    return score

best = (0,2000)
printable_bytes = bytes(string.printable,'utf8')
ascii_lower_bytes = bytes(string.ascii_lowercase,'utf8')
test = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
test_bytes = unhexlify(test)

for xor_key in range(256):
    test_string = bytes([xor_key ^ c for c in test_bytes])
    total_chars = sum([test_string.count(x) for x in printable_bytes])
    if total_chars == len(test_string):
        # print('Key:',xor_key, test_string)
        p = score_bytes(test_string.decode())
        if p < best[1]:
            best = (xor_key, p, test_string.decode())

    
print("Best XOR Key:", hex(best[0]))
print("Score:",best[1])
print("Decoded String:",best[2])
