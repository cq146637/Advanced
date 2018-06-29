__author__ = 'Cq'
"""
    读写csv数据
"""
import csv


def wr_csv():
    """
        使用标准库中的csv模块
    :return:
    """
    # 下载yahoo网站的数据集

    rf = open('demo.csv', 'rU', encoding='utf-8')

    reader = csv.reader(rf)

    wf = open('demo_copy.csv', 'w', encoding='utf-8')

    writer = csv.writer(wf)

    for row in reader:  # row是一个列表
        print(row)
        # 处理代码...
        writer.writerow(row)

    wf.flush()


if __name__ == '__main__':
    wr_csv()