from threading import Thread
import threading
import time


def count_time(fun: callable):
    def count():
        start = time.time()
        fun()
        end = time.time()
        print(fun.__name__, '花费了', end-start)

    return count


def test():
    print('线程调用.')
    time.sleep(1)


@count_time
def main():
    thread_list = list()
    for i in range(5):
        thread = Thread(target=test)
        thread_list.append(thread)
        thread.start()

    print(threading.enumerate()[1].name)
    for t in thread_list:
        t.join()

    print('finnish')


if __name__ == '__main__':
    main()

    print(threading.current_thread())
