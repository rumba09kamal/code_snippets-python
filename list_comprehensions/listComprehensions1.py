## List Comprehensions

# (1) create list based on string

shark_letters = [letter for letter in "shark"]
print(shark_letters)

# using for loop
# shark_letters = []
# for letter in "shark":
#     shark_letters.append(letter)
# print(shark_letters)


## Using conditional with list comprehensions
# if statement

fish_tuple = ("blowfish","catfish","octopus","clownfish")

fish_list = [fish for fish in fish_tuple if fish != "octopus"]
print(fish_list)


number_list = [x ** 2 for x in range(10) if x%2 == 0]
print(number_list)

# nested if condition

num_list = [x for x in range(100) if x%3==0 if x%5 == 0]
print(num_list)


### Nested loop in list comprehensions
# my_list = []
# for x in [20,40,60]:
#     for y in [2,4,6]:
#         my_list.append(x*y)
# print(my_list)

my_list = [x*y for x in [20,40,60] for y in [2,4,6]]
print(my_list)


### conclusion
# list comprehensions allows us to transform one list or other sequence into the new list
# they provide a consice syntax for completing this task, limiting our lines of code
# it is important that our final code is readable as possible, so very long single lines
# of code should be avoided to ensure that our code is user friendly.