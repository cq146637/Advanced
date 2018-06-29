"""
    使用线程本地数据
"""
import os, cv2, time, struct, threading
try:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from http.server import HTTPServer, BaseHTTPRequestHandler
try:
    from SocketServer import TCPServer, ThreadingTCPServer
except ImportError:
    from socketserver import TCPServer, ThreadingTCPServer
from threading import Thread, RLock
from select import select

class JpegStreamer(Thread):
    """
        该线程不停的从本地摄像头采集数据，此线程相当于数据源
    """
    def __init__(self, camera):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}

    def register(self):
        pr, pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr

    def unregister(self, pr):
        self.lock.acquire()
        pw = self.pipes.pop(pr)
        self.lock.release()
        pr.close()
        pw.close()

    def capture(self):
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                #ret, data = cv2.imencode('.jpg', frame)
                ret, data = cv2.imencode('.jpg', frame, (cv2.IMWRITE_JPEG_QUALITY, 40))
                yield data.tostring()

    def send(self, frame):
        n = struct.pack('l', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _, pipes, _ = select([], self.pipes.itervalues(), [], 1)
            for pipe in pipes:
                os.write(pipe, n)
                os.write(pipe, frame)
        self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send(frame)

class JpegRetriever(object):
    """
        一帧一帧的从Streamer采集监控数据
    """
    def __init__(self, streamer):
        self.streamer = streamer
        self.local = threading.local()  # 线程本地数据，使得每一个线程都独立用户一个管道，不与其他线程冲突

    def retrieve(self):
        while True:
            ns = os.read(self.local.pipe, 8)
            n = struct.unpack('l', ns)[0]
            data = os.read(self.local.pipe, n)
            yield data

    def __enter__(self):
        if hasattr(self.local, 'pipe'):
            raise RuntimeError()

        self.local.pipe = streamer.register()  # 注册线程本地对象
        return self.retrieve()

    def __exit__(self, *args):
        self.streamer.unregister(self.local.pipe)
        del self.local.pipe
        return True


class Handler(BaseHTTPRequestHandler):
    """
        接收客户端连接，并处理客户端的视频数据请求
        从Retriever获取数据，并传输给客户端，通过http协议
    """
    retriever = None
    @staticmethod
    def setJpegRetriever(retriever):
        Handler.retriever = retriever

    def do_GET(self):
        if self.retriever is None:
            raise RuntimeError('no retriver')

        if self.path != '/':
            return

        self.send_response(200)
        self.send_header("Content-type", 'multipart/x-mixed-replace;boundary=abcde')
        self.end_headers()

        with self.retriever as frames:
            for frame in frames:
                self.send_frame(frame)

    def send_frame(self, frame):
        self.wfile.write('--abcde\r\n')
        self.wfile.write('Content-Type: image/jpeg\r\n')
        self.wfile.write('Content-Length: %d\r\n\r\n' % len(frame))
        self.wfile.write(frame)


if __name__ == '__main__':
    streamer = JpegStreamer(0)
    streamer.start()

    retriever = JpegRetriever(streamer)
    Handler.setJpegRetriever(retriever)

    print('Start server...')
    # httpd = TCPServer(('', 9000), Handler)  # 只能处理单各客户端
    httpd = ThreadingTCPServer(('', 9000), Handler)
    httpd.serve_forever()

    # 启动完成服务器后，只要客户端访问ADDR+指定端口，即可获取到服务器摄像头的数据

