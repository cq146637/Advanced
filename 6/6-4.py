"""
    创建可管理的对象属性
"""
from math import pi


class Circle(object):
    """
        使用内置的property函数为类创建可管理属性
        fget,fset,fdel对应相应的属性
    """

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        # 使用访问器使得取值能够更加灵活，并且能隐藏相关的操作
        return self.radius

    def setRadius(self, value):
        # if not isinstance(value, (int,float,long)): python2
        # python 中 int 自动提升到long
        if not isinstance(value, (int, float)):
            raise ValueError('Wrong Type.')

        self.radius = float(value)

    def getArea(self):
        return self.radius ** 2 * pi

    R = property(getRadius, setRadius)


if __name__ == '__main__':
    c = Circle(3.2)
    print(c.R)
    c.R = 2
    print(c.R)

