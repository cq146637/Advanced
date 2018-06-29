"""
    节省创建大量实例的内存
"""


class Player(object):

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class Player2(object):

    __slots__ = ['uid', 'name', 'stat', 'level']
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


if __name__ == '__main__':
    p1 = Player('0001', 'bob')
    p2 = Player2('0001', 'bob')

    # 两个属性一模一样，我们只能查看两个类中属性的区别
    print(set(dir(p1)) - set(dir(p2)))

    # p1比p2多了{'__dict__', '__weakref__'}
    # 只要不使用弱引用时，weakref不会占用太多内存

     # dict是动态绑定
    print(p1.__dict__)
    # 由此可见，当类对象属性过多时，该字典也会增加

    # 我们对比一下两个类对象各自占用的内存
    import sys

    print(sys.getsizeof(p1.__dict__))

    # 如果使用slots表示提前声明对象属性，实例属性不能动态添加和删除了
    # 使用了slots方法，则该类没有__dict__方法