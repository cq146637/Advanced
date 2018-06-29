"""
    多线程使用
"""
import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
# from StringIO import StringIO  python2 中的导入，python3已经被取消
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
# from xml_pretty import prety
import threading



def download(url):
    # 并发处理问题，提高效率
    # 以下载雅虎大量股票数据为例
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content)


def csvToXml(scsv, fxml):
    reader = csv.reader(scsv)
    headers = reader.__next__()
    headers = map(lambda h:h.replace(' ',''), headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag, text in zip(headers, row):
            e = Element(tag)
            e.text = text

    # pretty(root)
    et = ElementTree(root)
    et.write(fxml)


class MyThread(threading.Thread):

    def __init__(self, sid):
        super(MyThread, self).__init__()
        self.sid = sid

    def run(self):
        handle(self.sid)


def handle(sid):
    print('Download...(%d)' % sid)
    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url %= str(sid).rjust(6, '0')
    rf = download(url)
    if rf is None:
        return
    print('Convert to XML...(%s)' % sid)
    fname = str(sid).rjust(6, '0') + '.xml'
    with open(fname, 'wb') as wf:
        csvToXml(rf, wf)




if __name__ == '__main__':
    # 处理单条
    # url = 'http://table.finance.yahoo.com/table.csv?s=000001.sz'
    # rf = download(url)
    # if rf:
    #     with open('000001.xml', 'wb') as wf:
    #         csvToXml(rf, wf)

    # 并发处理方式一
    # 使用多线程函数并发处理
    t = threading.Thread(target=handle, args=(1,))
    t.start()

    # 并发处理方式二
    t = MyThread(2)
    t.start()
    t.join()  # 使得主线程退出时，先等待子线程执行结束

