"""
    使用描述符对实例属性做类型检查
"""


class Attr(object):

    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise ValueError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person(object):
    """
        对于Person的实例对象，我们要求能像静态类型语言一样，对它们的实例属性做类型检查
        如 p.name = 'darius' 必须是字符串 str
        p.age = 18 必须是整型 int
        p.height = 1.88 必须是 float
        要求：
            可以对实例变量名指定类型
            赋予不正确类型时抛出异常
            
        解决：
            分别实现__get__,__set__,delete__方法
            然后在__set__中使用isinstance函数做类型检查
            
    """

    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)


if __name__ == '__main__':
    p = Person()
    p.name = 'bob'
    p.age = 17
    p.height = 12