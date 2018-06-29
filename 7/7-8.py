__author__ = 'Cq'
"""
    多进程使用以及使用Queue进行进程间通信
"""
from multiprocessing import Process, Queue
import threading
# import queue

# def f(q):
#     q.put([42, None, 'hello'])


def f(qq):
    print("in child:",qq.qsize())
    qq.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    q.put("test123")
    # p = threading.Thread(target=f,)
    p = Process(target=f, args=(q,))
    p.start()
    p.join()
    print("444",q.get_nowait())
    print("444",q.get_nowait())
    # prints "[42, None, 'hello']"
    # print(q.get())  # prints "[42, None, 'hello']"