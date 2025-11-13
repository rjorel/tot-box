#include <stdio.h>
#include <stdlib.h>

int data = 1, bss;

int f(int *a) {
    int b;
    return (a - &b);
}

int main() {
    int stack;
    void *heap = malloc(1);

    printf("code: %p, data: %p, bss: %p, stack: %p, heap: %p\n", &main, &data, &bss, &stack, heap);

    int a;
    printf("stack direction: %s\n", f(&a) > 0 ? "down" : "up");

    free(heap);

    return 0;
}