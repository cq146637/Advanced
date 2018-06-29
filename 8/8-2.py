__author__ = 'Cq'
"""
    为被装饰的函数保存元数据
"""
"""
    在函数对象中保存着一些函数的元数据，例如：
    f.__name__       函数名
    f.__doc__        函数文档字符串
    f.__module__     函数所属模块名
    f.__dict__       属性字典
    f.__defaults__   默认参数元组
    f.__closure__    返回闭包
    ...              ...

    我们在使用装饰器后，再使用上面这些属性访问时
    看到的是内部包裹函数的元数据，原来函数的元数据便丢失了

    解决：
        使用标准卡functools中的装饰器wraps装饰内部包裹函数
        可以制定将原函数的某些属性，更新到包裹函数上面
"""
from functools import update_wrapper, wraps, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES


def mydecorator(func):
    @wraps(func)
    def wrapper(*agrs, **kwargs):
        '''wrapper function'''
        print('In wrapper')
        func(*agrs, **kwargs)
    # update_wrapper(wrapper, func, ('__name__', '__doc__'), ('__dict__',))  # 第一个元组替换，第二个元组合并
    return wrapper


@mydecorator
def example():
    '''example function'''
    print('In example')


if __name__ == '__main__':
    print(example.__name__)
    print(example.__doc__)
    print(WRAPPER_ASSIGNMENTS)  # 可以使用这个默认元组代替
    print(WRAPPER_UPDATES)
