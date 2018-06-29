"""
    多个类支持运算符操作
"""
from functools import total_ordering
from abc import ABCMeta, abstractmethod
from math import pi


@total_ordering
class Shape(object):

    @abstractmethod
    def area(self):
        pass

    # 有了装饰器，我们只需要定义eq和大于或小于两个方法即可
    def __lt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Other is not Shape")
        return self.area() < other.area()

    def __eq__(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Other is not Shape")
        return self.area() == other.area()


class Rectangle(Shape):
    """
        我们希望自定义的类，实例间可以使用
        <,<=,>,>=,==,!=等符号进行比较
        我们自定义比较的行为
        需要重载__lt__,__le__,__gt__,ge__,__eq__,__ne__
        但如果我们使用标准库下的functools下的装饰器total_ordering可以简化此过程
    """

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * pi


if __name__ == '__main__':
    r1 = Rectangle(5, 3)
    r2 = Rectangle(4, 4)
    c1 = Circle(3.4)
    print(r2 < r1)
    print(r2 < c1)