import requests
import html5lib
from bs4 import BeautifulSoup

links = []
# with open('TOI_links.txt','r') as f:
#     for row in f:
#         links.append(row)
links.append('https://timesofindia.indiatimes.com/india/caa-and-nrc-not-anti-muslim-says-rss-chief-in-assam/articleshow/84624952.cms')
links.append('https://timesofindia.indiatimes.com/elections/assembly-elections/kerala/congress-will-not-implement-caa-in-kerala-rahul/articleshow/81908696.cms')
links.append('https://timesofindia.indiatimes.com/india/right-to-protest-cant-be-anytime-everywhere-sc-junks-shaheen-bagh-review-plea/articleshow/80893702.cms')
links.append('https://timesofindia.indiatimes.com/city/chennai/will-pass-resolutions-against-caa-farm-laws-tamil-nadu-cm-m-k-stalin/articleshow/83766572.cms')
links.append('https://timesofindia.indiatimes.com/city/kolkata/dont-politicise-it-says-shah-questions-cms-silence-on-rajbanshi-boys-death/articleshow/82022369.cms')
links.append('https://timesofindia.indiatimes.com/elections/assembly-elections/assam/gadkari-takes-on-cong-for-its-guarantee-to-nullify-caa-in-assam-if-voted-to-power/articleshow/81712113.cms')
links.append('https://timesofindia.indiatimes.com/elections/assembly-elections/assam/bjps-polarising-tactics-will-not-work-in-assam-sitaram-yechury/articleshow/81901338.cms')
links.append('https://timesofindia.indiatimes.com/city/guwahati/anti-caa-group-stages-protest-in-jorhat/articleshow/79296341.cms')
links.append('https://timesofindia.indiatimes.com/city/guwahati/hundreds-of-students-hit-guwahati-streets-demanding-scrapping-of-legislation/articleshow/79691370.cms')
links.append('https://timesofindia.indiatimes.com/city/meerut/hathras-cremation-rerun-of-what-we-faced-kin-of-those-killed-in-caa-dalit-protests-speak-up/articleshow/78469121.cms')

# print(links)


from pprint import pprint
import collections
lista = []

for url in links:
    # print(url)
    dicart = {}
    # dicart['url'] = url
    r = requests.get(url)
    # print(r.content)
    soup = BeautifulSoup(r.content,'html5lib')
    # print(soup)
    # print(type(soup))
    
    title = soup.find_all(class_ = '_1Y-96')
    title_text = ""
    for x in title:
        title_text += x.get_text()

    print(title_text)
    dicart['title'] = title_text

    # print(art)
    body = soup.find_all(class_ = '_3YYSt clearfix')
    # print(body[0])

    content=""
    for a in body:
        content += a.get_text()
    
    print(content)
    dicart['content'] = content
    sorted_x = sorted(dicart.items(), key=lambda kv: kv[1], reverse = True)
    dicart = collections.OrderedDict(sorted_x)
    lista.append(dicart)
    # print(dicart)

# print(lista)
# print(dicart)


