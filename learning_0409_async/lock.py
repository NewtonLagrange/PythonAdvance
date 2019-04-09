from threading import Thread, Lock
import time


def count_time(fun: callable):
    def count():
        start = time.time()
        fun()
        end = time.time()
        print(fun.__name__, '花费了', end-start)

    return count


def test(lock):
    global num
    lock.acquire()
    for i in range(10000000):
        num += 1

    lock.release()


@count_time
def main():
    lock = Lock()
    t1 = Thread(target=test, args=(lock, ))
    t1.start()
    t2 = Thread(target=test, args=(lock, ))
    t2.start()

    t1.join()
    t2.join()
    print('finish')


if __name__ == '__main__':
    num = 0
    main()
    print(num)
