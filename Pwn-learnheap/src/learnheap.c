#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// extern void (*__free_hook) (void *__ptr,const void *);
size_t ** free_hook = (void*)((char*)(&system) - 0x47dc0 + 0x3dc8a8);
// size_t ** __free_hook = 0;

void check_free_hook(void * ptr, const void * y) {
    if(strcmp(ptr, "/bin/sh\x00")) {
       puts("Oh no. Where is your /bin/sh??");
       exit(0);
    }
}

void init() {
    setbuf(stdin, 0);
    setbuf(stderr, 0);
    setbuf(stdout, 0);
}

char *book[16];

void add() {
    int id, size;
    printf("id> ");
    scanf("%d", &id);
    if(id < 0 || id > 15) exit(0);
    printf("size> ");
    scanf("%d", &size);
    if(size < 0 || size > 0x430) exit(0);
    book[id] = malloc(size);
    printf("content> ");
    read(0, book[id], size);
    puts("Your book: ");
    puts(book[id]);
    puts("ok");
}

void show() {
    printf("what?");
}

void delete() {
    int id;
    printf("id> ");
    scanf("%d", &id);
    if(id < 0 || id > 15) exit(0);
    free(book[id]);
}

void Step1(){
    puts("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-");
    puts("Step 1. Leak Libc address.");
    puts("To leak libc address. we should use add() and show(), but?");
    puts("Something wrong. where is show() function?");
    puts("And where is libc address usually located?");
    add();
    add();
    delete();
    add();
    puts("Did you get Libc address? Let's make a test.");
    void *addr;
    scanf("%p", &addr);
    if(addr != &system) {
        hint:
        puts("Test fail. Try again?");
        puts("hints: \n\tdid you see the libc address in unsortbin?\n\tadd()? addAndshow()!");
        exit(0);
    }
    puts("Well Done!");
}

void Step2() {
    puts("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-");
    puts("Step 2. double free.");
    puts("To make double free, you should delete a chunk twice.");
    puts("Okokok, it will be very easy.");
    // add();
    delete();
    delete();
    delete();
    // delete();
    puts("Ok~,Let's make a test again.\nwhat sizes you make?");
    int size;
    scanf("%d", &size);
    if(size < 0 || size > 0x430) exit(0);
    void *p1 = malloc(size), *p2 = malloc(size), *p3=malloc(size);
    if(p1 != p3) {
        puts("Test fail. Try again?");
        puts("hints: \n\ttcachebin is easier to make double free.\n\tDo you remember some chunks you make in Step 1.?");
        exit(0);
    }
    puts("Well Done. I will put them back.");
    free(p3);
    free(p2);
    free(p1);
}
void Step3() {
    puts("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-");
    puts("Step 3. hijacking __free_hook");
    puts("Double free makes chunks like this:\n ->a->b->a->...");
    puts("To hijack __free_hook, you should make a chunk in __free_hook and Tamper with it.");
    add();
    add();
    add();
    add();
    if(!*free_hook) {
        puts("Test fail. Try again?");
        puts("hints: \n\tSize right?");
        exit(0);
    }
    puts("Well Done. let's get shell");
}
void Step4() {
    puts("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-");
    puts("Step 4. get shell!");
    puts("This is the final test. You shold do nothing. Just get shell.");
    
    if((size_t)*free_hook != (size_t)&system) {
        puts("Oh no. Where is your system funcion?");
        exit(0);
    }
    *free_hook = (void*)check_free_hook;
    delete();
    puts("Well Done. You got it!");
}

int main() {
    init();
    // printf("%p", __free_hook);
    char* p = malloc(0x20);
    puts("Welcome to LearnHeap!");
    puts("This is a guided learning test.");
    puts("In this test, gdb and pwndbg may help you.");
    puts("");
    puts("Now you will see a very regular heap question. add() show() delete()");
    puts("Step 1. Leak Libc address.\nStep 2. double free.\nStep 3. hijacking __free_hook\nStep 4. get shell!");
    puts("Now, let's start!");

    Step1();
    Step2();
    Step3();
    Step4();

    *free_hook = 0;
    // printf("%p", p-0x260);
    memset(p-0x250, 0, 0x240);
    for(int i = 0x430 / 0x10; i; i--) malloc(0x10);
    memset(book, 0, sizeof(book));

    puts("Now Let's attack.");
    
    while (1)
    {
        puts("Welcome~!\n1.add\n2.show\n3.delete");
        printf("> ");
        int ch;
        scanf("%d", &ch);
        switch (ch)
        {
        case 1: add();break;
        case 2: show();break;
        case 3: delete();break;
        default:
            puts("error.");
            break;
        }
    }
    
    
}