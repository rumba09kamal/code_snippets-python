person = {'name': 'Jenn', 'age': 23}
# print(person)

# string concatination
# sentence = "My name is " + person['name'] + " and I am " + str(person['age']) + " years old."

# formating option, using `format()` method
# sentence = "My name is {} and I am {} years old.".format(person['name'], person['age'])

# using placeholder, useful for value to be repeated
# sentence = "My name is {0} and I am {1} years old.".format(person['name'],person['age'])

# tag = 'h1'
# text = 'This is Headline'
# sentence = '<{0}>{1}<{0}>'.format(tag, text)

# access value from dictionary from placeholder
# sentence = "My name is {0[name]} and I am {1[age]} years old.".format(person, person)
# sentence = "My name is {0[name]} and I am {0[age]} years old.".format(person)
# sentence = "My name is {0[0]} and I am {0[1]} years old".format(list(person))

# access value inside the class with the attribute


# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Jack", 33)
# sentence = "My name is {0.name} and I am {0.age} years old.".format(p1)# passing object in format

# passing keyword in format
# sentence = "My name is {name} and I am {age} years old.".format(name='Jenn', age=23)


# using keyword argument **kwarg, unpack the dict values
# sentence = "My name is {name} and I am {age} years old.".format(**person)
# print(sentence)


# Format and print out numbers
# we can add formating using `:`,
# example:- zero pad 3
# for i in range(1, 11):
#     sentence = "The value is {:03}".format(i)
#     print(sentence)


# pi = 3.14159265
# sentence = "Pi is equal to {:.3f}".format(pi)
# print(sentence)

# comma seperater on large number
# sentence = "1 MB is equal to {:,.2f}".format(1000**2)
# print(sentence)


# print out datetime

import datetime
my_date = datetime.datetime(2018, 11, 29, 18, 3, 45)

# November 29, 2018
# refer https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
# sentence = "{:%B %d, %Y }".format(my_date)

# November 29,2018 fell on a Thrusday and was the 333 days of the year.
sentence = "{0:%B %d, %Y} fell on {0:%A} and was the {0:%j} days of the year.".format(my_date)
print(sentence)
