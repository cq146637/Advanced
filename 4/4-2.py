__author__ = 'Cq'
"""
    设置文件缓冲，减少io操作次数。将多个IO操作合并，达到减少io时间
"""

# python默认文件带有缓冲，缓冲区大小为4096个字节
with open('demo.txt', 'w') as f:
    f.write('*' * 4096)
    f.write('-')

# 设置全缓冲
with open('demo1.txt', 'w', buffering=2048) as f:
    f.write('+' * 2048)
    f.write('-')

# 设置行缓冲,遇到回车符写入
with open('demo2.txt', 'w', buffering=1) as f:
    f.write('0sfasf')
    f.write('bbbbb')
    f.write('\n')

# 设置无缓冲,实时写入
with open('demo3.txt', 'w', buffering=0) as f:
    f.write('aaaaa')

