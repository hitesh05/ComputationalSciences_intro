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

nest_asyncio.apply()
c = twint.Config()  # initial config

#c.Username = "narendramodi" # specifying twitter @
# c.Limit = 5000 # limitting number of tweets 
c.Search = "#sabarimala" # search string
# c.Search = "RightToPray"
c.Since = "2017-01-01" # search tweets since
c.Until = "2021-01-01" # search tweets until

c.Min_likes = 1000 # min likes on the tweet
c.Lang = "en" # lang of tweet

c.Pandas = True # to store tweets in a dataframe
c.Store_csv = True # to store csv file
c.Output = "nmd.csv" # name of csv file
c.Hide_output = True # to hide output on terminal

twint.run.Search(c) # running the search!

Tweets_df = twint.storage.panda.Tweets_df #storing the dataframe

del Tweets_df["id"]
del Tweets_df["conversation_id"]
del Tweets_df["timezone"]
del Tweets_df["place"]
del Tweets_df["language"]
del Tweets_df["photos"]
del Tweets_df["created_at"]
del Tweets_df["hashtags"]
del Tweets_df["cashtags"]
del Tweets_df["day"]
del Tweets_df["hour"]
del Tweets_df["nretweets"]
del Tweets_df["nreplies"]
#del Tweets_df["nlikes"]
del Tweets_df["retweet"]
del Tweets_df["urls"]
del Tweets_df["user_id"]
del Tweets_df["user_id_str"]
del Tweets_df["quote_url"]
del Tweets_df["video"]
del Tweets_df["thumbnail"]
del Tweets_df["geo"]
del Tweets_df["near"]
del Tweets_df["source"]
del Tweets_df["user_rt_id"]
del Tweets_df["user_rt"]
del Tweets_df["retweet_id"]
del Tweets_df["reply_to"]
del Tweets_df["retweet_date"]
del Tweets_df["translate"]
del Tweets_df["trans_src"]
del Tweets_df["trans_dest"]
del Tweets_df['username']
del Tweets_df['name']
del Tweets_df['link']

#Tweets_df_left = Tweets_df.style.set_properties(**{'text-align': 'left'})

import re
stop_words = nltk.corpus.stopwords.words('english')
new_stpwords = ['amp','nt']
stop_words.extend(new_stpwords)
# cleaning tweets in the csv file generated
def remove_content(text):
    text = re.sub(r"http\S+", "", text) #remove urls
    text=re.sub(r'\S+\.com\S+','',text) #remove urls
    text=re.sub(r'\@\w+','',text) #remove mentions
    # text =re.sub(r'\#\w+','',text) #remove hashtags
    return text
def process_text(text, stem=False): #clean text
    text=remove_content(text)
    text = re.sub('[^A-Za-z]', ' ', text.lower()) #remove non-alphabets
    tokenized_text = word_tokenize(text) #tokenize
    clean_text = [
         word for word in tokenized_text
         if word not in stop_words
    ]
    if stem:
        clean_text=[stemmer.stem(word) for word in clean_text]
    return ' '.join(clean_text)

df = twint.storage.panda.Tweets_df
df['tweet']=df['tweet'].apply(lambda x: remove_content(x))

# print(df.to_string())

# MAKING A COUNTER (already done in bag of words)
counts = {}
text=""
for index, row in Tweets_df.iterrows():
    text += row["tweet"]

import spacy
en = spacy.load("en_core_web_sm")

spacy_tokens=[tok.text.lower() for tok in en.tokenizer(text) ]
spacy_tokens = [re.sub(r'[^\w\s]', '', tok) for tok in spacy_tokens ]
words = [word for word in spacy_tokens if word.isalpha()]

word_list=[word for word in words if word not in stop_words]

snowball = SnowballStemmer('english')
counts={snowball.stem(word) for word in word_list}
counts=Counter(word_list)
#print(counts)

sorted_x = sorted(counts.items(), key=lambda kv:kv[1], reverse=True)
# print(sorted_x)

import collections
sorted_dict = collections.OrderedDict(sorted_x)

# PLOTTING THE BAR GRAPH AND SAVING AS GRAPH.PNG
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
plt.savefig('project/Sabarimala1000_graph.png')
plt.show()

# MAKING THE WORDCLOUD (as done in lab)
from wordcloud import WordCloud
import matplotlib.pyplot as plt
temp=' '.join(df['tweet'].tolist())
wordcloud = WordCloud(width = 800, height = 500, 
                background_color ='white', 
                min_font_size = 10).generate(temp)
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0) 
plt.savefig('project/Sabarimala1000_wordcloud.png')