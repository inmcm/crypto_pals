

def pad_bytes_size(in_bytes, block_size):
    input_len = len(in_bytes)
    if (input_len % block_size) == 0:
        return in_bytes
    pad_size = block_size - (input_len % block_size)
    padded_bytes = in_bytes + bytes([pad_size for _ in range(pad_size)])
    return padded_bytes


if __name__ == '__main__':
    test_bytes = b'YELLOW SUBMARINE'
    block_size = 20
    padded = pad_bytes_size(test_bytes, block_size)
    print('Block Size:', block_size)
    print('Before:', test_bytes)
    print('After:', padded)

    test_bytes = b'A'
    block_size = 16
    padded = pad_bytes_size(test_bytes, block_size)
    print('Block Size:',block_size)
    print('Before:',test_bytes)
    print('After:', padded)
