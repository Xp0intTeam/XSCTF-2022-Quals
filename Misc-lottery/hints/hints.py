# -*- coding: UTF-8 -*-
from pwn import *
import threading
import time
import randcrack
import sys

rc = {}


def f(t):
    return int(''.join(map(lambda x: f"{x:x}", t)), 16)


def getWinningNumber(xt):
    return tuple(map(lambda x: int(x, 16), hex(xt)[2:].rjust(8, '0')))


class person:
    def __init__(self, personName, host, port):
        self.money = 0
        self.name = personName
        self.io = remote(host, port)
        self.io.sendlineafter('Your Name> ', self.name)
        self.hp = (host, port)

    def updateMoney(self):
        self.io.recvuntil("Your Money: ")
        self.money = float(self.io.recvuntil('$', drop=True).decode())

    def buyTicket(self, ticket, money):
        self.io.sendlineafter("> ", "1")
        self.io.sendlineafter('Your Ticket(Space interval)> ', ' '.join(map(str, ticket)))
        self.io.sendlineafter('Your Spend> ', str(money))

    def waitForResult(self, save=1, Max_wait=300):
        while True and Max_wait:
            Max_wait -= 1
            tmp = self.io.recvuntil('\n').decode()
            if 'win' in tmp:
                break
            if "Error" in tmp:
                return False
            log.debug(self.name + " " + tmp)
        if not save:
            return True
        self.io.recvuntil("Period: ")
        period = int(self.io.recvuntil('\n', drop=True).decode())
        self.io.recvuntil('Winning Number: ')
        number = f(eval(self.io.recvuntil('\n', drop=True).decode()))
        if period not in rc:
            rc[period] = number
        return True

    def buyFlag(self):
        self.io.sendlineafter("> ", "3")
        log.success(self.name.encode() + b" " + self.io.recvuntil('\n'))

    def remake(self):
        self.io.close()
        self.io = remote(*self.hp)
        self.io.sendlineafter('Your Name> ', self.name)


context.log_level = 'debug'
stat_time = time.time()
host = "0.0.0.0"
port = 1234

p = person("test", host, port)
for i in range(3):
    p.updateMoney()
    p.buyTicket((1, 2, 3, 4, 5, 6, 7, 8), 10000)
    if not p.waitForResult():
        p.remake()
