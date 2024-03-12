from pwn import *
import random
from sympy.ntheory import legendre_symbol, isprime
from sympy import gcd

HOST = "chall.lac.tf"
PORT = 31171

n = 0  # The modulus
e = 0  # The public exponent
c = 0  # The ciphertext

def query_advice(x):
    io = remote(HOST, PORT)
    io.sendlineafter("Enter your number: ", str(x))
    y = int(io.recvline().strip())
    io.close()
    return y

def find_p_and_q():
    while True:
        # Choose a random x
        x = random.randint(2, n-1)
        
        # Ensure x is not a perfect square to avoid trivial roots
        if legendre_symbol(x, n) == 1:
            continue

        try:
            y = query_advice(x)
        except EOFError:
            # The advice function exits if x is not a quadratic residue mod p or q
            continue

        # revale p, q, or fumble
        p_or_q = gcd(n, (x**2 - y**2) % n)

        if 1 < p_or_q < n:
            # Found a non-trivial factor
            p = p_or_q
            q = n // p
            if isprime(p) and isprime(q):
                return p, q

# Main script to factor n
if __name__ == "__main__":
    p, q = find_p_and_q()
    print(f"Found factors: p = {p}, q = {q}")
