"""
类方法, 实例方法, 静态方法
"""
import types


class Bird:
    """
    这是一只鸟
    """

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


# 动态添加类方法
@classmethod
def fact(cls):
    print('动态添加类方法')


# 动态添加实例方法
def fact1(self):
    print('动态添加实例方法')


# 动态添加静态方法
@staticmethod
def static():
    print('这是一个静态方法')


Bird.fact = fact
bird.fact1 = types.MethodType(fact1, bird)
Bird.static = static

Bird.fact()
bird.fact1()
Bird.static()
bird.static()
# 删除指定方法
del Bird.static
