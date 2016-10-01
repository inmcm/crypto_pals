from binascii import hexlify, unhexlify

class key_byte_gen:
    def __init__(self, key_string):
        self.count = 0
        self.key = key_string.encode()
        self.key_length = len(self.key)

    def next(self):
        key_byte = self.key[self.count % self.key_length]
        self.count += 1
        return key_byte

if __name__ == '__main__':  
    p = key_byte_gen('ICE')
    input_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    input_bytes = input_string.encode()

    xor_bytes = bytes([p.next() ^ x for x in input_bytes])
    print(hexlify(xor_bytes))
    solution = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    solution_bytes = unhexlify(solution)
    p = key_byte_gen('ICE')
    f = bytes([p.next() ^ x for x in solution_bytes])
    print(f.decode())
    assert f.decode() == input_string