from task6 import hamming_distance
from itertools import combinations

with open('8.txt','rb') as source_file:
    ciphertexts = source_file.read().splitlines()

block_size = 16

for entry, ctext in enumerate(ciphertexts):
    matches = 0
    block_cnt = len(ctext) // block_size
    blocks = [ctext[x*block_size:(x+1)*block_size] for x in range(block_cnt)]
    block_pairs = combinations(blocks, 2)
    for pair in block_pairs:
        score = hamming_distance(*pair)
        if score == 0:
            print('Match!',entry,*pair)
            matches += 1
    if matches:
        print('Block',entry, 'had' , matches, 'matches')