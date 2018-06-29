__author__ = 'Cq'
from random import randint, sample


"""
    快速找到多个字典中出现的公共键
"""

# l = sample('abcde', randint(3, 6))
# print(l)

d1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(d1)

d2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(d2)

d3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(d3)


def method_one():
    # 方法一：效率低
    same = list()
    for k in d1:
        if k in d2 and k in d3:
            same.append(k)
    print(same)

s1 = d1.keys()
s2 = d2.keys()
s3 = d3.keys()


def method_two():
    # 方法二：对于数量固定的字典使用

    print(s1 & s2 & s3)


def method_three():
    # 方法三：map+reduce
    # 注意reduce函数在python2中存在
    # 在python3中使用如下
    from functools import reduce
    # res = map(dict.keys, [d1, d2, d3])
    # print(res)
    # res = map(dict.keys, [d1, d2, d3])
    res = reduce(lambda a, b: a & b, map(dict.keys, [d1, d2, d3]))
    print(res)


if __name__ == '__main__':
    # method_one()
    # method_two()
    method_three()
