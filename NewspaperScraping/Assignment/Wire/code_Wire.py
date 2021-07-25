import requests
import html5lib
from bs4 import BeautifulSoup

links = []
# with open('TOI_links.txt','r') as f:
#     for row in f:
#         links.append(row)
links.append('https://thewire.in/law/supreme-court-anti-caa-protesters-uttar-pradesh-government-property')
links.append('https://thewire.in/politics/democracy-erosion-india-redefine-meaning')
links.append('https://thewire.in/politics/mohan-bhagwats-rss-outreach-muslims-hypocrisy-or-deviation-from-communal-ideology')
links.append('https://thewire.in/video/watch-anti-caa-women-protesters-enter-active-politics-up-polls-2022')
links.append('https://thewire.in/politics/modi-nationalism-indian-economy-gdp-unemployment-hindutva-love-jihad')
links.append('https://thewire.in/politics/bengal-polls-civil-society-no-vote-to-bjp-fascism-hatred-authoritarianism')
links.append('https://thewire.in/communalism/podcast-ali-khan-mahmudabad-muslim-exclusion-caa')
links.append('https://thewire.in/law/delhi-riots-court-lack-of-supervision-firs-clubbed-asj-vinod-yadav')
links.append('https://thewire.in/politics/kerala-assembly-elections-muslims-voters')
links.append('https://thewire.in/politics/caa-to-be-implemented-no-plans-for-nrc-exercise-in-bengal-kailash-vijayvargiya')

# print(links)


from pprint import pprint
import collections
lista = []

for url in links:
    r = requests.get(url)
    # print(r.content)
    soup = BeautifulSoup(r.content,'html5lib')
    
    title = soup.find_all(class_ = 'title')
    title_text = ""
    for x in title:
        title_text += x.get_text()

    print(title_text)
    desc = soup.find_all(class_='shortDesc')
    short_desc = ""
    for y in desc:
        short_desc += y.get_text()
    print(short_desc)

    body = soup.find_all(class_ = 'col s12 m9 l9')

    content=""
    for a in body:
        content += a.get_text()
    
    print(content)


