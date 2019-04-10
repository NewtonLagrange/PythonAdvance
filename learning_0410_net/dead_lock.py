import threading


def fun1():
    lock1.acquire()
    print('这是第一个函数')
    lock2.release()
    a = 1
    while True:
        a += 1
        pass


def fun2():
    lock2.acquire()
    print('这是第二个函数')
    lock2.release()
    a = 1
    while True:
        a += 1
        pass


def main():
    thread1 = threading.Thread(target=fun1)
    thread2 = threading.Thread(target=fun2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print('finish')


if __name__ == '__main__':
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    lock2.acquire()
    main()
    a = 1
    while True:
        a += 1
        pass
