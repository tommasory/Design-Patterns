def multiply_by_two(func):
    def _multiply_by_two(*args, **kw):
        return func(*args, **kw) * 2
    return _multiply_by_two


class DecoratedAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @multiply_by_two
    def add(self):
        return self.a + self.b


decorated_add = DecoratedAdd(1, 5)
print(decorated_add.add())


@multiply_by_two
def add(a, b):
    return a + b


print(add(1, 5))