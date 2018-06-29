"""
    在环状数据结构中管理内存
"""


class A(object):

    def __del__(self):
        print("in __del__")


def text():
    a = A()
    import sys
    print(sys.getrefcount(a))
    # 此处两次引用，多出来的引用为getrefcount本身的引用
    a2 = a
    print(sys.getrefcount(a) - 1)
    # 两次引用
    a = 1
    print(sys.getrefcount(a) - 1)  # 析构函数被调用了


import weakref


class Data(object):

    def __init__(self, value, owner):
        self.value = value
        self.owner = weakref.ref(owner)

    def __str__(self):
        return "%s's data, value is %s" % (self.owner(), self.value)

    def __del__(self):
        print('in Data.__del__')


class Node(object):
    """
        在python中，垃圾回收器通过引用计数来回收垃圾对象，
        但某些环状数据结构（树，图），存在对象间的循环引用，
        比如树的父节点引用子节点，子节点也在同时引用父节点。
        此时同时del父子节点，两个对象不能被立即回收

        解决：
            使用标准库weakref，它可以创建以一种能访问对象但不增加引用计数的对象

    """

    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print('in Node.__del__')


if __name__ == '__main__':
    text()
    node = Node(1)
    del node
    input("wait......")
    # 这里可以导入gc模块强制回收
    # import gc
    # gc.collect()
    # 但是由于存在循环引用，gc不能强制回收
