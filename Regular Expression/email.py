import re
import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
abc@edu.np
'''
# print(emails)

# pattern = re.compile(r'[a-zA-Z.-]+@[a-zA-Z-]+\.(com|edu|net|np)')

# using character set
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)
for match in matches:
    print(match)
    print(match.group())

# search and print email address from `data.txt` file
# with open('data.txt', 'rt') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

#     for match in matches:
#         # print(match)
#         print(match.group())
