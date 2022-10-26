#include <stdio.h>
#include <unistd.h>

/* https://zhuanlan.zhihu.com/p/74949252 */
const char *flag = "0123456789abcdef"; // fake flag

int _strcmp(const char *s1, const char *s2){
	int l = strlen(s2);
	for(int i = 0; i<=l; i++){
		if(*(s1+i) != *(s2+i)) return 0;
		usleep(100000);
	}
	return 1;
}

int main(){
	char buf[0x10] = {0};
	printf("input your flag: ");
	scanf("%15s", buf);
	if(_strcmp(buf)) printf("Here is your flag: flag{%s}\n", buf);
	else printf("Sorry, try again~\n");
	return 0;
}
