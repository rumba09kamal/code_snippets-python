## Scrapping site http://coreyms.com/

from bs4 import BeautifulSoup
import requests
import csv
source  = requests.get('http://coreyms.com/').text
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())
csv_file = open('csv_scrape_file.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','Video Link'])
for article in soup.find_all('article'):
    # print(article.prettify())
    try:
        headline = article.h2.a.text
        summary = article.find('div', class_='entry-content').p.text
        # to access attributes value use dictionary['attributeName']
        vid = article.find('iframe', class_='youtube-player')[
            'src']
        vid_id = vid.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://www.youtube.com/watch?v={vid_id}'
    except Exception as e:
        headline = None
        summary = None
        yt_link = None
    print(headline)
    print(summary)
    print(yt_link)
    print()
    csv_writer.writerow([headline,summary,yt_link])
csv_file.close()