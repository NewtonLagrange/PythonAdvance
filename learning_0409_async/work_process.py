from multiprocessing import Process
import time


class MyProcess(Process):
    def run(self):
        while True:
            print('Hi, I am a child process')
            time.sleep(1)


def main():
    process = MyProcess()
    process.start()
    process.join()
    print('finish')


if __name__ == '__main__':
    main()
