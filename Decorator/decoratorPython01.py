def multiply_by_two(func):
    def _multiply_by_two(a, b):
        return func(a, b) * 2
    return _multiply_by_two

@multiply_by_two
def add(a, b):
    return a + b

print(add(1, 5))

@multiply_by_two
def subtract(a, b):
    return a - b

print(subtract(1, 5))


