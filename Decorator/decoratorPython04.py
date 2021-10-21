def multiply_by_two(func):
    def _multiply_by_two(*args, **kw):
        return func(*args, **kw) * 2
    return _multiply_by_two


def divide_by_three(func):
    def _divide_by_three(*args, **kw):
        return func(*args, **kw) /3
    return _divide_by_three


@divide_by_three
@multiply_by_two
def add(a, b):
    return a + b


print(add(1, 5))