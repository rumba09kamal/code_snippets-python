## List Comprehensions
# - easier or sufficient way to create list based on the existing list

nums = [1,2,3,4,5,6,7,8,9,10]
#
# my_list = []
#
# for n in nums:
#     my_list.append(n)
# print(my_list)


# using list comprehensions
# my_list_c = [n for n in nums] # i want `n` from `for loop`
# print(my_list_c)




# # (2) n*n for each n in nums
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)
#
# # using list comprehension
# my_list = [n*n for n in nums]
# print(my_list)
#
# # using map + lambda
#
# my_list = map(lambda n: n*n, nums)
# print(list(my_list))# to print map objects convert it into the list or tuple


# (3) print n for each n in nums if n is even

# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# using list comprehensions
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# using filter + lambda function
# my_list = filter(lambda n: n%2 == 0,nums)
# print(list(my_list))


# create (letter,num) pair for each letter in 'abcd' and each number in '0123'

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

# using list comprehension
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)