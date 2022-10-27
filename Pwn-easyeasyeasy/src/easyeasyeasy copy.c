
#include<stdio.h>

const int p = 38;

void init(){
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

int main() {
    int fd = open("./flag");
    char flag[0x100];
    read(fd, flag, p);
    read(0, flag+p, 2*p);
    for(int i = 0; i < 2*p; ++i) {
        int tmp = rand() % (2*p);
        flag[i] ^= flag[i] ^ flag[tmp];
        flag[i] ^= flag[i] ^ flag[tmp];
        flag[i] ^= flag[i] ^ flag[tmp];
    }
    
}