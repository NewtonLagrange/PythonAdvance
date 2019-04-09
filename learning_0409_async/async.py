from multiprocessing import Pool
import os
import time


def p1(*args, **kwargs):
        time.sleep(2)
        print('这是第 %s 个子进程, 进程号: %s, 父进程号: %s' % (args[0], os.getpid(), os.getppid()))
        print(kwargs)


def main():
    # 创建进程池
    pool = Pool(4)
    for i in range(1, 5):
        pool.apply_async(func=p1, args=(i, ), kwds={'name': 'Out Time'})

    pool.close()
    pool.join()
    print('finish')


if __name__ == '__main__':
    main()
