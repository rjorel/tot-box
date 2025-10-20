    .globl  t
    .data
    
t:
    .long   0
    .long   1
    .long   2
    .long   3
    .long   4
    .long   5
    .long   6
    .long   7
    
    .text
    .globl  main
    .globl  sum

    
main:
    pushl   %edi
    pushl   %esi
    
    movl    $8, %edi
    movl    $t, %esi
    call    sum
    
    movl    %eax, %edi
    call    i2a_h
    
    popl    %esi
    popl    %edi
    
    ret



sum:                    # Paramètres : edi -> taille du tableau, esi -> pointeur sur tableau.                
    pushl   %ebx
    cmpl    $2, %edi
    jnz     .L2

    movl    (%esi), %edx    
    movl    4(%esi), %eax
    addl    %edx, %eax      # eax = esi[0] + esi[1]
    jmp     .L3

.L2:
    shrl    $1, %edi        # edi /= 2
    call    sum
    
    movl    %eax, %ebx
    
    leal    (%esi, %edi, 4), %esi    # Calcul de l'adresse du milieu de tableau
    call    sum
    
    addl    %ebx, %eax

    shll    $1, %edi     # Rétablissement des valeurs initiales de edi et esi
    subl    %edi, %esi
    subl    %edi, %esi
    
.L3:
    popl    %ebx

    ret
