__author__ = 'Cq'
# -*- coding=utf-8 -*-
import random


def analyze_item():
    """
        统计列表元素出现次数以及topn
    """

    # 方式一
    l = [random.randint(0, 20) for _ in range(20)]
    print(l)

    d = dict.fromkeys(l, 0)
    print(d)

    for i in l:
        d[i] += 1

    print(d)

    # 对字典中的项进行排序
    # 使用zip函数压缩字典成为元组
    # s = sorted(zip(d.values(), d.keys()))
    s = sorted(d.items(), key=lambda x: x[1])
    print(s)

    # 方式二：使用内置计数器
    from collections import Counter

    d2 = Counter(l)
    # print(d2)
    # print(d2[14])

    res = d2.most_common(3)
    # print(res)


def analyze_word():
    """
        对文本进行词频统计
    :return:
    """
    with open('word_text', 'r', encoding='UTF-8') as f:
        import re
        from collections import Counter
        res = Counter(re.split('\W+', f.read()))
        print(res)
        print(res.most_common(10))


if __name__ == '__main__':
    analyze_item()
    # analyze_word()