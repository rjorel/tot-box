    .globl  a2i_h
    .globl  a2i_1h


# Lit au clavier un nombre et le convertit en hexadecimal.

a2i_h:                      # Résultat dans eax.
    pushl   %ebx
    pushl   %edi
                
    xorl    %eax, %eax
    xorl    %ebx, %ebx
    
.a2i_h_loop:
    sall    $4, %ebx        # Décalage à droite de 4 bits.
    addl    %eax, %ebx      # Rajout du caractère lu.
    call    getchar
    
    movl    %eax, %edi
    call    a2i_1h
    
    cmpl    $0x10, %eax     # Boucle tant qu'on n'arrive pas sur un caractère fin.
    jnz     .a2i_h_loop
    
    movl    %ebx, %eax
    
    popl    %edi
    popl    %ebx
    
    ret


# Convertit un caractère ASCII en hexadécimal.                
    
a2i_1h:                         # Paramètre de transfert dans edi.
                                # Résultat dans eax.
    movl    %edi, %eax
    
    subl    $0x30, %eax         # eax < 0x30, eax mis à 0x10.
    jc      .a2i_h_else
    cmpl    $0xA, %eax          # 0x30 <= eax < 0x3A, on saute à la fin.
    jc      .a2i_h_exit
    
    subl    $0x07, %eax         # On retranche 0x07 pour que les caractères [0x41 - 0x46] correspondent aux caractères [0x0A - 0x0F].
    cmpl    $0xA, %eax          # 0x3A <= eax < 0x41, eax mis à 0x10.
    jc      .a2i_h_else
    cmpl    $0x10, %eax         # 0x41 <= eax < 0x47, on saute à la fin.
    jc      .a2i_h_exit
    
    cmpl    $0x2A, %eax         # 0x47 <= eax < 0x61, eax mis à 0x10
    jc      .a2i_h_else
    subl    $0x20, %eax         # On retranche de la même manière ici, pour que [0x61 - 0x66] correspondent aux [0x0A - 0x0F].
    cmpl    $0x10, %eax         # 0x61 <= eax < 0x67, on saute à la fin.
    jc      .a2i_h_exit
    
.a2i_h_else:
    movl    $0x10, %eax         # Si aucun saut n'est effectué, c'est que eax > 0x66 ou 0x47 <= eax < 0x57, ce n'est pas un caractère hexadécimal.
    
.a2i_h_exit:
    ret
