"""
    对迭代器进行切片操作
"""

# 使用itertools.islice,返回一个迭代对象切片的生成器

from itertools import islice


def file_slice():
    f = open('aaa')

    # islice(f, 1, 100)
    # islice(f, 500)
    for i in islice(f, 1, None):
        print(i)


def list_slice():
    l = [i for i in range(0, 20)]
    i = iter(l)
    # start=4表示列表中取索引4开始到14结束
    for x in islice(i, 4, 14):
        print(x)


if __name__ == '__main__':
    # file_slice()
    list_slice()