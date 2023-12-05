a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def encrypt(text,s):
    res = ""
    for i in range(len(text)):
        c = ord(text[i])
        if c <= 57:
            new = c - 57 + 21
        elif c <= 90:
            new = (c - 65) + 10 + 21
            if new >= 10:
        else:
            res += '_'
            continue
        new %= len(a)
        res += a[new]
    return res

print(
    encrypt(
        'H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_AJ8H7JJ7', 
        21
    )
)