#include<stdio.h>
#include<stdlib.h>
#include<string.h>

extern void (*__free_hook) (void *__ptr,const void *);

int main() {
        char *str = malloc(160);
        strcpy(str,"/bin/sh");

        printf("__free_hook: %p\n",__free_hook);

        // 劫持__free_hook

        puts(" __free_hook abduction");
        __free_hook = (void*)system;

        free(str);
        printf("__free_hook: %p\n",__free_hook);
        return 0;
}