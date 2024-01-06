.global _start
.intel_syntax

_start:
    pop %rdx
    sub %rdx, %rdi
    push %rdx

; as -o l14.o l14.S && objcopy -O binary --only-section=.text ./l14.o ./l14.bin && cat ./l14.bin | /challenge/run