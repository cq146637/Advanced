"""
    线程间通信
"""
import csv
import threading
import requests
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
# from xml_pretty import prety
from xml.etree.ElementTree import Element, ElementTree
from collections import deque
q = deque()  # 该队列是线程不安全的

try:
    from Queue import Queue
except ImportError:
    from queue import Queue  # 该Queue是线程安全的，即自动加解锁


"""
    由于全局解释器锁CLI的存在，多线程进行CPU密集型操作并不能提高执行效率
    解决：
        1. 使用多个线程处理IO操作
        2. 使用一个ConvertThread线程进行转换（CPU密集型）
        3. 下载线程把下载数据安全地传递给转换线程
"""


class DownloadThread(threading.Thread):

    def __init__(self, sid, queue):
        super(DownloadThread, self).__init__()
        self.sid = sid
        self.queue = queue
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6, '0')

    def download(self, url):
        # 并发处理问题，提高效率
        # 以下载雅虎大量股票数据为例
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        # 1. 下载数据
        data = self.download(self.url)
        # 2. 将下载完成的数据传递给转换线程
        self.queue.put((self.sid, data))


class ConvertThread(threading.Thread):

    def __init__(self, queue):
        super(ConvertThread, self).__init__()
        self.queue = queue


    def csvToXml(scsv, fxml):
        reader = csv.reader(scsv)
        headers = reader.__next__()
        headers = map(lambda h: h.replace(' ', ''), headers)

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

    def run(self):
        while True:
            # 接收sid、data
            sid, data = self.queue.get()
            # self.csvToXml()
            if sid == -1 :
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)


if __name__ == '__main__':
    q = Queue()
    dThreads = [DownloadThread(i, q) for i in range(1, 11)]
    cThread = ConvertThread(q)
    for t in dThreads:
        t.start()
    cThread.start()

    for t in dThreads:
        t.join()

    # 当所有的线程都执行结束时
    q.put((-1, None))  # 通知转换线程结束
    print("done ...")

