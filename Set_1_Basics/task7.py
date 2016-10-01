import base64
from Crypto.Cipher import AES

if __name__ == '__main__':
    
    with open('7.txt','rb') as b64_input:
        ciphertext = base64.b64decode(b64_input.read())

    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    
    plaintext = ''.join([cipher.decrypt(ciphertext[x:x+16]).decode() for x in range(0,len(ciphertext),16)])
    print(plaintext)
    
