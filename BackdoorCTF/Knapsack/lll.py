# https://www.cs.sjsu.edu/faculty/stamp/papers/topics/topic16/Knapsack.pdf
import olll
import numpy as np

T = [600848253359, 617370603129, 506919465064, 218995773533, 831016169202, 501743312177, 15915022145, 902217876313, 16106924577, 339484425400, 372255158657, 612977795139, 755932592051, 188931588244, 266379866558, 661628157071, 428027838199, 929094803770, 917715204448, 103431741147, 549163664804, 398306592361, 442876575930, 641158284784, 492384131229, 524027495955, 232203211652, 213223394430, 322608432478, 721091079509, 518513918024, 397397503488, 62846154328, 725196249396, 443022485079, 547194537747, 348150826751, 522851553238, 421636467374, 12712949979]
# Our message M = k, the key for encryption
C = 7929089016814

# We can write the encryption as TU=C
# Where T is the public knaspack and U = (u_0, u_1, ..., u_39)
# Write this in the form MV=W, and apply the LLL algorithm to M
M = np.zeros((41, 41), dtype='int64')

# Fill in identity matrix
for i in range(40):
    M[i,i] = 1


# Replace bottom row with public key
for i in range(40):
    M[i,40] = T[i]

# Last element will be encoded messages
M[40,40] = C

M_list = M.tolist()

res = olll.reduction(M_list, 0.1)
# print(res)
for c in range(len(M[0])):
    for r in range(len(M)):
        print(M[r][c], end=' ')
    print()
