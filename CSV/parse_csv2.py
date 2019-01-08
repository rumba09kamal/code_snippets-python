import csv

html_output = ''
names = []
"""
with open('names.csv') as file:
    csv_reader = csv.reader(file)
    # don't want to read the headers
    next(csv_reader)
    for line in csv_reader:
        names.append(f'{line[0]} {line[1]}')

html_output += '<ul>'
for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n<ul/>'
print(html_output)
"""


# method 2
with open('names.csv') as file:
    csv_reader = csv.DictReader(file)

    for line in csv_reader:
        names.append(f"{line['first_name']} {line['last_name']}")


html_output += '<ul>'
for name in names:
    html_output += f'\n\t<li>{name}</li>'
html_output += '\n</ul>'
print(html_output)
