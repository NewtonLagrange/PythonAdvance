import os
import time
from multiprocessing import Process


def pro1():
    while True:
        time.sleep(1)
        print('这是一个子进程, pid: %s, ppid: %s' % (os.getpid(), os.getppid()))


def main():
    p1 = Process(target=pro1)
    p1.start()


if __name__ == '__main__':
    main()
