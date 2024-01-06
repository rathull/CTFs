.global _start
.intel_syntax

_start:
    mov %rax, [0x404000]
    add DWORD PTR [0x404000], 0x1337

; as -o l10.o l10.S && objcopy -O binary --only-section=.text ./l10.o ./l10.bin && cat ./l10.bin | /challenge/run