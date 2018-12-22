def add(x, y):
    """ add function """
    return x + y


def sub(x, y):
    """ substract function """
    return x - y


def multiply(x, y):
    """ multiply function"""
    return x * y


def divide(x, y):
    """ divide function  """
    if y == 0:
        raise ValueError('Cann\'t divide by zero champ!')
    return x / y


# print(divide(6, 6))
