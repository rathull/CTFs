f = open('message.txt', 'r')

data = f.read()

map = {
    'b': 'L',
    'k': 'A',
    'v': 'C',
    'i': 'T',
    'm': 'F'
}

# map['q'] = 'D' # ada - there is/are

# (di) - at Case 1 for 2 letter words 
map['q'] = 'D' # di - in/at/on
map['e'] = 'I' # di - in/at/on

# Case 2 for 2 letter words (ke) (DOES NOT WORK)
# map['q'] = 'E' # di - in/at/on
# map['e'] = 'E' # di - in/at/on

# dia
# itu
# ini
# dua

# ADA - there is

# TAPI - but  Case 1 for TAxj
# Definitely wrong because ADALAP
# map['x'] = 'P'
# map['j'] = 'I'

# TAHU - take  Case 2 for TAxj
map['x'] = 'H'
map['j'] = 'U'

# Now, all ADALAP is correct

# APA - what (only option for A_A)
map['c'] = 'P'

# SATU - one  (LIKELY NOT, NOT CONFIRMED)
# LALU - then (NOT SAME LETTERS)
# BARY - new
# map['d'] = 'R'

# APAKAH
map['u'] = 'K'

# map['d'] = 'M'

# PAGI - morning
map['s'] = 'G'

# SUKA - like
map['w'] = 'S'
map['d'] = 'M'

# ANALYSIS
map['f'] = 'N'

# SELEMAT
map['z'] = 'E'

# FREKUENSI
map['t'] = 'R'

# KAMU is off


data_old = data

for o, n in map.items():
    data = data.replace(o, n)

print(data)

for word in data.split():
    if len(word) == 2:
        print(word)
for word in data.split():
    if len(word) == 3:
        print(word)
for word in data.split():
    if len(word) == 4:
        print(word)


print()

sol = 'LACTF{SELAMAT_PAGI_APAKAH_KAMU_SUKA_ANALISIS_FREKUENSI}'
print(sol.lower())

# ke - to
# di - at

# LACTF{SELAMAT PAGI APAKAH ANDA SUKA ANALISIS FREKUENSI}