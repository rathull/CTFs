.global _start
.intel_syntax noprefix

_start:
    mov DWORD PTR [rdi], 0x7f454c46

    mov rax, [rdi+4]
    mov edx, 0x7f454c46
    cmp [edi], edx
    je XEQ
    mov edx, 0x00005A4D
    cmp DWORD PTR [rdi], edx
    je YEQ

    mov rax, 3
    int 3
    mov rdx, 0
    mov edx, [rdi+8]
    movsx rdx, edx
    imul rax, rdx

    mov rdx, 0
    mov edx, [rdi+12]
    movsx rdx, edx
    imul rax, rdx
    XEQ:   
        mov rax, 1
        int 3
        mov rdx, 0
        mov edx, [rdi+8]
        movsx rdx, edx
        add rax, rdx

        mov rdx, 0
        mov edx, [rdi+12]
        movsx rdx, edx
        add rax, rdx
    YEQ:
        mov rax, 2
        int 3
        mov rdx, 0
        mov edx, [rdi+8]
        movsx rdx, edx
        sub rax, rdx

        mov rdx, 0
        mov edx, [rdi+12]
        movsx rdx, edx
        sub rax, rdx

; as -o l18.o l18.S && objcopy -O binary --only-section=.text ./l18.o ./l18.bin && cat ./l18.bin | /challenge/run