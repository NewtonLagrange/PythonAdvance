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


@check_access
def select_fruit(test_arg):
    print('apple', 'orange', 'banana', test_arg)


# 装饰器的本质是执行了代码 --> select_fruit = check_access(select_fruit)
select_fruit('测试参数')

