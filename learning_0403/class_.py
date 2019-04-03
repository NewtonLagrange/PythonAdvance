def rename_attr(class_name, parent_class, attrs):
    new_attrs = dict()
    for k, v in attrs.items():
        if not k.startswith('__'):
            k = k.lower()
            new_attrs[k] = v

    return type(class_name, parent_class, new_attrs)


class Test(metaclass=rename_attr):
    Is_alive = False


test = Test()
print(hasattr(test, 'is_alive'))
