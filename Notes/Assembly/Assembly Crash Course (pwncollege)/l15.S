.global _start
.intel_syntax

_start:
    push %rdi
    push %rsi
    pop %rdi
    pop %rsi

; as -o l15.o l15.S && objcopy -O binary --only-section=.text ./l15.o ./l15.bin && cat ./l15.bin | /challenge/run