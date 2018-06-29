__author__ = 'Cq'
"""
    提高元组索引的可读性
"""

# 方式一
NAME, AGE, SEX, EMAIL = range(4)

student = ('darius', 20, 'male', '1016025625@qq.com')

# name
print(student[0])

# gender
# ...

# mail
# ...

# 方式二： 使用nametuple

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

s = Student('darius', 20, 'male', '1016025625@qq.com')

# print(s)
# print(s.name)