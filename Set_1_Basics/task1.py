import base64
w = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
d = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
print(hex(d))
c = d.to_bytes(48,'big')
print(c)
v = base64.b64encode(c)
print(v)
assert w == v
