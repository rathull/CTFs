import numpy as np
from PIL import Image

img = Image.open('6e7ee269ddfdddc28304a10b36991812.png')
arr = np.array(img)[0,:,1]
s = ''
for i in arr:
    # s += bytes.fromhex(str(hex(i))[2:]).decode('ASCII')
    # s += str(i) + '\n'
    s += chr(i)
    # print(bytes.fromhex(str(hex(i))[2:]).decode('ASCII'), end='')
    
open('green.txt', 'w').write(s)
print(min(arr), max(arr))