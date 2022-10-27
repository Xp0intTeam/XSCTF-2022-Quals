from Crypto.Util.number import GCD
from string import ascii_letters, digits, punctuation
from random import randint
from sercet import pwd

#pwd = "pwd{**********************************}"

def encrypt(x, a, b): return a*x+b

def keyGen(n):
    a = [randint(1, 94) for _ in range(4)]
    b = [randint(1, 94) for _ in range(4)]
    while GCD(n, a[0]*a[1]*a[2]) != 1:
        a = [randint(1, 94) for _ in range(4)]
    return a, b

table = ascii_letters+digits+punctuation
n = len(table)
A, B = keyGen(n)
c = "".join([table[encrypt(encrypt(encrypt(encrypt(table.find(x),A[0], B[0]), A[1], B[1]), A[2], B[2]), A[3], B[3]) % n] for x in pwd])
with open("cipher",'w') as f:
    print(c,file=f)