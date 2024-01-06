.global _start
.intel_syntax

_start:
    mov %rdx, 0
    mov %rax, %rdi
    div %rsi
    mov %rax, %rdx

; as -o l5.o l5.S && objcopy -O binary --only-section=.text ./l5.o ./l5.bin && cat ./l5.bin | /challenge/run