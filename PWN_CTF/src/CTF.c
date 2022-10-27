#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>
#include <math.h>
#define BUFSIZE 64

//challenge 1 是利用pwntools的简单数学题
//challenge 2 是利用数组索引的
//challenge 3 格式化字符串泄露金丝雀，达成利用

int FLAG = 0;


void init() {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}
int getshell()
{
    if (FLAG ==  1){
    puts("But not you!");
    puts("You get the food!");
    puts("Great Job!You finish all challenges!");
    
    return execv("/bin/sh",NULL);
    }
    else{
      printf("You Don't follow the route!\n");
      return 0;
    }
  
}

void challenge1(){
  unsigned int seed;
  int iter = 50;
  int num1;
  int num2;
  int result=0;
  int answer=0;
  char sign[4] = {'+','-','*','/'};
  char true_sign;
  printf("Here is your first challenge\n");
  printf("50 easy math question\n");
  srand(seed);
  for(int i = 1 ; i<=iter;++i)
  {
    num1 = rand()%600;
    num2 = rand()%600+10;
    true_sign = sign[rand()%4];
    char buf[8];
    switch (true_sign)
    {
    case '+':
        result = num1 + num2;
        break;
    
    case '-':
        result = num1 - num2;
        break;
      case '*':
        result = num1 * num2;
        break;
      case '/':
        result = num1 / num2;
        break;
    }
    printf("num1:%d,num2:%d\n",num1,num2);
    printf("operator:%c\n",true_sign);
    printf("Your answer is: ");
    read(0,buf,8uLL);
    answer = strtol(buf,0LL,10);
    if (answer!=result)
    {
        printf("Huh?That's what You get?\n");
        exit(0);
    }
    printf("Right!Next one\n");
    printf("%d Left\n",iter-i);
    sleep(0);
  }
  printf("Great Job!\n");
  return  ;
}

void challenge2(){
    int i;
    __int64_t s[12];
    __int64_t num1,num2;
    memset(s, 0, 0x50uLL);
    puts("Here is your Second challenge");
    puts("You are very hugry now");
    puts("Someone comes and says : \n'Today is CTF(Crazy Thursday Festival),tell me a secret about stack.Then I will v you 50 yuan'");
    puts("Your answer: ");
    scanf("%lld",&num1);
    puts("Someone : 'I don't like this one.Have any else?'");
    puts("Your answer: ");
    scanf("%lld",&num2);
    if ( num1 > 2 )
      exit(0);
    s[num1] = num2;
    puts("Someone : 'OK, I give you what you deserve");
    puts("Then you go into the KFC");
    puts("You look up your wechat wallet");
    if (s[12] ==1)
        challenge3();
    return ;
}
void challenge3(){
    int i;
    char buf[0x80];
    printf("It shows: 50!!!\n");
    printf("staff : 'what is your payment password?'\n");
    puts("Your answer: ");
    read(0,buf,0x150uLL);
    printf(buf);
    puts("staff : 'Thank you! Just wait a minute'\n");
    for (i = 0 ;i<=2;++i)
        printf("...\n");
        sleep(1);
    puts("10 minutes after\n");
    puts("staff: 'Because many fans of Genshin Impact from the Pizza Hut also ordered dishes here.'\n");
    puts("       'We need you to show your Pick-up-Code'\n");
    puts("Your answer: ");
    read(0,buf,0x150uLL);
    puts("one of fans: 'Someone steals my food! My friends ,help me to find out who it is!'\n");
    puts("Quickly, you are surrounded.\n");
    FLAG = 1;
    return 0;
}

void main(){
  asm("jz label1");
  asm("jnz label1");
  asm __volatile__ (".byte 0x12");
  asm("label1:");   

  init();
  int (*pf)();
  pf = getshell;
  printf("Hey,Welcome to the road of Pwn\n");
  printf("To ensure you have the ability to go on,\n");
  printf("There are 3 challenge waitting for you.\n");
  printf("Please finish all of them in 30 seconds\n");
  printf("and tell you a secret %p\n",pf);
  printf("Good Luck!\n");
  alarm(0x42u);
  challenge1();
  challenge2();
  printf("It shows: 0!!!\n");
  printf("Where is your 50 yuan?!\n");
  printf("Finally, you are fainted from hunger\n");
  return 0;
}
