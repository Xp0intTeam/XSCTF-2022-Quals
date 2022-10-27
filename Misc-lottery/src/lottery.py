# -*- coding: UTF-8 -*-
import random
import os
import threading
import string
import time
import socket

random.seed(os.urandom(32))

flag = b'XSCTF{YOuR_ha^e_3arn3d_1O0_M1lLion_W0W_23j37si04kw}'
flagPrice = 10 ** 8
MAX_TICKET_PER_PERIOD = 20
MAX_RECEIVE_CONNECT = MAX_TICKET_PER_PERIOD + 1
TIME_QUERY = 0.2
PERSON_INIT_BUDGET = 10 ** 6
LOTTERY_INIT_BUDGET = 10 ** 8
HP = ("0.0.0.0", 9999)

assert MAX_RECEIVE_CONNECT >= MAX_TICKET_PER_PERIOD


def getWinningNumber():
    # tmp = tuple(map(lambda x: int(x, 16), hex(random.getrandbits(32))[2:]))
    return tuple(map(lambda x: int(x, 16), hex(random.getrandbits(32))[2:].rjust(8, '0')))


def proof_of_work():
    proof = os.urandom(32)


# 个人类，每一个接入的用户都会生成一个新的私有的person类
class person:
    def __init__(self):
        self.name = ""
        self.money = PERSON_INIT_BUDGET
        self.lotteryEarn = 0
        self.lotteryInfo = ""

    def buyTicket(self, ticket, money):
        money = int(money)
        if self.money < money:
            return None
        self.money -= money
        return lotteryOperator.buyLotteryTicket(ticket, money, self)

    def earn(self, m):
        self.money += m

    def buyFlag(self):
        if self.money < flagPrice:
            return b"Money? flag?", False
        else:
            return flag, True


# 公共的彩票管理类
class lottery:
    def __init__(self):
        self.currentAwardPool = LOTTERY_INIT_BUDGET
        self.lastAwardPool = 0
        self.lock = threading.Lock()
        self.period = 0
        self.ticketCache = []
        self.MAX_TICKET = MAX_TICKET_PER_PERIOD
        self.MAX_EARN = 10_000_000

    def buyLotteryTicket(self, ticket: tuple, money, p: person):
        """
        购买彩票的函数
        :param ticket: 长度为8的list，代表选择的数字
        :param money: 下注的金钱
        :param p: 回调的person类
        :return: 返回当前购买的期数
        """
        self.lock.acquire()

        # print(len(self.ticketCache))
        self.ticketCache.append((ticket, money, p))
        self.lastAwardPool += money
        period = self.period

        # 当本期购买彩票的人数达到MAX_TICKET时候就开奖
        if len(self.ticketCache) >= self.MAX_TICKET:
            wn = getWinningNumber()
            firstPrize = []
            allMoney = 0
            for t, m, p in self.ticketCache:
                if t == wn:
                    firstPrize.append((p, m))
                    allMoney += m
                elif any(map(lambda i: t[i] == wn[i], range(len(t)))):
                    p.lotteryEarn += m

            spentPool = 0
            firstPrizeAward = min(self.MAX_EARN, self.currentAwardPool / allMoney) if allMoney else 0
            firstPrizeInfo = []
            for p, m in firstPrize:
                tmp = firstPrizeAward * m
                p.lotteryEarn += tmp
                spentPool += tmp
                firstPrizeInfo.append(p.name)

            sInfo = ' / '.join(firstPrizeInfo)
            for t, m, p in self.ticketCache:
                p.lotteryInfo = f"Period: {self.period}\nWinning Number: {wn}\nFirst Prize Winner: {sInfo}"
            self.currentAwardPool -= spentPool
            self.currentAwardPool += self.lastAwardPool
            self.lastAwardPool = 0
            self.ticketCache = []
            self.period += 1

        self.lock.release()
        return period

    def getPeriodInfo(self):
        return f"Period {self.period} Award Pool: {self.currentAwardPool}$ " \
               f"Participants: {len(self.ticketCache)}/{self.MAX_TICKET}".encode('utf-8')

    def query(self, period):
        if period == self.period:
            return False, self.getPeriodInfo()
        elif period < self.period:
            return True, b""
        else:
            return None, b"Error"


lotteryOperator = lottery()


def game(conn: socket.socket, addr):
    """
    游戏的主要函数，彩票由8个[0,15]的数字构成，输入的时候空格间隔隔开
    :param conn:
    :param addr:
    :return:
    """
    print(addr)
    p = person()
    conn.send(f'Welcome to Lottery Play!\n'
              f'Lottery rules: Each lottery ticket can select 8 numbers in order, with each number ranging from 0 '
              f'to 15. A total of {MAX_TICKET_PER_PERIOD} tickets will be sold in each lottery, and prizes will be '
              f'awarded immediately when the number of tickets sold reaches.\n'
              f'you need to earn {flagPrice}$ to buy the flag.\n'.encode())
    conn.send(b"Your Name> ")
    name = conn.recv(0x20).decode('utf-8')
    p.name = name
    while True:
        conn.send(f"Your Money: {p.money}$\n".encode())
        conn.send(b'1.Lottery\n2.Earn\n3.Buy flag\n> ')
        ch = int(conn.recv(5).decode())
        if ch == 1:
            conn.send(lotteryOperator.getPeriodInfo() + b'\n')
            conn.send(b"Your Ticket(Space interval)> ")
            t = list(map(int, conn.recv(128).decode('utf-8').strip().split())) + [-1] * 8
            t = tuple(t[:8])
            conn.send(b"Your Spend> ")
            m = int(conn.recv(0x20).decode('utf-8'))
            m = max(1, abs(m))
            period = p.buyTicket(t, m)
            if period is None:
                conn.send(b"Error not enough money\n")
                continue
            while True:
                test, info = lotteryOperator.query(period)
                conn.send(info + b'\n')
                if test:
                    break
                time.sleep(TIME_QUERY)
            conn.send(f"Your win {p.lotteryEarn}\n{p.lotteryInfo}\n".encode('utf-8'))
            p.earn(p.lotteryEarn)
            p.lotteryEarn = 0
            p.lotteryInfo = ''
        elif ch == 3:
            flagTmp, tmp = p.buyFlag()
            conn.send(flagTmp + b'\n')
            if tmp:
                break


def startService(conn, addr):
    try:
        game(conn, addr)
    except Exception as e:
        pass

if __name__ == '__main__':
    # sem = threading.Semaphore(MAX_RECEIVE_CONNECT) # 线程通信量，最大限制MAX_RECEIVE_CONNECT个
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # 流式Socket
        print("Start", HP)
        s.bind(HP)
        s.listen(5)
        while True:
            conn, addr = s.accept()
            threading.Thread(target=startService, args=(conn, addr)).start()

        # while True:
        #     threading.Thread(target=startService, args=(s, )).start()
