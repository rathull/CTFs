.global _start
.intel_syntax noprefix

_start:
    mov rax, [rsp+0x18]
    add rax, [rsp+0x10]
    add rax, [rsp+0x8]
    add rax, [rsp]
    shr rax, 2
    push rax


; as -o l16.o l16.S && objcopy -O binary --only-section=.text ./l16.o ./l16.bin && cat ./l16.bin | /challenge/run