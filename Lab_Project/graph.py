import twint
import nest_asyncio
import datetime
import pandas
from wordcloud import WordCloud, STOPWORDS
from nltk.tokenize import word_tokenize

import string
import nltk
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.corpus import stopwords 

from collections import Counter
from string import punctuation
from numpy.lib.function_base import percentile


# MAKING A COUNTER (already done in bag of words)
counts = {}
text=""
with open('articles_Wire.csv','r') as f:
    text = f.read()

import spacy
import re
stop_words = nltk.corpus.stopwords.words('english')
new_stpwords = ['amp']
stop_words.extend(new_stpwords)

en = spacy.load("en_core_web_sm")

spacy_tokens=[tok.text.lower() for tok in en.tokenizer(text) ]
spacy_tokens = [re.sub(r'[^\w\s]', '', tok) for tok in spacy_tokens ]
words = [word for word in spacy_tokens if word.isalpha()]

word_list=[word for word in words if word not in stop_words]

snowball = SnowballStemmer('english')
counts={snowball.stem(word) for word in word_list}
counts=Counter(word_list)
# print(counts)

sorted_x = sorted(counts.items(), key=lambda kv:kv[1], reverse=True)
# print(sorted_x)

import collections
sorted_dict = collections.OrderedDict(sorted_x)

PLOTTING THE BAR GRAPH AND SAVING AS GRAPH.PNG
import matplotlib.pyplot as plt
import seaborn as sns
limit = 30
# number of words to plot
keys = list(sorted_dict.keys())[0:limit]
items = [sorted_dict[key] for key in keys]
plt.figure(figsize=(10,5))
sns.barplot(items, keys, alpha=0.8)
plt.title("Top Words Overall in The Hindu")
plt.ylabel("Words", fontsize=12)
plt.xlabel("Counts", fontsize=12)
# plt.savefig('project/graph_Hindu.png')
plt.show()

# MAKING THE WORDCLOUD (as done in lab)
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# temp=' '.join(df['tweet'].tolist())
wordcloud = WordCloud(width = 800, height = 500, 
                background_color ='white', 
                min_font_size = 10).generate(text)
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0) 
plt.savefig('project/wordcloud_Wire.png')