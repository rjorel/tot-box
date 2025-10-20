    .globl    main
    .globl    random
    .globl    display
    
t:
    .byte   0x20
    .byte   0x20
    .byte   0x2A
    .byte   0x20
    .byte   0x2A
    .byte   0x20
    .byte   0x20
    .byte   0x20
    .byte   0x2A
    .byte   0x2A
    .byte   0x2A
    .byte   0x2A
    .byte   0x2A
    .byte   0x20
    .byte   0x20
    .byte   0x2A
    .byte   0x20
    .byte   0x2A
    .byte   0x20
    .byte   0x2A
    .byte   0x20
    .byte   0x20
    .byte   0x2A
    .byte   0x2E
    .byte   0x2A
    .byte   0x2E
    .byte   0x2A
    .byte   0x20
    .byte   0x2A
    .byte   0x2A
    .byte   0x2A
    .byte   0x2A
    .byte   0x2A
    .byte   0x2A
    .byte   0x2A
    .byte   0x2A
    .byte   0x20
    .byte   0x2A
    .byte   0x20
    .byte   0x2A
    .byte   0x20
    .byte   0x2A

    
.LC0:
    .string     "clear"

.LC1:
    .string     "sleep 0.5"
    
    
main:
    pushl   %ebx
    pushl   %esi
    pushl   %edi
    
    subl    $4, %esp
    xorl    %ebx, %ebx
    
    movl    $0, (%esp)
    call    time
    movl    %eax, (%esp)
    call    srand

.L0:
    movl    $40, %edi
    call    random
    movl    %eax, %esi
    
    movl    $50, %edi
    call    random
    movl    %eax, %edi
    
    movl    $.LC0, (%esp)   # Ecran effacé entre chaque affichage.
    call    system

    call    display
    
    movl    $.LC1, (%esp)   # Temps d'attente entre chaque affichage.
    call    system
    
    addl    $1, %ebx
    cmpl    $20, %ebx
    jnz     .L0

    addl    $4, %esp
    popl    %edi
    popl    %esi
    popl    %ebx

    ret
    
    
random:                     # Nombre aléatoire, modulo le paramètre dans edi. Résultat dans eax.
    pushl   %edi
    call    rand
    
.L1:
    movl    $0, %edx
    divl    %edi
    cmpl    %edi, %eax
    jae     .L1
    
    movl    %edx, %eax
    popl    %edi
    
    ret


display:                    # Affichage du motif. y = esi, x = edi. ebx permet de se déplacer dans le tableau.
    pushl   %ebx
    pushl   %ebp
    pushl   %esi
    pushl   %edi
    
    subl    $4, %esp
    xorl    %ebx, %ebx
    
    movl    $0xA, (%esp)
    cmpl    $0, %esi        # Permet de positionner le motif sur l'axe des ordonnées.
    jz      .L3
    
.L2:
    call    putchar
    subl    $1, %esi
    jnz     .L2
        
.L3:
    
.loop_pattern:              # Affichage du motif, en prenant en compte le décalage sur l'axe des abscisses.
                            # ebx parcourt le tableau, tandis que ebp sert juste à savoir quand la ligne s'arrête
    movl    $0x20, (%esp)
    cmpl    $0, %edi
    jz      .L5
    movl    %edi, %esi

.L4:
    call    putchar
    subl    $1, %esi
    jnz     .L4
    
.L5:
    xorl    %ebp, %ebp      # Affichage des valeur du tableau sur une ligne, puis retour à la ligne.
    
.L6:                        
    push    t(%ebx)
    call    putchar
    addl    $4, %esp

    addl    $1, %ebx
    addl    $1, %ebp
    cmpl    $7, %ebp
    jnz     .L6

    movl    $0xA, (%esp)    # Retour à la ligne
    call    putchar

    cmpl    $42, %ebx       # Valeur maximale de ebx, le tableau fait 24 cases de 1 octet chacune.
    jnz     .loop_pattern
    
    addl    $4, %esp
    
    popl    %edi
    popl    %esi
    popl    %ebp
    popl    %ebx

    ret
