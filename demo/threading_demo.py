# coding=utf-8
# --------------------------
# @Time    : 18-2-24 上午9:29
# @Author  : knight
# @File    : threading_demo.py
# --------------------------
import time
from threading import Thread


class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = 0
    def run(self):
        while self.n > 0:

            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

c = CountdownThread(5)
c.start()
