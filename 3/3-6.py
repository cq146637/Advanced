__author__ = 'Cq'

"""
    去掉字符串中不需要的字符
"""


def first():
    """
        过滤掉用户输入中前后多余的空白字符
    :return:
    """
    string = '  as  '
    print(string.strip())
    print(string.lstrip())
    string = '-------asd++++++++'
    print(string.rstrip('+-'))
    string = 'aaaaaa++bbbbbb'
    print(string[:6] + string[8:])


def second():
    """
        过滤掉某windows下编辑文件中的'\r'
    :return:
    """
    _str = '\raaa\rbbb\tccc\tyyy'
    print(_str.replace('\r', '').replace('\t', ''))

    import re
    print(re.sub('[\t\r]', '', _str))

    # import string python2.x 中maketrans封装在了string对象中
    table1 = str.maketrans('abcxyz', 'xyzabc')  # 生成一个映射表
    print(_str.translate(table1))


def third():
    """
        去掉文本中的unicode组合符号（音调）
    :return:
    """
    u = u'ni\u0301  ha\u030c, chi\u0304  fa\u0300n'
    print(u.translate({0x0301: None, 0x030c: None, 0x0304: None, 0x0300: None}))


if __name__ == '__main__':
    # first()
    # second()
    third()