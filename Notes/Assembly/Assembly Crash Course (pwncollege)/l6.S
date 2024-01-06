.global _start
.intel_syntax

_start:
    mov %rax, 0
    mov %al, %dil
    mov %rbx, 0
    mov %bx, %si

; as -o l6.o l6.S && objcopy -O binary --only-section=.text ./l6.o ./l6.bin && cat ./l6.bin | /challenge/run