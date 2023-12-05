import base64

# Decode base64 of string
c = "LEs2fVVxNDMfNHEtcx80cB8nczQfJhVkDHI/Ew=="
c = base64.b64decode(c)

print('Ciphertext:', c)

# Solve for the key by reversing xors
flag_known = 'flag{}'
key = [0]*6
key[0] = chr(c[0]^ord(flag_known[0]))
for i in range(1, 5):
    key[i] = c[i]^ord(flag_known[i])
    for prev in range(i):
        key[i] ^= ord(key[prev])
    key[i] = chr(key[i])
key[5] = chr(c[-1]^ord(flag_known[-1]))

print('Key: ', ''.join(key))

# Repeat encryption algorithm
flag_len = len(c)
key_len = len(key)
output = list(c)

for i in range(flag_len - key_len + 1):
    for j in range(key_len):
        output[i + j] ^= ord(key[j])
        
print('Flag: ', end='')
for i in output:
    print(chr(i), end='')