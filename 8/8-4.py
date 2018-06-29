__author__ = 'Cq'
"""
    实现属性可修改的函数装饰器
"""

"""
    实例：
        分析程序内哪些函数执行时间开销较大，
        我们定义一个带timeout参数的函数装饰器能实现，
        统计被装饰函数单次调用运行时间，
        时间大于参数timeout的，将此次函数调用记录到log日志中，
        运行参数可修改timeout的值
"""
from functools import wraps
from random import randint
import time
import logging


def warn(timeout):
    timeout = [timeout]
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kargs):
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout[0]:
                msg = '"%s": %s > %s' % (func.__name__, used, timeout[0])
                logging.warn(msg)
            return res
        def setTimeout(k):
            # nonlocal 访问嵌套作用域中的变量
            # nonlocal timeout timeout = k python3
            timeout[0] = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator


if __name__ == '__main__':
    @warn(1.5)
    def test():
        print('In test')
        while randint(0, 1):
            time.sleep(0.5)

    for _ in range(30):
        test()

    test.setTimeout(1)
    for _ in range(30):
        test()