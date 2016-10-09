import picamera
import time
import io
import socket
import struct

class CameraControl:
    def __init__(self, **kwargs):
        self.server = kwargs['server'] if 'server' in kwargs else '127.0.0.1'
        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.video_stabilization = True
        self.is_streaming = False
        # self.buffer_dir = '/home/pi/buffer_dir/'
        self.client_socket = socket.socket()
        self.client_socket.connect((self.server, 8000))
        self.connection = client_socket.makefile('wb')
        self.stream = io.BytesIO()


    def enable_stream():
        self.is_streaming = True
        self.stream()

    def disable_stream():
        self.is_streaming = False

    def stream():
        start = time.time()
        for foo in self.camera.capture_continuous(self.stream, 'bmp'):
            self.connection.write(struct.pack('<L', stream.tell()))
            self.connection.flush()
            self.stream.seek(0)
            self.connection.write(stream.read())
            if self.is_streaming is False:
                self.disconnect()
                break
            elif time.time() - start > 0.5:
                break
            self.stream.seek(0)
            self.stream.truncate()
        self.connection.write(struct.pack('<L', 0))

    def disconnect():
        self.connection.close()
        self.client_socket.close()
