# coding=utf-8
# --------------------------
# @Time    : 18-2-24 上午9:33
# @Author  : knight
# @File    : process_demo.py
# --------------------------
from multiprocessing import Process
import time


class MyProcess(Process):


    """
    继承Process类，类似threading.Thread
    """

    def __init__(self, arg):
        super(MyProcess, self).__init__()
        # multiprocessing.Process.__init__(self)
        self.arg = arg

    def run(self):
        '''
        重构run函数
        '''
        print('nMask', self.arg)
        time.sleep(0.5)

    time.sleep(1)
if __name__ == '__main__':
    for i in range(100):
        p = MyProcess(i)
        p.start()
    print('xxxx')
    for i in range(100):
        p.join()
