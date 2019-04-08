from multiprocessing import Process


class MyProcess(Process):
    def run(self):
        print(self.name)


def main():
    p1 = MyProcess(name='MyProcess', args=(1, 2, 3), kwargs={'name': '时间之外', 'age': 21})
    p1.start()
    print(p1.is_alive())
    p1.join()
    print(111111111)


if __name__ == '__main__':
    main()
