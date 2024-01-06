.global _start
.intel_syntax

_start:
    xor %rax, %rax
    not %rax
    and %rax, %rdi
    and %rax, %rsi

; as -o l8.o l8.S && objcopy -O binary --only-section=.text ./l8.o ./l8.bin && cat ./l8.bin | /challenge/run
