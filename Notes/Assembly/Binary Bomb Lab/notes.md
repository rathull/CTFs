# Bomb Lab (OpenSecurityTraining2)

Recommendations 

- Stay focused on your goal
    - You don’t need to understand every piece of code, you can get stuck in the weeds
    - E.g. look at the exit condition and walk backwards to find out how you avoid those paths

## Phase 1

`objdump -M intel --disassemble bomb` is too much code to work with, so we look to dynamic analysis with GDB on this bomb

We can also use `strings bomb` to get all the strings in this file, see what kind of stuff the bomb might do

```
That's number 2. Keep going!
Halfway there!
Good work! On to the next...
Welcome to my fiendish little bomb. You have 6 phases with
which to blow yourself up. Have a nice day!
Phase 1 defused. How about the next one?
So you got that one. Try this one.
I am just a renegade hockey mom.
Wow! You've defused the secret stage!
So you think you can stop the bomb with ctrl-c, do you?
Curses, you've found the secret phase!
But finding it and solving it are quite different...
Congratulations! You've defused the bomb!
Well...
OK. :-)
Invalid phase%s
BOOM!!!
The bomb has blown up.
```

- We see that at some point, we’ll come across a secret phase

Run with GDB: `gdb ./bomb -q -x ~/gdbCfg`

We have a very narrow window of what’s going on, so let’s use `disas` to see more

```nasm
Dump of assembler code for function main:
=> 0x0000555555555449 <+0>:	endbr64 
   0x000055555555544d <+4>:	push   rbx
   0x000055555555544e <+5>:	cmp    edi,0x1
   0x0000555555555451 <+8>:	je     0x55555555554f <main+262>
   0x0000555555555457 <+14>:	mov    rbx,rsi
   0x000055555555545a <+17>:	cmp    edi,0x2
   0x000055555555545d <+20>:	jne    0x555555555584 <main+315>
   0x0000555555555463 <+26>:	mov    rdi,QWORD PTR [rsi+0x8]
   0x0000555555555467 <+30>:	lea    rsi,[rip+0x1b96]        # 0x555555557004
   0x000055555555546e <+37>:	call   0x5555555552e0 <fopen@plt>
   0x0000555555555473 <+42>:	mov    QWORD PTR [rip+0x421e],rax        # 0x555555559698 <infile>
   0x000055555555547a <+49>:	test   rax,rax
   0x000055555555547d <+52>:	je     0x555555555562 <main+281>
   0x0000555555555483 <+58>:	call   0x555555555b31 <initialize_bomb>
   0x0000555555555488 <+63>:	lea    rdi,[rip+0x1bf9]        # 0x555555557088
   0x000055555555548f <+70>:	call   0x555555555200 <puts@plt>
   0x0000555555555494 <+75>:	lea    rdi,[rip+0x1c2d]        # 0x5555555570c8
   0x000055555555549b <+82>:	call   0x555555555200 <puts@plt>
   0x00005555555554a0 <+87>:	call   0x555555555c56 <read_line>
   0x00005555555554a5 <+92>:	mov    rdi,rax
   0x00005555555554a8 <+95>:	call   0x5555555555a7 <phase_1>
   0x00005555555554ad <+100>:	call   0x555555555d9e <phase_defused>
   0x00005555555554b2 <+105>:	lea    rdi,[rip+0x1c3f]        # 0x5555555570f8
   0x00005555555554b9 <+112>:	call   0x555555555200 <puts@plt>
   0x00005555555554be <+117>:	call   0x555555555c56 <read_line>
   0x00005555555554c3 <+122>:	mov    rdi,rax
   0x00005555555554c6 <+125>:	call   0x5555555555cb <phase_2>
   0x00005555555554cb <+130>:	call   0x555555555d9e <phase_defused>
   0x00005555555554d0 <+135>:	lea    rdi,[rip+0x1b66]        # 0x55555555703d
   0x00005555555554d7 <+142>:	call   0x555555555200 <puts@plt>
   0x00005555555554dc <+147>:	call   0x555555555c56 <read_line>
   0x00005555555554e1 <+152>:	mov    rdi,rax
   0x00005555555554e4 <+155>:	call   0x555555555639 <phase_3>
   0x00005555555554e9 <+160>:	call   0x555555555d9e <phase_defused>
   0x00005555555554ee <+165>:	lea    rdi,[rip+0x1b66]        # 0x55555555705b
   0x00005555555554f5 <+172>:	call   0x555555555200 <puts@plt>
   0x00005555555554fa <+177>:	call   0x555555555c56 <read_line>
   0x00005555555554ff <+182>:	mov    rdi,rax
   0x0000555555555502 <+185>:	call   0x55555555574b <phase_4>
   0x0000555555555507 <+190>:	call   0x555555555d9e <phase_defused>
   0x000055555555550c <+195>:	lea    rdi,[rip+0x1c15]        # 0x555555557128
   0x0000555555555513 <+202>:	call   0x555555555200 <puts@plt>
   0x0000555555555518 <+207>:	call   0x555555555c56 <read_line>
   0x000055555555551d <+212>:	mov    rdi,rax
   0x0000555555555520 <+215>:	call   0x5555555557c4 <phase_5>
   0x0000555555555525 <+220>:	call   0x555555555d9e <phase_defused>
   0x000055555555552a <+225>:	lea    rdi,[rip+0x1b39]        # 0x55555555706a
   0x0000555555555531 <+232>:	call   0x555555555200 <puts@plt>
   0x0000555555555536 <+237>:	call   0x555555555c56 <read_line>
   0x000055555555553b <+242>:	mov    rdi,rax
   0x000055555555553e <+245>:	call   0x55555555585b <phase_6>
   0x0000555555555543 <+250>:	call   0x555555555d9e <phase_defused>
   0x0000555555555548 <+255>:	mov    eax,0x0
   0x000055555555554d <+260>:	pop    rbx
   0x000055555555554e <+261>:	ret    
   0x000055555555554f <+262>:	mov    rax,QWORD PTR [rip+0x411a]        # 0x555555559670 <stdin@@GLIBC_2.2.5>
   0x0000555555555556 <+269>:	mov    QWORD PTR [rip+0x413b],rax        # 0x555555559698 <infile>
   0x000055555555555d <+276>:	jmp    0x555555555483 <main+58>
   0x0000555555555562 <+281>:	mov    rcx,QWORD PTR [rbx+0x8]
   0x0000555555555566 <+285>:	mov    rdx,QWORD PTR [rbx]
   0x0000555555555569 <+288>:	lea    rsi,[rip+0x1a96]        # 0x555555557006
   0x0000555555555570 <+295>:	mov    edi,0x1
   0x0000555555555575 <+300>:	call   0x5555555552d0 <__printf_chk@plt>
   0x000055555555557a <+305>:	mov    edi,0x8
   0x000055555555557f <+310>:	call   0x5555555552f0 <exit@plt>
   0x0000555555555584 <+315>:	mov    rdx,QWORD PTR [rsi]
   0x0000555555555587 <+318>:	lea    rsi,[rip+0x1a95]        # 0x555555557023
   0x000055555555558e <+325>:	mov    edi,0x1
   0x0000555555555593 <+330>:	mov    eax,0x0
   0x0000555555555598 <+335>:	call   0x5555555552d0 <__printf_chk@plt>
   0x000055555555559d <+340>:	mov    edi,0x8
   0x00005555555555a2 <+345>:	call   0x5555555552f0 <exit@plt>
End of assembler dump.
```

