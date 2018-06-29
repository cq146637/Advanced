"""
    线程间进行事件通知
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
import tarfile
import os
from threading import Event



"""
    在上一个需要的基础上，我们添加新的需求
    1. 转换线程每产生100个xml文件,就通知打包线程将它们打包成tag.gz文件，并删除xml文件
    2. 打包完成后，打包线程反过来通知转换线程,转换线程继续工作
    解决：
        使用标准库中的Threading.Event
        等待事件一端调用wait，等待事件
        通知事件一端调用set，通知事件
    
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

    def __init__(self, queue, cEvent, tEvent):
        super(ConvertThread, self).__init__()
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent

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
        count = 0
        while True:
            # 接收sid、data
            sid, data = self.queue.get()
            # self.csvToXml()
            if sid == -1 :
                self.cEvent.set()
                self.tEvent.wait()
                break
            if data:
                fname = str(sid).rjust(6, '0') + '.xml'
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)
                count += 1
                if count == 5:
                    self.cEvent.set()
                    self.tEvent.wait()
                    self.tEvent.clear()
                    count = 0


class TarThread(threading.Thread):

    def __init__(self, cEvent, tEvent):
        super(TarThread, self).__init__()
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDaemon(True)

    def tarXML(self):
        """
            python下文件打包函数
        :param tfname: 
        :return: 
        """
        self.count += 1
        tfname = '%d.tar.gz' % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
            tf.close()

        if not tf.numbers:
            os.remove(tfname)

    def run(self):
        # 由于该线程是在转换线程执行时，才运行我们可以把它设置为守护线程，跟随转换线程同时结束
        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()  # Event事件set一次默认就不能在wait了，想要循环等待，我们只能调用一次clear函数
            self.tEvent.set()


if __name__ == '__main__':
    q = Queue()
    dThreads = [DownloadThread(i, q) for i in range(1, 11)]

    cEvent = Event()
    tEvent = Event()

    cThread = ConvertThread(q)
    tThread = TarThread(cEvent, tEvent)

    tThread.start()

    for t in dThreads:
        t.start()

    cThread.start()

    for t in dThreads:
        t.join()

    # 当所有的线程都执行结束时
    q.put((-1, None))  # 通知转换线程结束
    print("done ...")


