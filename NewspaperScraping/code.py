import requests
import html5lib
from bs4 import BeautifulSoup

def get_day_links(date):
    url = 'https://www.thehindu.com/archive/print/' + date + '/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html5lib')
    archive_lists = soup.findAll('ul', class_='archive-list')
    links = []
    for al in archive_lists:
        hrefs = al.findAll('a')
        for href in hrefs:
            link = href['href']
            links.append(link)
    return links

date = '2020/05/05' # YYYY/MM/DD
links = get_day_links(date)
# print(links)
# print(*links, sep = "\n") #to print each element in a newline

from pprint import pprint
import collections
lista = []

for url in links[0:5]:
    dicart = {}
    dicart['url'] = url
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html5lib')
    # print(soup)
    # print(type(soup))
    
    art = soup.find_all(class_ = 'article')
    # print(type(art))
    
    if(art != []):
        
        title = art[0].find_all(class_ = 'title')
        # print((title[0]))
        title_text = title[0].get_text()
        title_text = title_text.strip()
        # print(title_text)
        dicart['title'] = title_text
    
        body = art[0].select("[id*=content-body-]")
        content = ""
        for p in body[0].find_all("p"):
            content += p.get_text()
        dicart['content'] = content
        sorted_x = sorted(dicart.items(), key=lambda kv: kv[1], reverse = True)
        dicart = collections.OrderedDict(sorted_x)
        # print(content)
        lista.append(dicart)
pprint(lista)

import json
with open('result.json','w') as res:
    json.dump(lista, res)

