"""
    使用生成器函数实现可迭代类
"""
import math


class PrimeNumbers(object):
    """
        实现正向迭代
        实现 __iter__ 或 __getitem__ 方法
        实现反向迭代
        实现 __reversed__ 方法
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isParimeNum(self, k):
        if k < 2:
            return False

        for i in range(2,int(math.sqrt(k) + 1)):
            if k % i == 0:
                return False

        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isParimeNum(k):
                yield k

    def __reversed__(self):
        for k in range(self.end, self.start - 1, -1):
            if self.isParimeNum(k):
                yield k


def main():
    for i in PrimeNumbers(1, 10):
        print(i)

    for i in reversed(PrimeNumbers(1, 10)):
        print(i)


if __name__ == '__main__':
    main()