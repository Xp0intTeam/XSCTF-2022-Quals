#!/usr/bin/env python3

import random
import signal
import socketserver
import string
from hashlib import sha256
from os import urandom
from Crypto.Util.number import *
from gmpy2 import next_prime

flag = 'flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'


class Task(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def proof_of_work(self):
        random.seed(urandom(8))
        proof = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(16)])
        digest = sha256(proof.encode()).hexdigest()
        self.dosend('sha256(XXXX + {}) == {}'.format(proof[4:], digest) + "\n" + '@ XXXX=')
        x = self.request.recv(10)
        x = (x.strip()).decode('utf-8')
        if len(x) != 4 or sha256((x + proof[4:]).encode()).hexdigest() != digest:
            return False
        return True

    def dosend(self, msg):
        try:
            self.request.sendall(msg.encode('latin-1') + b'\n')
        except:
            pass

    def timeout_handler(self, signum, frame):
        raise TimeoutError

    def error(self):
        self.dosend("sorry!")
        self.request.close()

    def game1(self):
        p = getPrime(20)
        q = getPrime(20)
        e = 0x10001
        m = random.randint(0x10000, 0xfffff)
        c = pow(m, e, p * q)
        self.dosend("Welcome to game1" + "\n" + "The answer submitted should be hexadecimal strings like 0x1a23\n" + "# n=" + hex(p * q) + "\n" + "# e=" + hex(e) + "\n" + "# c=" + hex(
            c) + "\n" + "@ m=")
        rec_m = self.request.recv(1024).strip().decode('utf-8')
        if rec_m != hex(m):
            self.error()

    def game3(self):
        self.dosend("Welcome to game3. In this game should try 30 times and solve them")
        for i in range(30):
            p = getPrime(512)
            q = next_prime(p)
            e = 0x10001
            m = random.randint(0x100000000000, 0xffffffffffff)
            c = pow(m, e, p * q)
            self.dosend(
                "{} try".format(i + 1) + "\n" + "# n=" + hex(p * q) + "\n" + "# e=" + hex(e) + "\n" + "# c=" + hex(
                    c) + "\n" + "@ m=")
            rec_m = self.request.recv(1024).strip().decode()
            if rec_m == hex(m):
                continue
            else:
                self.error()

    def handle(self):
        try:
            signal.signal(signal.SIGALRM, self.timeout_handler)
            signal.alarm(50)
            if not self.proof_of_work():
                self.dosend('You must pass the PoW!')
                self.request.close()
            signal.alarm(300)

            self.game1()
            self.game3()
            
            self.dosend(flag)

        except TimeoutError:
            self.dosend('Timeout!')
            self.request.close()
        except:
            self.dosend('Wtf?')
            self.request.close()


class ThreadedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10001
    server = ThreadedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
    

