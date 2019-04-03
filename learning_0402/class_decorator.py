# import time
#
#
# class Ly:
#     def __init__(self, one_parm, two_parm, three_parm):
#         self.one_parm = one_parm
#         self.two_parm = two_parm
#         self.three_parm = three_parm
#
#     def __call__(self, fun):
#         print('性别为' + self.one_parm + "的" + self.two_parm + "岁的" + self.three_parm)
#         time.sleep(1)
#
#         def info(*args):
#             fun(*args)
#
#         return info
#
#
# @Ly("男", "22", "ly")
# def show(name, age, sex):
#     print('性别为' + sex + "的" + age + "岁的" + name)
#
#
# print(show, type(show))
import time


class Ly(object):

    def __init__(self, fun):
        print("this is the first step")
        time.sleep(1)
        self.fun = fun

    def __call__(self, *args):
        print("this is the second step")
        time.sleep(1)
        self.fun(*args)
        print("this is the fourth step")
        time.sleep(1)


@Ly
def show(a1, a2, a3, a4):
    print('this is the thirty step', a1, a2, a3, a4)
    time.sleep(1)


print(show, type(show))
show("parm", "1", "1", "1")
print("After first part call")
time.sleep(1)
show("parm", "2", "2", "2")
print("After second part call")
