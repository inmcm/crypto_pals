from operator import xor
import base64
import string
from task5 import key_byte_gen
from task3 import freqs

def hamming_distance(a,b):
    diff_bytes =  bytes(map(xor,a,b))
    hd = 0
    for one_byte in diff_bytes:
        for shft in range(8):
            hd += (one_byte >> shft) & 1
    return hd

if __name__ == '__main__':
    q = b'this is a test'
    w = b'wokka wokka!!!'
    print('Example Hamming Distance:', hamming_distance(q,w))

    with open('6.txt','rb') as b64_input:
        decoded_content = base64.b64decode(b64_input.read())

    best = [8,0]  # Distance score, key_size
    print('\nFind most likely key size:')
    for key_size in range(2,41):
        tests = 16
        score = 0
        for edits in range(tests):
            section1 = decoded_content[key_size*(edits*2):key_size*((edits*2)+1)]
            section2 = decoded_content[key_size*((edits*2)+1):key_size*((edits*2)+2)]
            score += hamming_distance(section1, section2) / key_size
        score /= tests
        print(score,key_size)
        if score < best[0]:
            best[0] = score
            best[1] = key_size

    print('\nBest Key Size:',best[0], best[1],'\n')
    
    positional_arrays = [bytearray() for _ in range(best[1])]
    for x, c_byte in enumerate(decoded_content):
        positional_arrays[x % best[1]].append(c_byte)

    

    key_string = ''
    print("\nFind Each XOR Key Byte:")         
    for x, sample_bytes in enumerate(positional_arrays):
        best = (0,0,0)
        for xor_key in range(256):
            test_bytes = bytes([xor_key ^ c for c in sample_bytes])
            # print(test_bytes[:15])
            total_chars = sum([test_bytes.count(x) for x in string.printable.encode()])
            if total_chars == len(test_bytes):
                test_string = test_bytes.decode()
                score = sum([freqs[x] for x in test_string.lower() if x in freqs])
                if score > best[1]:
                    best = (xor_key, score, test_string)
        key_string += chr(best[0])

            
        print('Position:',x)
        print("Best XOR Key:", hex(best[0]), '(',chr(best[0]),')')
        print("Score:",best[1])
        print('Current Key String:',key_string)

    print('\nFinal Key String:', key_string)    
    p = key_byte_gen(key_string)    
    xor_bytes = bytes([p.next() ^ x for x in decoded_content])
    print('\nDecrypted File:')
    print(xor_bytes)