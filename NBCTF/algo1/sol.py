f = open('in.txt' ,'r')
n = int(f.readline())
a, b = f.readline().split(' ')
c = f.readline()

arr = c.split('/')
for i in arr:
    print(i)
    