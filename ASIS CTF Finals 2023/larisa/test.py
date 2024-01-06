from Crypto.Util.number import *
from tqdm import tqdm

nbit = 1024
def next_prime(r):
    i = 0
    while True:
        if isPrime(r):
            return r, i
        r += 1
        i += 1
    
# Find rough upper bound for c, d
x = 0
for _ in tqdm(range(100)):
    p = getPrime(nbit // 2)
    P, c = next_prime(p * getPrime(nbit // 2 - 10))
    Q, d = next_prime(p * getPrime(nbit // 2 - 10))
    x = max(x, c)
    x = max(x, d)
print(x)

n = P*Q

print(len(long_to_bytes(p)*8))
print({len(long_to_bytes(getPrime(nbit // 2 - 10))*8)})
print(len(long_to_bytes(n)*8))