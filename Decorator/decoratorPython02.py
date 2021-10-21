def multiply_by_two(func):
    def _multiply_by_two(self=None):
        return func(self) * 2
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
