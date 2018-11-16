## Sorting in python
# sort() method sorts the element in ascending or descending order
# syntax:- list.sort(key=.., reverse=..)
# we can use python in-built `sorted()` method for the same purpose
# `sorted()` returns a sorted list from the given iterable


li = [9,1,8,2,7,3,6,4,5]
# s_li = sorted(li) # sorted() returns new sorted list
s_li = sorted(li,reverse=True) # sorts in descending order
print('sorted variable:\t',s_li)
# li.sort() # returns None
# li.sort(reverse=True)
print('original variable:\t',li)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup) # ascending order
# s_tup = sorted(tup,reverse=True) # descending order
print('Tuple:\t',s_tup)


di = {'name':'kamal','job':'programming','age':None,'os':'Mac'}
s_di = sorted(di)#by default sort with key
print('Dict:\t',s_di)


li = [-5,-6,-1,1,2,3,4]
s_li = sorted(li)
# print(s_li)
# sorting with absolute value
s_li = sorted(li,key=abs)
print(s_li)

class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('Carl',37,70000)
e2 = Employee('Sarah',29,80000)
e3 = Employee('John',43,90000)

employees = [e1,e2,e3]
# sorted(employees) # produces error(requires key to sort it)

# def e_sort(emp):
#     # return emp.name
#     # return emp.age
#     return emp.salary
# s_employees = sorted(employees, key = e_sort)

# s_employees = sorted(employees, key = lambda e: e.age)

from operator import attrgetter

s_employees = sorted(employees, key=attrgetter('salary'))
print(s_employees)
