import requests
from bs4 import BeautifulSoup
import pprint
from operator import itemgetter

res1 = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res1.text+res2.text, 'html.parser')
links = soup.select('.titlelink')
votes = soup.select('.score')
subtext = soup.select('.subtext')


def create_custom_hn(links, subtext):
    hn = {}
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        if subtext[index].select('.score'):
            points = int((subtext[index].getText()).split(' ')[0].strip())
            if points >= 100:
                hn[title] = href, points
    sort_hn = hn.items()
    return sorted(sort_hn, key=lambda x:x[1][1], reverse=True)

pprint.pprint(create_custom_hn(links, subtext))