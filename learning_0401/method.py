"""
类方法, 实例方法, 静态方法
"""


class Bird:
    def __init__(self, name):
        self._name = name

    @classmethod
    def fly(cls):
        print('I am fling!')

    @staticmethod
    def jump():
        print('I can jump!')

    def set_name(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


bird = Bird('燕子')
bird.fly()
print(bird.name)
Bird.fly()
