.global _start
.intel_syntax noprefix

_start:
    mov rax, [rdi]
    mov rdx, [rdi+8]
    add rax, rdx
    mov [rsi], rax

; as -o l13.o l13.S && objcopy -O binary --only-section=.text ./l13.o ./l13.bin && cat ./l13.bin | /challenge/run