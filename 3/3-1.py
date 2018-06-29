__author__ = 'Cq'

"""
    拆分含有多种分隔符的字符串
"""


def split_method_first(s, ds):
    # 方式一：多次使用split方法处理字符串

    res = [s]

    for i in ds:
        t = list()
        list(map(lambda x: t.extend(x.split(i)), res))
        res = t
        print(t)

    return [i for i in res if i]


def split_method_second(s):
    # 方式二：使用正则表达式
    import re
    res = re.split(r'[,;|\t\n\\]+', s)
    print(res)
    return res

if __name__ == '__main__':

    s = 'asg\nsa\tfas dv,ja,dh;gb;ia;hsdg\iah|giha|ighi\\ash;gia,sg'
    # split_method_first(s, [';', ',', '|', ' ', '\\', '\n', '\t'])
    split_method_second(s)