"""
分布式处理任务
"""
import time
from multiprocessing import Queue, Process


def func():
    print('新的进程')


def wp(*args):
    q = args[0]
    for i in range(1, 11):
        time.sleep(2)
        q.put(i)


def rp(*args):
    q = args[0]
    while True:
        p = q.get()
        print('读取到进程', p)
        # 开启线程
        new_p = Process(target=func)
        new_p.start()


if __name__ == '__main__':
    queue = Queue(10)
    read_p = Process(target=wp, args=(queue,))
    read_p.start()
    write_p = Process(target=rp, args=(queue,))
    write_p.start()

    read_p.join()
    write_p.join()
    print('finish')
