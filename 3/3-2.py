__author__ = 'Cq'
import os
import stat
"""
    判断字符串是否已字符串a或字符串b结尾
"""


l = [i for i in os.listdir('/root/text/') if i.endswith(('.sh', '.py'))]

print(l)

umask = stat.S_IXUSR

print(umask)

for i in l:
    print(oct(os.stat('/root/text/' + i).st_mode))
    # 给文件执行权限
    os.chmod('/root/text/' + i, os.stat('/root/text/' + i).st_mode | stat.S_IXUSR)