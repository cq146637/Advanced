"""
    让类支持运算符操作
"""
from functools import total_ordering


@total_ordering
class Rectangle(object):
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

    # 有了装饰器，我们只需要定义eq和大于或小于两个方法即可
    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()


if __name__ == '__main__':
    r1 = Rectangle(5, 3)
    r2 = Rectangle(4, 4)
    print(r1 < r2)
    # 此处为简单实现，我们在下一节定义抽象类，并让需要运行的类都集成该类，使得圆类、三角形类、正方形类都能比较面积大小