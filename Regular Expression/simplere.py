# Python Regular Expression

# Raw string
# - raw string in python is just a sting prefixed with r
# - tells python not to handle blackslash in special way(i.e. doesn't escape it)

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr Stink
The Rock_

cat
mat
pat
bat

'''

sentence = 'Start a sentence and then bring it to an end'

#pattern = re.compile(r'abc')
# pattern = re.compile(r'\.')# to find . we need to escape it otherwise it will find any char except new line

# pattern = re.compile(r'coreyms\.com')# literal matching


# pattern = re.compile(r'.')# matches all character except new line

# pattern = re.compile(r'\d')# matches a digit
# pattern = re.compile('r\D')# matches not a digit

# pattern = re.compile(r'\w') # matches word characters, _
# pattern = re.compile(r'\W')# matches anything that not a characters, _

# pattern = re.compile(r'\s')# matches whitespaces
# pattern = re.compile(r'\S')# matches everything except whitespaces

# \b --> word boundary indicated by whitespace or non-alphaNumeric character
# pattern = re.compile(r'\bHa')# matches all `Ha` that have word boundary directy before
# pattern = re.compile(r'\BHa') # matches `Ha` that doesn't have word boundary before them

# pattern = re.compile(r'^Start')
# pattern = re.compile(r'end$')
# matches = pattern.finditer(sentence)
# for matche in matches:
#     print(matche)


# match a phone number in string
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
# here, [-.] matches character in bracket in this case matches character either dot(.) or hyphen(-)

# pattern = re.compile(r'[89]00[.-]\d{3}[.-]\d{4}')
# matches number starts with 800 or 900 number([89] searching for character either starts with 8 or 9)

# pattern = re.compile(r'[1-5]') # matches character from 1 to 5(range
# pattern = re.compile(r'[a-z]') # matches character lower case letter a to z
# pattern = re.compile(r'[a-zA-Z]') # matches all the lower(a-z) and upper case(A-Z)

# pattern = re.compile(r'[^a-z]')  # inside the charater set carat is used to match character not in bracket
# pattern = re.compile(r'[^b]at')

# quantifier
# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

# pattern to match mr name
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# search string starts with Mr, quantifier `?`(0 or none) is used to check if dot(.) is present or not
# \s is used for to check whitespace
# character set[A-Z] is used to check for character ranges from A to Z
# \w and quantifier * is used for to check for word containing letter 0 or more

# pattern to match all name
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Za-z]\w*')

# matches = pattern.finditer(text_to_search)
# finditer() return regex match objects

# pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
# matches = pattern.findall(text_to_search)
# findall() returns the tuple of matched capturing group

# for match in matches:
#     print(match)

# match() --> only matches at the begining of string
# pattern = re.compile(r'Start')
# pattern = re.compile(r'sentence')  # match will return None
# matches = pattern.match(sentence)
# print(matches)
# search() --> checks match for anywhere in string
# pattern = re.compile(r'sentence')
# matches = pattern.search(sentence)
# print(matches)

# flag(eg:- IGNORECASE or I )
pattern = re.compile(r'start')  # return none
pattern = re.compile(r'start', re.IGNORECASE)
pattern = re.compile(r'start', re.I)  # shorthand for IGNORECASE
matches = pattern.search(sentence)
print(matches)


# print(text_to_search[1:4])


# open the file and search phone number
# with open('data.txt', 'rt') as f:
#     contents = f.read()
#     # print(contents)
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)
