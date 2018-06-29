__author__ = 'Cq'
"""
    字符串的左，右，居中对齐
"""

text = {
    'Alexander': 182.3,
    'Elijah': 191.6,
    'Wallace': 155.5,
    'Winston': 188.6,
    'Wyatt': 190.2,
    'bob': 144.4,
    'tom': 166.6
}


def str_just(string):
    # 使用str内置方法对齐
    print(string.ljust(20, '-'))
    print(string.rjust(20, '-'))
    print(string.center(20, '-'))


def str_format(string):
    print(format(string, '<20'))
    print(format(string, '>20'))
    print(format(string, '^20'))


def text_center():
    max_len = max(map(len, text.keys()))
    for i in text:
        print(i.ljust(max_len), ':', str(text[i]))


if __name__ == '__main__':
    str_just('abc')
    str_format('abc')
    text_center()