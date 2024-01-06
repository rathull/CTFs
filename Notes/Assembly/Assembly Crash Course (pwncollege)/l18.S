.global _start
.intel_syntax noprefix

_start:
    mov rax, [rdi+4]
    mov rdx, 0x7f454c46
    cmp [rdi], rdx
    je XEQ
    mov rdx, 0x00005A4D
    cmp [rdi], rdx
    je YEQ
    jmp ELSE
    XEQ:   
        mov rdx, 0
        mov edx, [rdi+8]
        movsx rdx, edx
        add rax, rdx

        mov rdx, 0
        mov edx, [rdi+12]
        movsx rdx, edx
        add rax, rdx
    YEQ:
        mov rdx, 0
        mov edx, [rdi+8]
        movsx rdx, edx
        sub rax, rdx

        mov rdx, 0
        mov edx, [rdi+12]
        movsx rdx, edx
        sub rax, rdx
    ELSE:
        mov rdx, 0
        mov edx, [rdi+8]
        movsx rdx, edx
        imul rax, rdx

        mov rdx, 0
        mov edx, [rdi+12]
        movsx rdx, edx
        imul rax, rdx

; as -o l18.o l18.S && objcopy -O binary --only-section=.text ./l18.o ./l18.bin && cat ./l18.bin | /challenge/run