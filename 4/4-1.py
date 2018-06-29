__author__ = 'Cq'
"""
    对WAV音频二进制文件处理
"""


def python2_rw():
    pass


def python3_rw():
    # 先读入前44个字节的信息
    with open('demo.wav', 'rb') as f:
        info = f.read(44)

        # 使用struct解析字节信息
        import struct
        number_channels = struct.unpack('h', info[22:24])  # h代表字节序，大头字节序
        # print(number_channels)

        bits_per_sample = struct.unpack('i', info[34:38])
        # print(bits_per_sample)

        # 创建一个struct数组，用于存储特殊格式的数据
        import array
        # 获取数据字节数
        f.seek(0, 2)   # 将文件指正移动到末尾，0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。默认为0
        import math
        data_len = math.ceil((f.tell() - 44) / 2)
        buf = array.array('h', (0 for _ in range(data_len)))
        # 将文件指针移动到数据位
        f.seek(44)
        # 将data读入到buf中
        f.readinto(buf)

    # 缩小采样值进而缩小声音
    with open('demo2.wav', 'wb') as f1:
        f1.write(info)
        for i in range(data_len):
            buf[i] = int(buf[i] / 8)
        buf.tofile(f1)


if __name__ == '__main__':
    # python2_rw()
    python3_rw()
