"""
统计性能的装饰器
"""
import time


def time_count(fun):
    def count():
        start = time.time()
        fun()
        end = time.time()
        cost_time = end - start
        print(fun.__name__, '花费了', cost_time)

    return count


@time_count
def test():
    test_list = [x for x in range(1, 1000001)]
    print(test_list[999999])


@time_count
def generator():
    test_gene = (x for x in range(1, 1000001))
    i = 0
    while i != 999999:
        next(test_gene)
        i += 1
    print(next(test_gene))


test()
generator()
