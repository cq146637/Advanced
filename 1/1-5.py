__author__ = 'Cq'
"""
    让字典保持有序，即让字典元素保持原有的生成顺序不改变
"""

# 使用OrderedDict
from collections import OrderedDict

d = OrderedDict()

d[1] = 1
d[2] = 2
d[3] = 3

for i in d:
    print(i)