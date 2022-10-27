all: club
club: club.c
	gcc -fno-stack-protector -z now -fomit-frame-pointer -o club club.c
	strip --remove-section=.symtab club
	strip --remove-section=.strtab club

clean:
	rm club
