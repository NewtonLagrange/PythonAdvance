"""
类属性, 与实例属性
"""


class Good:
    name = 'tea'

    def __init__(self, price: int):
        self._price = price


g1 = Good(20)
g2 = Good(30)
g1.name = 'apple'
print(id(g1), id(g2))
Good.name = 2
print(id(g1.name), id(g2.name), id(Good.name))







