def modinv(a, m):
  def eea(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = eea(b % a, a)
        return (g, x - (b//a) * y, y)

  g, x, y = eea(a, m)
  return -1 if g != 1 else x % m

c = [104, 85, 69, 354, 344, 50, 149, 65, 187, 420, 77, 127, 385, 318, 133, 72, 206, 236, 206, 83, 342, 206, 370]
sol = ''
for i in range(len(c)):
    c[i] %= 41
    c[i] = modinv(c[i], 41)
    if (c[i] <= 26): sol += chr(c[i]+64)
    elif (c[i] <= 36): sol += chr(c[i]+48-27)
    else: sol += '_'
print(sol)
