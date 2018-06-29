__author__ = 'Cq'
"""
    函数装饰器的使用
"""


def memo(func):
    cache = {}
    def wrap(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrap


@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

@memo
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count


if __name__ == '__main__':
    print(fibonacci(50))
    print(climb(10, (1, 2, 3)))