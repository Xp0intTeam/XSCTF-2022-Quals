#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/prctl.h>
#include <linux/filter.h>
#include <seccomp.h>
const char text[] = "ZjFhZ3tYU0NURi0yMDIyLWdvLWdvLWdvfQ==";
char invitation_code[32];

void gift() {
    asm("syscall");
    asm("mov $10, %rdx");
}

void initial() {
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
}

void sandbox(void) {
    prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0);
    struct sock_filter sfi[] = {
        {0x20, 0x00, 0x00, 0x00000004},
        {0x15, 0x00, 0x0e, 0xc000003e},
        {0x20, 0x00, 0x00, 0x00000000},
        {0x35, 0x00, 0x01, 0x40000000},
        {0x15, 0x00, 0x0c, 0xffffffff},
        {0x15, 0x0b, 0x00, 0x0000003b},
        {0x15, 0x0a, 0x00, 0x00000142},
        {0x15, 0x09, 0x00, 0x00000039},
        {0x15, 0x08, 0x00, 0x00000038},
        {0x15, 0x07, 0x00, 0x0000000f},
        {0x15, 0x06, 0x00, 0x00000009},
        {0x15, 0x05, 0x00, 0x0000000a},
        {0x15, 0x04, 0x00, 0x00000029},
        {0x15, 0x00, 0x02, 0x00000001},
        {0x20, 0x00, 0x00, 0x00000010},
        {0x15, 0x01, 0x00, 0x00000002},
        {0x06, 0x00, 0x00, 0x7fff0000},
        {0x06, 0x00, 0x00, 0x00000000}
    };
    struct sock_fprog sfp = {18, sfi};
    prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &sfp);
}

void display() {
    putchar('\n');
    write(1, " \x1B[0;1;35;95m░█\x1B[0;1;31;91m░█\x1B[0;1;33;93m░█\x1B[0;1;32;92m▀▀\x1B[0;1;36;96m░░\x1B[0;1;34;94m░█\x1B[0;1;35;95m▀▀\x1B[0;1;31;91m░█\x1B[0;1;33;93m░░\x1B[0;1;32;92m░█\x1B[0;1;36;96m░█\x1B[0;1;34;94m░█\x1B[0;1;35;95m▀▄\x1B[0m\n", 241);
    write(1, " \x1B[0;1;31;91m░▄\x1B[0;1;33;93m▀▄\x1B[0;1;32;92m░▀\x1B[0;1;36;96m▀█\x1B[0;1;34;94m░░\x1B[0;1;35;95m░█\x1B[0;1;31;91m░░\x1B[0;1;33;93m░█\x1B[0;1;32;92m░░\x1B[0;1;36;96m░█\x1B[0;1;34;94m░█\x1B[0;1;35;95m░█\x1B[0;1;31;91m▀▄\x1B[0m\n", 240);
    write(1, " \x1B[0;1;33;93m░▀\x1B[0;1;32;92m░▀\x1B[0;1;36;96m░▀\x1B[0;1;34;94m▀▀\x1B[0;1;35;95m░░\x1B[0;1;31;91m░▀\x1B[0;1;33;93m▀▀\x1B[0;1;32;92m░▀\x1B[0;1;36;96m▀▀\x1B[0;1;34;94m░▀\x1B[0;1;35;95m▀▀\x1B[0;1;31;91m░▀\x1B[0;1;33;93m▀░\x1B[0m\n", 240);
    putchar('\n');
}

char* cipher(char input_str[]) {
    int len_str = strlen(input_str);
	char char_set[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
	char *res_str = (char *) malloc(1000 * sizeof(char));
	int index, no_of_bits = 0, padding = 0, val = 0, count = 0, temp;
	int i, j, k = 0;
	for (i = 0; i < len_str; i += 3)
		{
			val = 0, count = 0, no_of_bits = 0;
			for (j = i; j < len_str && j <= i + 2; j++)
			{
				val = val << 8;
				val = val | input_str[j];
				count++;
			}
			no_of_bits = count * 8;
			padding = no_of_bits % 3;
			while (no_of_bits != 0)
			{
				if (no_of_bits >= 6)
				{
					temp = no_of_bits - 6;
					index = (val >> temp) & 63;
					no_of_bits -= 6;
				}
				else
				{
					temp = 6 - no_of_bits;
					index = (val << temp) & 63;
					no_of_bits = 0;
				}
				res_str[k++] = char_set[index];
			}
	}
	for (i = 1; i <= padding; i++)
	{
		res_str[k++] = '=';
	}
	res_str[k] = '\0';
	return res_str;
}

void do_read(char *str, int size) {
    read(0, str, size);
    for (int i = 0; i < size; i++) {
        if (str[i] == '\n') {
            str[i] = '\x00';
            break;
        }
    }
}

void club() {
    char phone_number[0x18];
    char name[8];
    write(1, "Hey, this is XS-Club, your name?\n", 33);
    do_read(name, 8);
    printf("Okay, %s\n", name);
    write(1, "Please show me your invitation code\n", 36);
    do_read(invitation_code, 32);
    if (strcmp(cipher(invitation_code), text)) {
        write(1, "OUT 0UT OUT!!! (ノ｀⊿´)ノ\n", 32);
        exit(0);
    }
    write(1, "Good, just leave your phone number here\n", 40);
    gets(phone_number);
    write(1, "Well done~\nNow you can join the club, go crazy!!! *\\(^o^)/*\n", 60);
    close(0);
    close(1);
}

int main() {
    initial();
    sandbox();
    display();
    club();
}
