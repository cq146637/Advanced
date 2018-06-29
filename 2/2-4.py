from random import randint

"""
    在一个for语句中迭代多个可迭代对象
"""


# 生成三个列表
math = [randint(60,100) for _ in range(40)]
english = [randint(60,100) for _ in range(40)]
chinese = [randint(60,100) for _ in range(40)]

# 类似并行处理
# 使用zip将多个可迭代对象合并，每次返回以各元组
t = zip(chinese, math, english)  # 长度不一致取较短的列表

# for i in t:
#     print(i)

# 串行处理
# 使用itertools.chain，将多个可迭代对象连接
from itertools import chain

l = chain(math, english, chinese)
for i in l:
    print(i)