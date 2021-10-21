
class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def process(self):
        return self.a + self.b


class Multiply:
    def __init__(self, decorated, num):
        self.decorated = decorated
        self.num = num

    def process(self):
        print("I am multiply process")
        return self.decorated.process() * self.num


class Divide:
    def __init__(self, decorated, num):
        self.decorated = decorated
        self.num = num

    def process(self):
        print("I am divide process")
        return self.decorated.process() / self.num
