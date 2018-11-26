import re
# find phone number, name, email
with open('data.txt', 'rt') as f:
    contents = f.read()
    pattern = re.compile(r'\d{3}[-]\d{3}[-]\d{4}')
    matches = pattern.findall(contents)
    for phoneNumbers in matches:
        print(phoneNumbers)

    pattern = re.compile(r'(^[a-zA-Z]+)\s([a-zA-Z]+)', re.M | re.I)
    matches = pattern.finditer(contents)
    for names in matches:
        print(names.group())

    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', re.M | re.I)
    matches = pattern.findall(contents)
    for email in matches:
        print(email)
