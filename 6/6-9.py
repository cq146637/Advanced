"""
    通过实例方法名字的字符串调用方法
"""
from lib1 import Circle
from lib2 import Rectangle
from lib3 import Triangle
from operator import methodcaller



def getArea(shape):
    """
        方法一
    :param shape: 
    :return: 
    """
    for name in ('area', 'getArea', 'get_area'):
        f = getattr(shape, name, None)
        if f:
            return f()

def get_area(shape):
    res = None
    for name in ('area', 'getArea', 'get_area'):
        try:
            res = methodcaller(name)(shape)
        except AttributeError:
            pass
    return res



if __name__ == '__main__':
    shape1 = Circle(2)
    shape2 = Triangle(3, 4, 5)
    shape3 = Rectangle(6, 4)

    shapes = [shape1, shape2, shape3]

    print(list(map(getArea, shapes)))
    print(get_area(shape3))