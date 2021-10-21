import decorator

if __name__ == '__main__':
    add_object = decorator.Add(1, 4)
    multiply_add_object = decorator.Multiply(add_object, 4)
    print(multiply_add_object.process())
    divide_multiply_add_object = decorator.Divide(multiply_add_object, 5)
    print(divide_multiply_add_object.process())