__author__ = 'Cq'
"""
    实现用户的历史记录功能
"""

# 创建一个队列，容量为n，右进左出
# 使用deque，它是一个双端队列
from collections import deque

# 初始化队列，并限定大小
q = deque([], 5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

print(q)

q.append(6)
print(q)
print(list(q))


# 持久化队列

# 使用pickle，将内存对象持久化
import pickle

with open('history', 'wb') as f:
    pickle.dump(q, f)

q2 = pickle.load(open('history', 'rb'))
print(q)
print(q2)