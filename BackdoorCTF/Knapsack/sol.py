from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
c = 'af95a58f4fbab33cd98f2bfcdcd19a101c04232ac6e8f7e9b705b942be9707b66ac0e62ed38f14046d1cd86b133ebda9'

arr = [600848253359, 617370603129, 506919465064, 218995773533, 831016169202, 501743312177, 15915022145, 902217876313, 16106924577, 339484425400, 372255158657, 612977795139, 755932592051, 188931588244, 266379866558, 661628157071, 428027838199, 929094803770, 917715204448, 103431741147, 549163664804, 398306592361, 442876575930, 641158284784, 492384131229, 524027495955, 232203211652, 213223394430, 322608432478, 721091079509, 518513918024, 397397503488, 62846154328, 725196249396, 443022485079, 547194537747, 348150826751, 522851553238, 421636467374, 12712949979]
s = 7929089016814

# First, let's try to find properties of these numbers
# Let's start by comparing their bits
sum_3_zero = 0
for n in arr:
    print(bin(n)[2:].zfill(43))
    if bin(n)[2:].zfill(43)[3] == '1':
        sum_3_zero += 1

print()
print(sum_3_zero)
print()
print(bin(s)[2:])



'''
reconstructed_key = 0
for i in range(len(arr)):
    if arr[i] <= s:
        s -= arr[i]
        # Set corresponding bit in the reconstructed key
        reconstructed_key |= (1 << i)

print(f"Reconstructed Key: {reconstructed_key}")
print(f"Reconstructed Key (hex): {hex(reconstructed_key)}")
print(f"Reconstructed Key (bytes): {long_to_bytes(reconstructed_key)}")
print()

key_bits = [0] * 40
for i in range(40):
    bit = (s >> i) & 1
    if bit == 1:
        key_bits[i] = 1


reconstructed_key = long_to_bytes(int("".join(map(str, key_bits)), 2), blocksize=16)

print(f"Reconstructed Key (hex): {reconstructed_key.hex()}")

cipher = AES.new(reconstructed_key, AES.MODE_ECB)
decrypted = cipher.decrypt(c)
# print(decrypted)
'''