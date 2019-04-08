"""
进程的传参
python进行 *argus, **kwargs作为参数时, 使用无需加*或**只需使用argus/kwargs
"""
import time
from multiprocessing import Process


def pro1(*args, **kwargs):
    while True:
        time.sleep(2)
        print('这是一个子进程, 参数: %s, %s' % (args, kwargs))


def main():
    p1 = Process(target=pro1, args=(1, 2, 3), kwargs={'name': '时间之外', 'age': 21})
    p1.start()
    print(p1.is_alive())
    p1.join()
    print(111111111)


if __name__ == '__main__':
    main()
