from binascii import hexlify
from gmpy2 import mpz_urandomb, next_prime, random_state
import math
import os
import sys

if sys.version_info < (3, 9):
    import gmpy2
    math.gcd = gmpy2.gcd
    math.lcm = gmpy2.lcm


FLAG  = open('flag.txt').read().strip()
FLAG  = int(hexlify(FLAG.encode()), 16)
SEED  = int(hexlify(os.urandom(32)).decode(), 16)
STATE = random_state(SEED)

def get_prime(bits):
    return next_prime(mpz_urandomb(STATE, bits) | (1 << (bits - 1)))

p = get_prime(1024)
q = get_prime(1024)

x = p + q
n = p * q

'''
x = p+q = 283448763112935396292672508494677342956387692709613190747337505254745038440112219196768813935476747610338768373312897468544362172877862811371116345292731982030202799279648808568611019652855145745874995725323535434244721756466664844450642633991884547297913224974132790120791402207195730139176850623910443635096
n = p*q = 19594979821655183104856721200876279688744199212596318791410700925214020940999368124753876379046101491755637328180352524777390418669210709696131801135729820817964419360433309338628094186567119917735965630612618443318361476838501333469511238156792898753876667912964148133223421606462036819614830830346046983259407147596111671725522875516790826213635619398696281968888325882416381776971733880221909903860599888903194248107358128483103962534467323374352040906477803568664482713174891860915973023918444553550090873773281086421418960484839799410173913761912529789181262819973734812402783319741028408456027454148088452256679
'''

e = 65537

m = math.lcm(p - 1, q - 1)

print(m)

d = pow(e, -1, m)

c = pow(FLAG, e, n)

print(f'x = {x:x}')
print(f'n = {n:x}')
print(f'c = {c:x}')