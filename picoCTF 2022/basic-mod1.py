c = [202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390, 383, 225, 258, 38, 291, 75, 324, 401, 142, 288, 397, ]
sol = ''
for i in range(len(c)):
    c[i] %= 37
    if (c[i] <= 25): sol += chr(c[i]+65)
    elif (c[i] <= 35): sol += chr(c[i]+48-26)
    else: sol += '_'
print(sol)
