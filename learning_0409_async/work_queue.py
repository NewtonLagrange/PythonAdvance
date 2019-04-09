from multiprocessing import Process, Queue
import time


class MyProcess(Process):

    def __init__(self, args):
        Process.__init__(self, args=args)
        self.queue = args[0]

    def run(self):
        for i in range(3):
            print('Hi, I am a child process')
            time.sleep(1)
            self.queue.put(i)

        while True:
            num = self.queue.get()
            print(num)


def main():
    queue = Queue(maxsize=4)
    queue.put_nowait(1)
    process = MyProcess((queue, ))
    process.start()
    process.join()
    print('finish')


if __name__ == '__main__':
    main()
