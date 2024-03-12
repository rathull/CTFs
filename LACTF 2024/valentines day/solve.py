import re

c = open('ct.txt', 'r').read().replace(' ', '').replace('\n', '').lower()
m = open('intro.txt', 'r').read().replace(' ', '').replace('\n', '').lower()
# c = open('ct.txt', 'r').read().lower()
# m = open('intro.txt', 'r').read().lower()
# print(c)
# print(m)
 
key = ['*']*161
    
# c = m + key
def encrypt(m, key):
    encrypted_message = ""
    for i in range(len(m)):
        if key[i % len(key)] == '*':
            encrypted_message += '*'
        else:
            offset = ord(key[i % len(key)]) - ord('a')
            base = ord('a')
            offset += ord(m[i])
            if offset >= base + 26:
                offset -= 26
            encrypted_message += chr(offset)
    return encrypted_message

# m = c - key
def decrypt(c, key):
    decrypted_message = ""
    ptr = 0
    for i in range(len(c)):
        if key[ptr % len(key)] == '*':
            decrypted_message += '*'
            ptr += 1
        elif c[i].isalpha():
            offset = ord(key[ptr % len(key)]) - ord('a')
            base = ord('a')
            offset = ord(c[i]) - offset
            if offset < base:
                offset += 26
            decrypted_message += chr(offset)
            ptr += 1
        else: 
            decrypted_message += c[i]
            
    return decrypted_message

def recover_key_start(m, c):
    key_offsets = [0]*len(m)
    for i in range(len(m)):
        key_offsets[i] = ord(c[i]) - ord(m[i])
        key_offsets[i] %= 26
    return [chr(i + ord('a')) for i in key_offsets]

def get_lyrics():
    l = '''Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    We've known each other for so long
    Your heart's been aching, but you're too shy to say it (say it)
    '''
    
    l = l.replace(' ', '').replace('\n', '').replace('\'', '').lower()[:161]
    # print(len(l), l)
    return l

# print(''.join(encrypt(m, key)))
recovered = recover_key_start(m=m, c=c)
key[:len(recovered)] = recovered
print(''.join(key), end='\n\n\n')
# print(encrypt(m=m, key=key))
key = get_lyrics()
decrypted = ''.join(decrypt(c=c, key=key))
print(decrypted)
# print(re.match(r'lactf', decrypted))