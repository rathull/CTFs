c = 'Ta _7N6D8Dhlg:W3D_H3C31N__387ef sHR053F38N43DFD i33___N6'
m = ''
i = 0

a = [[],[],[],[]]
down = True
curr =  0
for i in range(0, len(c)):
    if down:
        if curr != 3:
            a[curr].append(i)
            # print(f'{i} at {curr}')
            curr += 1
        elif curr == 3:
            # print(f'{i} at {curr}')
            a[curr].append(i)
            curr -= 1
            down = False
    else:
        if curr != 0:
            # print(f'{i} at {curr}')
            a[curr].append(i)
            curr -= 1
        elif curr == 0:
            # print(f'{i} at {curr}')
            a[curr].append(i)
            curr += 1
            down = True
l = []
for r in range(0, 4):
    for i in a[r]:
        l.append(i)
# print(l)
for i in l:
    m += c[i]
print(m)
# for i in a:
#     print(i)