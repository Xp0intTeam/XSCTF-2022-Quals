#!/usr/bin/env python3

import random
import signal
import socketserver
import string
from hashlib import sha256
from os import urandom
from Crypto.Cipher import AES

flag = b'flag{xxxxxxxxxxxxxxxxxxxxxxxxxx}'
BLOCK_SIZE = 16

def pad(m):
    if len(m) % BLOCK_SIZE != 0:
        m += b'\x00' * (BLOCK_SIZE - len(m) % BLOCK_SIZE)
    return m

pad(flag)
part_flag = [flag[i:i + BLOCK_SIZE] for i in range(0, len(flag), BLOCK_SIZE)]

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

    def keyGen(self):
        key = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(16)])
        return key.encode()

    def encrypt(self):
        self.dosend("Enter HEXADECIMAL message:")
        m = self.receive().decode().strip()
        m = pad(bytes.fromhex(m))
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.IV)
        c = cipher.encrypt(m)
        self.dosend("This is your cipher")
        self.dosend(c.hex())

    def decrypt(self):
        self.dosend("Enter HEXADECIMAL cipher:")
        c = self.receive().decode().strip()
        c = pad(bytes.fromhex(c))
        cipher = AES.new(self.key, AES.MODE_CBC, iv=self.IV)
        m = cipher.decrypt(c)
        self.dosend("This is your message")
        self.dosend(m.hex())


    def selectIV(self):
        while True:
            self.dosend("Which part of flag do you want to choose?")
            part = self.receive().decode().strip()
            try:
                part = int(part)
                assert 0 <= part < len(part_flag)
                return part_flag[part]
            except:
                continue


    def handle(self):
        try:
            signal.signal(signal.SIGALRM, self.timeout_handler)
            signal.alarm(50)
            if not self.proof_of_work():
                self.dosend('You must pass the PoW!')
                self.request.close()
            signal.alarm(300)

            self.key = self.keyGen()
            self.IV = self.selectIV()
            while True:
                self.dosend("1: Encrypt")
                self.dosend("2: Decrypt")
                self.dosend("3: ChangeIV")
                self.dosend("4: Give up")
                choice = self.receive().decode()
                if choice == "1":
                    self.encrypt()
                elif choice == "2":
                    self.decrypt()
                elif choice == "3":
                    self.IV = self.selectIV()
                elif choice == "4":
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
    HOST, PORT = '0.0.0.0', 10002
    server = ThreadedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
    

