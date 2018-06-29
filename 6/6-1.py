"""
    派生内置不可变类型并修改其实例化行为
"""

class IntTuple(tuple):

    def __new__(cls, iterable):
        # 在这里定义实例化行为
        # 我们自定义一个元组，使得元组的每一项为int类，并且大于零
        g = tuple(x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        super(IntTuple, self).__init__()



if __name__ == '__main__':
    t = IntTuple(['a', 2, -1, ['a', 'b'], 3])
    print(t)

