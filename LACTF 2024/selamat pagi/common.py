f = open('common.txt', 'r')
data = f.read()
c = ''

for line in data.splitlines():
    word = line.split('.')[1]
    word = word.split()
    for i in word:
        c += i + '\n'
    
f = open('words.txt', 'w')
f.write(c)