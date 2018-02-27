#!/usr/bin/python3
'''
LEGB ==> common abbreation for understanding scoping rule in python
Local, Enclosing, Global, Built-in

- order in which python searches variable , first Local,Enclosing,Global,Built-in
'''

# Local an Global variable scope
x = 'global x'


def test(z):  # z is also local i.e. not availabe outside the test function
    global x
    x = 'global x inside function'
    y = 'local y'
    print(z)


# test('local z')
# print(x)

# buit-ins
# m = min([5, 4, 3, 2, 1])  # min is built-in function of python
# print(m)

# import builtins

# print(dir(builtins))


# Enclosing

def outer():
    x = 'outer x'

    def inner():
        # nonlocal x
        x = 'string inner x'
        print(x)  # checks local scope of enclosing function
    inner()
    print(x)


print('LEGB rules')
outer()
print(x)
