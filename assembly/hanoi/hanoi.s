    .globl  main
    .globl  hanoi
    

main:
    pushl   %ebp
    pushl   %esi
    pushl   %edi
    pushl   %ebx
    
    movl    $4, %edi
    movl    $1, %ebp
    movl    $2, %esi
    movl    $3, %ebx
    
    call    hanoi    
    
    popl    %ebx
    popl    %edi
    popl    %esi
    popl    %ebp
    
    ret
    
    
hanoi:                      # n: edi, d: ebp, i: esi, a: ebx
    cmpl    $0, %edi
    jz      .hanoi_exit

    movl    %esi, %eax      # i <-> a; esi <-> ebx
    movl    %ebx, %esi      # a: esi
    movl    %eax, %ebx      # i: ebx
    subl    $1, %edi
    call    hanoi           # hanoi(n - 1, d, a, i)
    
    addl    $1, %edi
    call    deplace         # deplace(n, d, a)
    
    movl    %ebx, %eax      # d -> a -> i, i -> d; ebp -> esi -> ebx, ebx -> ebp
    movl    %esi, %ebx      # a: ebx
    movl    %ebp, %esi      # d: esi
    movl    %eax, %ebp      # i: ebp
    subl    $1, %edi
    call    hanoi           # hanoi(n - 1, i, d, a)

    movl    %ebp, %eax      # i <-> d; ebp <-> esi
    movl    %esi, %ebp      # d: ebp
    movl    %eax, %esi      # i: esi
    addl    $1, %edi
    
.hanoi_exit:

    ret
    
    
deplace:                    # n: edi, d: ebp, a: esi
    pushl   %edi

    pushl   $'n'
    call    putchar
    
    pushl   $':'
    call    putchar
    
    pushl   $' '
    call    putchar

    call    i2a_h           # n

    pushl   $'d'
    call    putchar
    
    pushl   $':'
    call    putchar
    
    pushl   $' '
    call    putchar

    movl    %ebp, %edi
    call    i2a_h           # d

    pushl   $'a'
    call    putchar
    
    pushl   $':'
    call    putchar
    
    pushl   $' '
    call    putchar

    movl    %esi, %edi
    call    i2a_h           # a
    
    pushl   $0xA
    call    putchar
    
    addl    $40, %esp
    
    popl    %edi
    ret