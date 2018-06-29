__author__ = 'Cq'
"""
    将文件映射到内存
"""


def require_one():
    """
        1. 在访问某些二进制文件时，希望能把文件映射到内存中，可以实现随机访问
        2. 某些嵌入式设备，寄存器被编址到内存地址空间，我们可以映射/dev/mem某范围，去访问这些寄存器
        3. 如果多个进程映射同一个文件，还能实现进程通信的目的
    :return:
    """
    # 生成一个二进制文件
    with open('binary.bin', 'wb') as f:
        f.write(b'0' * 2048)

    # 导入mmap模块
    import mmap
    # 获取一个文件对象
    f = open('binary.bin', 'rb+')
    # 获取内存页大小，用于指定offerset
    size = mmap.PAGESIZE
    # 映射到内存
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    # m = mmap.mmap(f.fileno(), size * 8, access=mmap.ACCESS_WRITE, offset=size * 8)
    print(type(m))
    print([0])


if __name__ == '__main__':
    require_one()
