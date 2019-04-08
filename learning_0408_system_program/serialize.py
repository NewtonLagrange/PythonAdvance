import json


class Good:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def eat(self):
        pass


with open('good.txt', 'a') as f:
    g = Good('tea', 20)
    result = json.dumps(g.__dict__)
    json.dump(g.__dict__, f)
    f.write('\n')

with open('good.txt', 'r') as f:
    # for text in f.read():
    #     print(text)
    r1 = f.readline()
    print(r1)
    r2 = f.readline()
    print(r2)
