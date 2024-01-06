.global _start
.intel_syntax noprefix

_start:
    mov DWORD PTR [rdi], 0x00001337
    mov DWORD PTR [rdi+4], 0xdeadbeef
    mov DWORD PTR [rsi], 0xffee0000
    mov DWORD PTR [rsi+4], 0xc0

; as -o l12.o l12.S && objcopy -O binary --only-section=.text ./l12.o ./l12.bin && cat ./l12.bin | /challenge/run