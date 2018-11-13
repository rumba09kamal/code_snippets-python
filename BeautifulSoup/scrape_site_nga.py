#### Scraping site `https://www.nga.gov/`
# collecting artist name and relevent links
# import libraries
from bs4 import BeautifulSoup
import requests
import csv

## Sometimes a good idea to scrape website with header so that site can identify you
# headers = {
#     'User-Agent': 'Your Name, example.com',
#     'From': 'email@example.com'
# }
#
# url = 'https://example.com'
#
# page = requests.get(url, headers = headers)
csv_file = open('z-artist-name.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Artist Name', 'Link'])

pages = []
for i in range(1,5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for page in pages:
    page = requests.get(page)
    #create beautifulsoup object
    soup = BeautifulSoup(page.text,'lxml')

    # Remove bottom links or tag from the parse tree and destroy it along its content
    last_link = soup.find(class_='AlphaNav')
    last_link.decompose()


    artist_name_list = soup.find('div',class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')
    # print(artist_name_list_items)


    # use .contents to pull out the <a> tag's children
    for artist_name in artist_name_list_items:
        # print(artist_name.prettify())
        try:
            links = artist_name.get('href')
            links = f'https://web.archive.org+{links}'
            name = artist_name.contents[0]#gets artist name
        except Exception as e:
            links = None
            name = None
        csv_writer.writerow([name,links])
        print(name)
        print(links)
        print()
csv_file.close()