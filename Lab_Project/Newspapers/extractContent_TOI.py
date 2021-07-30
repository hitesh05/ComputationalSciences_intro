import requests
import html5lib
from bs4 import BeautifulSoup
from pprint import pprint
import collections

import time

start = time.time()

links = []
lines = []

with open('Output.csv','r') as f:
    for line in f:
        line = line.strip()
        lines.append(line)

def get_links(list):
    links = []
    for x in lines:
        url = x
        links.append(url)
    return links   

def get_len(links):
    count = 0
    for i in links:
        count += 1
    return count

temp = get_links(lines)
[links.append(x) for x in temp if x not in links]

# length = get_len(links)
# print(length)

# print(links)

count = 1
for url in links:
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html5lib')

    title = soup.find_all(class_ = '_1Y-96')
    title_text = ""
    for x in title:
        title_text += x.get_text()

    if len(title_text) == 0:
        continue
    else:
        print(count)
        count += 1
        print(title_text)

        body = soup.find_all(class_ = '_3YYSt clearfix')
        content = ''
        for a in body:
            content += a.get_text()
        print(content)

end = time.time()
print()
print('Time taken by the program to run:' , end - start, 'seconds')