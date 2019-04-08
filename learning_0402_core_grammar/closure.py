def f1(a):
    def f2(b):
        c = a + b
        return c

    return f2


f = f1(10)
print(f.__name__)
