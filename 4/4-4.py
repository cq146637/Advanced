__author__ = 'Cq'
"""
    访问文件的状态
"""
import os


# 方式一：使用os模块下的stat、fstat、lstat函数获取文件状态
s = os.stat('text-4-4-f')
print(s)
print(os.lstat('text-4-4-f.lnk'))
with open('text-4-4-f') as f:
    print(os.fstat(f.fileno()))

# 获取文件类型
print(s.st_mode)
# 导入stat模块辅助判断
import stat
# 判断是否是文件夹
print(stat.S_ISDIR(s.st_mode))
# 判断是否是常规文件
print(stat.S_ISREG(s.st_mode))

# 查看文件读权限
print(s.st_mode & stat.S_IRUSR)  # 大于零代表真值
print(s.st_mode & stat.S_IROTH)  # 大于零代表真值
print(s.st_mode & stat.S_IRGRP)  # 大于零代表真值

# 查看文件执行权限
print(s.st_mode & stat.S_IXUSR)  # 大于零代表真值
print(s.st_mode & stat.S_IXOTH)  # 大于零代表真值
print(s.st_mode & stat.S_IXGRP)  # 大于零代表真值

# 查看文件写权限
print(s.st_mode & stat.S_IWUSR)  # 大于零代表真值
print(s.st_mode & stat.S_IWOTH)  # 大于零代表真值
print(s.st_mode & stat.S_IWGRP)  # 大于零代表真值

# 查看文件的访问时间戳
import time
print(s.st_atime)
print(time.localtime(s.st_atime))
print(time.ctime(s.st_atime))

# 创建时间
print(s.st_ctime)
print(time.localtime(s.st_ctime))
print(time.ctime(s.st_ctime))

# 修改时间
print(s.st_mtime)
print(time.localtime(s.st_mtime))
print(time.ctime(s.st_mtime))

# 文件大小
print(s.st_size)


# 方式二：使用os.path下的函数

# 获得文件类型os.path.isxxx
print(os.path.isdir('text-4-4-d'))
print(os.path.islink('text-4-4-f.lnk'))
print(os.path.isfile('text-4-4-f'))

# 获取创建、访问、修改时间
print(os.path.getatime('text-4-4-f'))
print(os.path.getctime('text-4-4-f'))
print(os.path.getmtime('text-4-4-f'))

# 获取文件大小
print(os.path.getsize('text-4-4-f'))
