__author__ = 'Cq'
"""
    使用临时文件
"""
from tempfile import TemporaryFile, NamedTemporaryFile


def temporary_file():
    """
        某些时候我们需要对临时产生的数据进行分析，然后只保存结果，临时数据就没有用了。这样很大的临时数据如果常驻内存，
        将消耗大量的内存空间，我们可以使用临时文件存储这些临时数据（外部存储）
        临时文件不用命名，且关闭后会自动删除
    :return:
    """
    # 导入tempfile文件下的TemporaryFile，NamedTemporaryFile
    # NamedTemporaryFile(
    # mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True
    # )
    # 此方式创建的文件，在系统目录下是找不到该文件的
    f = TemporaryFile()
    f.write(b'aaaaaaaaaaaaaa' * 20000)  # 将被存储到磁盘中，使用的交换到内存
    # 使用文件时，需要重新指定文件指针
    f.seek(0)
    # 操作文件....

    # NamedTemporaryFile创建带名称的文件
    # NamedTemporaryFile(
    # mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True
    # )
    # 可以在文件系统中找到文件
    ntf = NamedTemporaryFile()
    print(ntf.name)  # C:\Users\Darius\AppData\Local\Temp\tmphmj1s1ns

    # 指定文件关闭后不进行删除 delete=False, 由此创建的文件可以被多个进程同时访问
    ntf1 = NamedTemporaryFile(delete=False)


if __name__ == '__main__':
    temporary_file()