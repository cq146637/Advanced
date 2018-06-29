__author__ = 'Cq'
"""
    定义带参数的装饰器
"""

"""
    实现：
        用来检查被装饰函数的参数类型
        装饰器可以通过参数指明函数参数的类型
        调用时，如果检测出不匹配则抛出异常
"""
from inspect import signature


def typeassert(*ty_args, **ty_kargs):
    def decorator(func):
        # func -> a,b
        # d = {'a': int, 'b': str}
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments
        def wrapper(*args, **kargs):
            # arg in d, instance(arg, d[arg])
            for name, obj in sig.bind(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' % (name, btypes[name]))
            return func(*args, **kargs)
        return wrapper
    return decorator


@typeassert(int, str, list)
def f(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    f(1, 'abc', [1, 2, 3])
    f(1, 2, [1, 2, 3])


