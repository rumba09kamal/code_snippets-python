### Dictionary Comprehensions

names = ["Bruce","Clark","Peter","Logan","Wade"]
heros = ["Batman","Superman","Spiderman","Wolverine","Deadpool"]
# print(dict(zip(names,heros)))# zip function matches up two collections one to one


# (1) create dictionary {'name':'hero'} for each name, hero in zip (names,heros)
# my_dict = {}
#
# for name,hero in zip(names,heros):
#     my_dict[name] = hero
# print(my_dict)

# using dictionary comprehensions
# my_dict = {name:hero for name,hero in zip(names,heros)}
# print(my_dict)

# (2) if name not equal to peter
# my_dict = {}
# for name,hero in zip(names,heros):
#     if name != "Peter":
#         my_dict[name] = hero
# print(my_dict)

# using dictionary comprehension
my_dict = {name: hero for name,hero in zip(names,heros) if name != "Peter"}
print(my_dict)