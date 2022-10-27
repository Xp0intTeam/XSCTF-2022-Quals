#include<stdio.h>

void init(){
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

int main() {
    init();
    char map[256] = {0};
    short p;
    printf("you>");
    scanf("%d", &p);
    if(map[p % 256]) system("/bin/sh");
}
