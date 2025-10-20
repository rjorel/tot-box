    .globl    a2i_d
    .globl    a2i_1d
    

# Lit au clavier un nombre et le convertit en decimal.
    
a2i_d:
    pushl   %ebx
    pushl   %edi
    
    xorl    %eax, %eax
    xorl    %ebx, %ebx
    
.a2i_d_loop:
    movl    %ebx, %ecx
    sall    $3, %ebx
    addl    %ecx, %ebx
    addl    %ecx, %ebx
    addl    %eax, %ebx
    call    getchar
    movl    %eax, %edi
    call    a2i_1d
    
    cmpl    $0x10, %eax
    jnz     .a2i_d_loop
    
    movl    %ebx, %eax

    popl    %edi
    popl    %ebx

    ret


# Convertit un caractère ASCII en décimal.
    
a2i_1d:
    movl    %edi, %eax
    
    subl    $0x30, %eax
    jc      .a2i_d_else
    cmpl    $0xA, %eax
    jc      .a2i_d_exit
    
.a2i_d_else:
    movl    $0x10, %eax
    
.a2i_d_exit:
    ret
