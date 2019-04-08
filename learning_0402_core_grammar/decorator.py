"""
权限装饰器: 当执行一项业务时, 判断是否具有权限
"""


def check_access(fun):
    def check(*args, **kwargs):
        secret = input('请输入暗号: ')
        if secret == 'outime':
            return fun(*args, **kwargs)
        else:
            print('你没有权限执行......')

    return check


def log(fun):
    def wrapper(*args, **kwargs):
        print('这是一条日志')
        return fun(*args, **kwargs)

    return wrapper


@check_access
def select_fruit(test_arg):
    print('apple', 'orange', 'banana', test_arg)


# 装饰器的本质是执行了代码 --> select_fruit = check_access(select_fruit)
select_fruit('测试参数')


# 双层装饰器
@log
@check_access
def select_fruit():
    print('apple', 'orange', 'banana')


# 双层装饰器的本质 --> 首先函数名传递给内层装饰器,  select_fruit = check_access(select_fruit)
# 之后再将函数名select_fruit传递给外层装饰器 @log, 最终select_fruit = wrapper,即外层装饰器的返回值.
select_fruit()
