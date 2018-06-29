__author__ = 'Cq'
import random


def filter_list():
    """
    过滤列表项
    :return:
    """

    l = [2, 3, -5, 10, -5]
    # 方式一，过滤函数
    res = filter(lambda x: x >= 0, l)

    for i in res:
        print(i)

    # 方式二: 列表生成式，速度比方式一快
    l = [i for i in l if i > 0]
    print(l)


def filter_dict():
    """
    过滤字典值
    :return:
    """
    d = {i: random.randint(0, 100) for i in range(1, 11)}
    # 字典表生成式
    d = {x: y for x, y in d.items() if y > 60}

    print(d)


def filter_set():
    """
    过滤字典项
    :return:
    """
    s = {1, 2, 3, 4, 5, 6}
    s = {i for i in s if i > 4}
    print(s)

if __name__ == '__main__':
    # filter_list
    # filter_dict()
    filter_set()

