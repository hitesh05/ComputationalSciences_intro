import string
import nltk
#nltk.download('stopwords')
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.corpus import stopwords 

import string
from collections import Counter
from string import punctuation
from collections import Counter
from string import punctuation
from numpy.lib.function_base import percentile
# f=open("TOI/TOI_content.txt", "r")
f=open("Wire/Wire_content.txt", "r")
text=f.read()
f.close()
import spacy
en = spacy.load("en_core_web_sm")

spacy_tokens=[tok.text.lower() for tok in en.tokenizer(text) ]

import re
spacy_tokens = [re.sub(r'[^\w\s]', '', tok) for tok in spacy_tokens ]
words = [word for word in spacy_tokens if word.isalpha()]

stop_words = set(stopwords.words('english'))
word_list=[word for word in words if word not in stop_words]

snowball = SnowballStemmer('english')
word_list=[snowball.stem(word) for word in word_list]
word_freq=Counter(word_list)
# print(word_freq)

sorted_x = sorted(word_freq.items(), key=lambda kv:kv[1], reverse=True)

import collections
sorted_dict = collections.OrderedDict(sorted_x)
print(sorted_dict)

# PLOTTING THE BAR GRAPH
import matplotlib.pyplot as plt
import seaborn as sns
limit = 30
# number of words to plot
keys = list(sorted_dict.keys())[0:limit]
items = [sorted_dict[key] for key in keys]
plt.figure(figsize=(10,5))
sns.barplot(items, keys, alpha=0.8)
plt.title("Top Words Overall")
plt.ylabel("Words", fontsize=12)
plt.xlabel("Counts", fontsize=12)
# plt.savefig('TOI/graph_TOI.png')
# plt.savefig('Wire/graph_Wire.png')
plt.show()