There are function calls to each phase and each defuse

For phase 1, we want to look within the `phase_1` function and find a call to `0x5555555554ad`

Let’s start by disassembling this phase with `disas phase_1`

```nasm
Dump of assembler code for function phase_1:
   0x00005555555555a7 <+0>:	endbr64 
   0x00005555555555ab <+4>:	sub    rsp,0x8
   0x00005555555555af <+8>:	lea    rsi,[rip+0x1b9a]        # 0x555555557150
   0x00005555555555b6 <+15>:	call   0x555555555ad1 <strings_not_equal>
   0x00005555555555bb <+20>:	test   eax,eax
   0x00005555555555bd <+22>:	jne    0x5555555555c4 <phase_1+29>
   0x00005555555555bf <+24>:	add    rsp,0x8
   0x00005555555555c3 <+28>:	ret    
   0x00005555555555c4 <+29>:	call   0x555555555be5 <explode_bomb>
   0x00005555555555c9 <+34>:	jmp    0x5555555555bf <phase_1+24>
End of assembler dump
```

We want to make the program jump to `<phase_1+29>`, since this passes the `explode_bomb` call

- We see there is some string check here

Let’s jump through the code with `ni` until we reach phase 1

Once we hid read_line, the debugger waits for an input

Let’s put in a test string and keep going, like “input”

We know that in the calling convention, the first parameters to the function call at phase_1 would be `rdi`, `rsi`, `rcx` `rdx`, `r8`, `r9` respectively

Let’s check what’s at the memory location of `rdi` using `x/16bx 0x5555555596a0`

- This corresponds to the string “input” that we passed in

Let’s step into phase 1 with and keep stepping until `strings_not_equal`

