### Set Comprehensions
## set - collection which is unordered, unindexed. No duplicate members allowed.
nums = [1,1,1,1,2,2,2,3,4,5,6,7,7,8,8,8,9,9]

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

my_set = {n for n in nums}
print(my_set)


### Generator Expressions

nums = [1,2,3,4,5,6,7,8,9]

# yield n*n for each n in nums
# def gen_func(nums):
#     for n in nums:
#         yield n*n
# my_gen = gen_func(nums)
#

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)