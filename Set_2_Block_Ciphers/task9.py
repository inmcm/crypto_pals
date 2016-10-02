

def pad_bytes_size(in_bytes, block_size):
    if len(in_bytes) > block_size:
        pad_size = block_size - (len(in_bytes) % block_size) 
    else:
        pad_size = block_size % len(in_bytes)
    
    padded_bytes = in_bytes + bytes([pad_size for _ in range(pad_size)])
    return padded_bytes


if __name__ == '__main__':
    test_bytes = b'YELLOW SUBMARINE'
    block_size = 20
    padded = pad_bytes_size(test_bytes, block_size)
    print('Block Size:',block_size)
    print('Before:',test_bytes)
    print('After:', padded)
