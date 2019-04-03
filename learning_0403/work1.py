def get_info():
    pass


def get_name():
    pass


Goods = type('Goods', (), {'id': None, 'name': None, 'get_info': get_info})
Food = type('Food', (Goods,), {'get_name': get_name})
g1 = Goods()
f1 = Food()

print('这是g1的方法: ', dir(g1))
print('这是f1的方法: ', dir(f1))
