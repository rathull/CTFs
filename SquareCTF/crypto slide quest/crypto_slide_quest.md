# Crypto Slide Quest - SquareCTF
### Chllenge Prompt
We are given a ciphertext (encoded in base64) and a C program used to encrypt the flag into this file. We also know there is a secret key involved. The encryption technique is as follows:

```C
_Static_assert(sizeof(key) == 7, "Invalid key size!");

char* output = malloc(sizeof(flag));
strncpy(output, flag, sizeof(flag));

int flag_len = strlen(flag);
int key_len = strlen(key);

for(int i = 0; i < flag_len - key_len + 1; i++) {
    for(int j = 0; j < key_len; j++) {
        output[i + j] ^= key[j];
    }
}

printf("%s", moutput);
```

### The Encryption Program
We'll begin by analyzing the provided encryption program to understand how our ciphertext was created. We are primarily interested in the nested for loops in the middle of the program, as this is where our encryption occurs. We notice that the outer for loop loops from $0$ to the flag's length, leaving room for the length of the key. The inner loop loops $j$ from 0 to the length of the key. The indices we access are the sums of these values, essentially performing operations in a sliding window of length equal to the size of the key string. We also note that the operation in this sliding window is an XOR between the sliding window and the key. 

### Solution Idea

We start by attempting to determine what our key is. The `assert` statement at the beginning of the program ensures that the size of the key variable is 7. However, since this value is a C string, one of these characters will be the zero byte `\0'`, so we know our key consists of 6 characters.

Additionally, we can pair this with the fact that we already know a portion of the characters in the plaintext. SquareCTF's flags are of the form `flag{...}`, so we know 6 of these characters. Since we know 6 characters of the plaintext corresponding 6 characters in the ciphertext created with the 6 character key, we represent encryption in a system of 6 XOR equations. This is a system of 6 equations and 6 unknowns that we can solve.

### More on XOR

XOR is the exclusive OR logic gate, which returns True if its two inputs are different, and it has some unique properties we can leverage to solve this problem. XOR behaves as shown in the truth table below:

|   $a$     |   $b$     |  $a\oplus b$     |
| ------- | ------- | ------- |
|1|1|0|
|1|0|1|
|0|1|1|
|0|0|0|

First, we notice that XOR is *commutative*. That is, the order of the elements in an XOR operation does not matter, and $a\oplus b=b\oplus a$. 

Additionally, if we extend the table:

   $a$     |   $b$     |  $a\oplus b$     |$a\oplus b\oplus b$     |
| ------- | ------- | ------- | ------- |
|1|1|0|1|
|1|0|1|1|
|0|1|1|0|
|0|0|0|0|

We see that $a\oplus b \oplus b=a$, so XOR is also *self-inverting*. This means XOR is *not* a one-way function. One-way functions are a standard in modern cryptographic algorithms as they are easy to compute and hard to reverse, ensuring that text can be easily encrypted but not decrypted by attackers. However, in this algorithm, we use the same key and algorithm to encrypt and decrypt. Therefore, we can exploit this to reverse our encryption algorithm if we know the key. This is an example of *symmetric key cryptography*.

### Reversing our Key
Using our XOR sliding window, we can derive the following equations from the encryption loop in our provided encryption program. Let the key consist of character variables labeled a-f:
\[
    \text{flag[0]}\oplus a=\text{c[0]} \\
    \text{flag[1]}\oplus a\oplus b=\text{c[1]} \\
    \text{flag[2]}\oplus a\oplus b\oplus c=\text{c[2]} \\
    \text{flag[3]}\oplus a\oplus b\oplus c\oplus d=\text{c[3]} \\
    \text{flag[4]}\oplus a\oplus b\oplus c\oplus d\oplus e=\text{c[4]} \\
    \ldots \\
    \text{flag[-1]}\oplus g=\text{c[-1]}
\]

Using the commutative property of XOR, we can reorganize these as:
\[
    a\oplus \text{flag[0]}=\text{c[0]} \\
    a\oplus b\oplus \text{flag[1]}=\text{c[1]} \\
    a\oplus b\oplus c\oplus \text{flag[2]}=\text{c[2]} \\
    a\oplus b\oplus c\oplus d\oplus \text{flag[3]}=\text{c[3]} \\
    a\oplus b\oplus c\oplus d\oplus e\oplus \text{flag[4]}=\text{c[4]} \\
    \ldots \\
    g\oplus \text{flag[-1]}=\text{c[-1]}
\]

Using the self-inverting property, we can move all our known values to one side of this system:
\[
    a\oplus \text{flag[0]}\oplus \text{flag[0]}=a=\text{c[0]}\oplus \text{flag[0]} \\
    a\oplus b\oplus \text{flag[1]}\oplus \text{flag[1]}=a\oplus b=\text{c[1]} \oplus \text{flag[1]}\\
    a\oplus b\oplus c\oplus \text{flag[2]}\oplus \text{flag[2]}=(a\oplus b)\oplus c=\text{c[2]}\oplus \text{flag[2]} \\
    a\oplus b\oplus c\oplus d\oplus \text{flag[3]}\oplus \text{flag[3]}=(a\oplus b\oplus c)\oplus d=\text{c[3]}\oplus \text{flag[3]} \\
    a\oplus b\oplus c\oplus d\oplus e\oplus \text{flag[4]}\oplus \text{flag[4]}=(a\oplus b\oplus c\oplus d)\oplus e=\text{c[4]}\oplus \text{flag[4]} \\
    \ldots \\
    g\oplus \text{flag[-1]}\oplus \text{flag[-1]}=g=\text{c[-1]}\oplus \text{flag[-1]} \\
\]
And using the commutative property again:
\[
    a=\text{c[0]}\oplus \text{flag[0]} \\
    b=\text{c[1]} \oplus \text{flag[1]}\oplus a\\
    c=\text{c[2]}\oplus \text{flag[2]}\oplus a\oplus b\\
    d=\text{c[3]}\oplus \text{flag[3]}\oplus a\oplus b\oplus c\\
    e=\text{c[4]}\oplus \text{flag[4]}\oplus a\oplus b\oplus c\oplus d\\
    \ldots \\
    g=\text{c[-1]}\oplus \text{flag[-1]}
\]
This is a recurrence we can calculate using a simple Python script. Once we have the key, we can use it with the ciphertext to reverse the encryption algorithm.

### Solution Script
We can use the following Python script to solve for the key. First, we decode the ciphertext from base64, and then calculate the XORs above.
```Python
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
```
Since we've already determined that XOR is reversible and not a one-way function, we can simply use this key with our encryption algorithm again to decrypt our ciphertext:
```Python
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
```
This recovers our plaintext! The output is the flag: `flag{1ts_t1m3_t0_g3t_fUnkee}`.