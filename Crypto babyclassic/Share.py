#!/usr/bin/env python3

import random
import signal
import socketserver
import string
from hashlib import sha256
from os import urandom
from Crypto.Util.number import bytes_to_long
from secret import flag, pwd1, pwd2, pwd3, pwd4

secret = bytes_to_long(flag)
FIELD_SIZE = secret


def coefficient(t, secret):
    coeff = [random.randrange(1, FIELD_SIZE)]
    if t > 2:
        coeff += [random.randrange(0, FIELD_SIZE) for _ in range(t - 2)]
    coeff.append(secret)
    return coeff


def fx(x, coeff):
    y = 0
    for coeff_index, coeff_value in enumerate(coeff[::-1]):
        y += x ** coeff_index * coeff_value
    return y


def sercet_shares(t, n, secret):
    coeff = coefficient(t, secret)
    shares = []
    for x in range(1, n + 1):
        shares.append((x, fx(x, coeff)))
    return shares


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

    def dosend(self, msg, newline=True):
        try:
            string = msg.encode('latin-1')
            if newline:
                string = string + b"\n"
            self.request.sendall(string)
        except:
            pass

    def receive(self, prompt=">> "):
        self.dosend(prompt, newline=False)
        return self.request.recv(2048).strip()

    def timeout_handler(self, signum, frame):
        raise TimeoutError

    def error(self):
        self.dosend("sorry!")
        self.request.close()

    def handle(self):
        try:
            signal.signal(signal.SIGALRM, self.timeout_handler)
            signal.alarm(50)
            if not self.proof_of_work():
                self.dosend('You must pass the PoW!')
                self.request.close()
            signal.alarm(300)

            self.shares = sercet_shares(3, 4, secret)

            while True:
                self.dosend("1: Alice")
                self.dosend("2: Bob")
                self.dosend("3: Charlie")
                self.dosend("4: Dave")
                self.dosend("5: GoodBye")
                choice = self.receive().decode()
                if choice == "1":
                    self.dosend("Give me Alice's password")
                    pwd = self.receive().decode()
                    if pwd != pwd1:
                        self.error()
                    self.dosend(str(self.shares[0]))
                elif choice == "2":
                    self.dosend("Give me Bob's password")
                    pwd = self.receive().decode()
                    if pwd != pwd2:
                        self.error()
                    self.dosend(str(self.shares[1]))
                elif choice == "3":
                    self.dosend("Give me Charlie's password")
                    pwd = self.receive().decode()
                    if pwd != pwd3:
                        self.error()
                    self.dosend(str(self.shares[2]))
                elif choice == "4":
                    self.dosend("Give me Dave's password")
                    pwd = self.receive().decode()
                    if pwd != pwd4:
                        self.error()
                    self.dosend(str(self.shares[3]))
                elif choice == "5":
                    self.dosend("88")
                    self.request.close()

        except TimeoutError:
            self.dosend('\nTimeout!')
            self.request.close()
        except:
            self.dosend('Wtf?')
            self.request.close()


class ThreadedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10006
    server = ThreadedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
    

