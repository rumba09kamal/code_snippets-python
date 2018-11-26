import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://www.facebook.com
https://www.github.com
https://www.heroku.com
'''

# pattern = re.compile(r'http(s)?://[a-zA-Z0-9]+.[a-zA-Z0-9.]+[a-zA-Z0-9]+')

# get top level domain(com,gov)
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(0))#acess the captured group`()`


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
