"""
生成器, 生成器迭代之后索引不会重置, 重新创建索引将会重置
"""
list_gene = (x for x in range(1, 11))
i = 0
while i < 10:
    try:
        print(next(list_gene))
        i += 1
    except StopIteration as e:
        print(e)
        break
# 重置生成器索引
list_gene = (x for x in range(1, 11))
for l in list_gene:
    print(l)

print('斐波那契数列')


# 斐波那契
def fib(num):
    a, b = 0, 1
    yield a
    j = 1
    while j < num:
        a, b = b, a + b
        yield a
        j += 1


for i in fib(6):
    print(i)
