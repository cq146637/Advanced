__author__ = 'Cq'
"""
    装饰器类实现
"""
from types import MethodType


class NCalls(object):
    def __init__(self, func):
        self.func = func
        self._ncalls = 0

    def __call__(self, *args, **kargs):
        print('in __call__')
        self._ncalls += 1
        return self.func(*args, **kargs)

    def __get__(self, instance, cls):
        return MethodType(self, instance, cls)

    def ncalls(self):
        return self._ncalls

    def reset(self):
        self._ncalls = 0

@NCalls
def f():
    print('in f')


class A(object):
    @NCalls
    def g(self):
        print('in A::g', self)

    def h(self):
        print('in A::h', self)


if __name__ == '__main__':
    f = NCalls(f)
    f()
    f()
    f()

    print(f.ncalls())

    # a = A()
    # a.g()
    # a.g()
    # a.g()
    # a.g()
    # print(a.g.ncalls())

