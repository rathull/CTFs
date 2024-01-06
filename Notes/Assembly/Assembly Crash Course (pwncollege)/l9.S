.global _start
.intel_syntax

_start:
    xor %rax, %rax
    or %rax, %rdi
    and %rax, 0x0000000000000001
    xor %al, 0x01

; as -o l9.o l9.S && objcopy -O binary --only-section=.text ./l9.o ./l9.bin && cat ./l9.bin | /challenge/run
