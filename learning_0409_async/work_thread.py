from threading import Thread
import time


class MyThread(Thread):
    def run(self):
        while True:
            print('Hi, I am a child thread.')
            time.sleep(1)


def main():
    thread = MyThread()
    thread.start()
    thread.join()
    print('Finish')


if __name__ == '__main__':
    main()
