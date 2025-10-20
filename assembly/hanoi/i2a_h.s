    .globl  i2a_h
    .globl  i2a_1h


# Ecrit à l'écran le nombre hexadécimal

i2a_h:                      # Paramètre de transfert dans edi.
    pushl   %ebp
    pushl   %ebx
    pushl   %edi

    movl    %edi, %ebp
    movl    $8, %ebx        # Boucle 8 fois.

.i2a_h_loop:
    shrl    $28, %edi
    call    i2a_1h

    pushl   %eax            # Affichage du caractère.
    call    putchar
    addl    $4, %esp

    sall    $4, %ebp
    movl    %ebp, %edi

    subl    $1, %ebx
    jnz     .i2a_h_loop

    movl    $0xA, %eax      # Retour à la ligne.
    pushl   %eax
    call    putchar
    addl    $4, %esp

    popl    %edi
    popl    %ebx
    popl    %ebp

    ret

# Convertit un chiffre hexadécimal sur 4 bits en son code ASCII.

i2a_1h:                     # Paramètre de transfert dans edi.
                            # Résultat dans eax.
    movl    %edi, %eax
    andl    $0xF, %eax

    addl    $0x30, %eax
    cmpl    $0x3A, %eax
    jc      .i2a_h_exit

    addl    $0x7, %eax

.i2a_h_exit:
    ret