- The two pointers this takes in are likely `rdi` and `rsi`
- We can use `x/s 0x555555557150` to find the string at `rsi`, which is "I am just a renegade hockey mom.”
- We have to fail the `strings_not_equal` check move to the next part of main, defusing phase 1

Sol: to defuse phase 1, pass in the input “I am just a renegade hockey mom.” 

### Phase 2

Skip through to phase 2 (or edit gdbCfg file to include `b phase_2`)

Let’s also create a text file with our solutions and use `start defuse.txt` in GDB

Once we reach, disassemble phase 2

```nasm
Dump of assembler code for function phase_2:
   0x00005555555555cb <+0>:	endbr64 
   0x00005555555555cf <+4>:	push   %rbp
   0x00005555555555d0 <+5>:	push   %rbx
   0x00005555555555d1 <+6>:	sub    $0x28,%rsp
   0x00005555555555d5 <+10>:	mov    %fs:0x28,%rax
   0x00005555555555de <+19>:	mov    %rax,0x18(%rsp)
   0x00005555555555e3 <+24>:	xor    %eax,%eax
   0x00005555555555e5 <+26>:	mov    %rsp,%rsi
   0x00005555555555e8 <+29>:	call   0x555555555c11 <read_six_numbers>
   0x00005555555555ed <+34>:	cmpl   $0x1,(%rsp)
   0x00005555555555f1 <+38>:	jne    0x5555555555fd <phase_2+50>
   0x00005555555555f3 <+40>:	mov    %rsp,%rbx
   0x00005555555555f6 <+43>:	lea    0x14(%rsp),%rbp
   0x00005555555555fb <+48>:	jmp    0x555555555612 <phase_2+71>
   0x00005555555555fd <+50>:	call   0x555555555be5 <explode_bomb>
   0x0000555555555602 <+55>:	jmp    0x5555555555f3 <phase_2+40>
   0x0000555555555604 <+57>:	call   0x555555555be5 <explode_bomb>
   0x0000555555555609 <+62>:	add    $0x4,%rbx
   0x000055555555560d <+66>:	cmp    %rbp,%rbx
   0x0000555555555610 <+69>:	je     0x55555555561d <phase_2+82>
   0x0000555555555612 <+71>:	mov    (%rbx),%eax
   0x0000555555555614 <+73>:	add    %eax,%eax
   0x0000555555555616 <+75>:	cmp    %eax,0x4(%rbx)
   0x0000555555555619 <+78>:	je     0x555555555609 <phase_2+62>
   0x000055555555561b <+80>:	jmp    0x555555555604 <phase_2+57>
   0x000055555555561d <+82>:	mov    0x18(%rsp),%rax
   0x0000555555555622 <+87>:	xor    %fs:0x28,%rax
   0x000055555555562b <+96>:	jne    0x555555555634 <phase_2+105>
   0x000055555555562d <+98>:	add    $0x28,%rsp
   0x0000555555555631 <+102>:	pop    %rbx
   0x0000555555555632 <+103>:	pop    %rbp
   0x0000555555555633 <+104>:	ret    
   0x0000555555555634 <+105>:	call   0x555555555220 <__stack_chk_fail@plt>
End of assembler dump.
```

Out exit condition is passing the `je` at byte 69

Let’s start with an example input of numbers `10 11 12 13 14 15` (hex A B C D E F)

Skip ahead to `read_size_numbers`

- We need to start by failing the `jne` 38 bytes after phase_2, as this jump leads to an explosion
- To fail this, the value at `[rsp]` must be equal to `0x1`

Let’s skip to read_six_numbers and see where the numbers are read into

If we read the first 24 bytes on the stack at `[rsp]`, we get all our 6 inputs separated by four zeros

- These are all 32-bit ints stored in little endian

Going back to the first comparison we have to fail, since `[rsp]` must be equal to `0x1`, our first input value must be a 1 

******first input = 1, now we are at byte 40******

After this, our code:

1. `rbx` is a pointer to the first input value
2. `rbp` is a pointer to the rsp+20, last input value
3. Jump to byte 71
4. Move `rbx` into `eax`
5. Double `eax`
6. Compare `eax` with the next value 4 bytes after `rbx`
7. If these are not equal, the bomb explodes
8. If they are equal (e.g. the input value is equal to double the next input value), jump back to byte 62
9. At byte 62, move `rbx` to the next input value
10. Compare `rbx` to `rbp`, if they’re equal, this is our exit condition
11. Go back to step 3 and repeat

So to make sure we don’t repeat, for all input values, the next input value must be two times greater

Sol: to defuse, pass in 6 integers `1 2 4 8 16 32`
