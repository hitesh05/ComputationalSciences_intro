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
f=open("essays/gwalior.txt", "r")
text=f.read()
f.close
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
print(word_freq)