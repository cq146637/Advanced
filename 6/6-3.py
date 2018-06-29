"""
    让对象支持上下文管理
"""
from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque


class TelnetClient(object):
    """
        使得对象在我们不需要的时候，或者执行完某以语句后，自动被回收
        实现上下文管理协议，需要定义实例的__enter__,__exit__方法
        它们分别在with开始和结束时被调用
    """

    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):
        # user
        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]): t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput) + 1:])

    def __enter__(self):
        # with TelnetClient('127.0.0.1') 执行
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        # 返回值作为 as 后的 client 对象
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tn.close()
        self.tn = None
        with open(self.addr  + 'history.txt', 'w') as f:
            f.writelines(self.history)



if __name__ == '__main__':
    with TelnetClient('127.0.0.1') as client:
        client.start()
