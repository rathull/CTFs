.global _start
.intel_syntax

_start:
    mov %rax, 0
    mov %al, [0x404000]
    mov %rbx, 0
    mov %bx, [0x404000]
    mov %rcx, 0
    mov %ecx, [0x404000]
    mov %rdx, [0x404000]

; as -o l11.o l11.S && objcopy -O binary --only-section=.text ./l11.o ./l11.bin && cat ./l11.bin | /challenge/run