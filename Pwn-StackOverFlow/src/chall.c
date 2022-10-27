#include <stdio.h>

int count = 0;

void shell(){
    count++; 
    char buf[0x30]; //37
    //read(0,buf,0x40);
    gets(buf);
}

int main(){
    if (count == 1){
        return 0;
    }
    shell();
    return 0;
}