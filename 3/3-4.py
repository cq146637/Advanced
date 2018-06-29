__author__ = 'Cq'
import timeit


def direct_add():
    """
    如果直接使用字符串相加，每次相加后都会产生一个临时列表，下次相加时则产生行的。当列表大时，会造成内存浪费
    :return:
    """
    s = ""
    for i in ['a', 'b', 'c', 'd']:
        s += i
        print(s)


def join_add():
    """
        推荐使用
    :return:
    """
    # s = ''.join(['a', 'b', 'c', 'd'])
    s = ''.join(str(i) for i in ['a', 'b', 'c', 'd', 1, 2])
    print(s)


if __name__ == '__main__':
    # direct_add()
    join_add()
