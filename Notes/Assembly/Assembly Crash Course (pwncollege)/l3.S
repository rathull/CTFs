.global _start
.intel_syntax noprefix

_start:
    mov rax, rsi
    imul rax, rdi
    add rax, rdx
