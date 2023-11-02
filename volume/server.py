#!/usr/bin/env python3

import threading
import grpc
from concurrent.futures import ThreadPoolExecutor
from pubsub_pb2_grpc import add_pubsubServicer_to_server, pubsubServicer
from pubsub_pb2 import mes2client, mes2server

class PubsubServer:
    def __init__(self):
        self.threadLock = threading.Lock()
        self.n = 0
        self.mes = "default"
    def pubsubServe(self, request, context):
        if self.n == 0:
            self.threadLock.acquire()  # 线程锁
            self.n += 1
            self.mes = input('mes:')
            self.threadLock.release()  # 释放锁
        self.threadLock.acquire()  # 线程锁
        self.n = 0
        self.threadLock.release()  # 释放锁
        return mes2client(mes2=self.mes)

def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=3))
    add_pubsubServicer_to_server(PubsubServer(), server)
    server.add_insecure_port('[::]:50000')
    server.start()

    try:
        while True:
            pass  # 保持服务器持续运行
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
