### BeautifulSoup
# beautifulsoup4
# lxml
# html5lib
# requests

from bs4 import BeautifulSoup
import requests

with open("simple.html") as html_file:
    soup = BeautifulSoup(html_file,'lxml') # specify parser (in this case `lxml`)
# print(soup.prettify()) # `prettify()` pretifies the HTML

# title = soup.title
# print(title)
# titleText = soup.title.text
# print(titleText)
#
# firstdivonpage = soup.div # gets first div on page(contains all child tag)
# print(firstdivonpage)
#
## `find()` method returns the first tag that matches the argument
# findFooterdiv = soup.find('div',class_='footer')
# print(findFooterdiv)


# article = soup.find('div',class_='article')
# print(article)
#
# headline = article.h2.a.text
# summary = article.p.text
# print(headline)
# print(summary)


## `find_all()` returns all tag that matches the argument
articles = soup.find_all('div',class_='article')

headlines = []
summaries = []
for article in articles:
    headlines.append(article.h2.a.text)
    summaries.append(article.p.text)
print(headlines,summaries)