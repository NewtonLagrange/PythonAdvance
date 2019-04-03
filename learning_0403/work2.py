def rename_class(class_name, parent_name, attrs):
    new_attrs = dict()
    for k, v in attrs.items():
        if not k.startswith('__'):
            k = k + '_attr'
            new_attrs[k] = v

    new_class_name = 'new_' + class_name
    return type(new_class_name, parent_name, new_attrs)


class Test(metaclass=rename_class):
    name = 'outime'


test = Test()
print(Test.__name__, test.name_attr)
