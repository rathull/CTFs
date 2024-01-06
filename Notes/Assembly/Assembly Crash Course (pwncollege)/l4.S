.global _start
.intel_syntax

_start:
    mov %rdx, 0
    mov %rax, %rdi
    div %rsi

; as -o l4.o l4.S && objcopy -O binary --only-section=.text ./l4.o ./l4.bin && cat ./l4.bin | /challenge/run