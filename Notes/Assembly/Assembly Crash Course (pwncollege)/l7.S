.global _start
.intel_syntax noprefix

_start:
    shr rdi, 0x20
    mov rax, 0
    mov al, dil

; as -o l7.o l7.S && objcopy -O binary --only-section=.text ./l7.o ./l7.bin && cat ./l7.bin | /challenge/run