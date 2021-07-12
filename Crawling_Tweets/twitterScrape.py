import twint
import nest_asyncio
import datetime
import pandas
from wordcloud import WordCloud, STOPWORDS

import string
import nltk
from nltk.stem import PorterStemmer,SnowballStemmer
from nltk.corpus import stopwords 

from collections import Counter
from string import punctuation
from numpy.lib.function_base import percentile

nest_asyncio.apply()
c = twint.Config()  # initial config

c.Username = "narendramodi" # specifying twitter @
c.Limit = 5 # limitting number of tweets
c.Search = "India" # search string

c.Since = "2020-05-15" # search tweets since
c.Until = "2021-07-10" # search tweets until

c.Min_likes = 10  # min likes on the tweet
c.Lang = "en" # lang of tweet

c.Pandas = True # to store tweets in a dataframe
c.Store_csv = True # to store csv file
c.Output = "nmd.csv" # name of csv file
c.Hide_output = True # to hide output on terminal

twint.run.Search(c) # running the search!

Tweets_df = twint.storage.panda.Tweets_df #storing the dataframe

# deleting un-necessary columns from dataframe:
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
del Tweets_df["nlikes"]
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

# printing complete dataframe (no dots)
print(Tweets_df.to_string())

# MAKING A COUNTER (already done in bag of words)
counts = {}
text=""
for index, row in Tweets_df.iterrows():
    text += row["tweet"]

import spacy
en = spacy.load("en_core_web_sm")

spacy_tokens=[tok.text.lower() for tok in en.tokenizer(text) ]

import re
spacy_tokens = [re.sub(r'[^\w\s]', '', tok) for tok in spacy_tokens ]
words = [word for word in spacy_tokens if word.isalpha()]

stop_words = set(stopwords.words('english'))
word_list=[word for word in words if word not in stop_words]

snowball = SnowballStemmer('english')
counts=[snowball.stem(word) for word in word_list]
counts=Counter(word_list)

# print(counts)

# PLOTTING THE BAR GRAPH AND SAVING AS GRAPH.PNG
import matplotlib.pyplot as plt
import seaborn as sns
limit = 20
# number of words to plot
keys = list(counts.keys())[0:limit]
items = [counts[key] for key in keys]
plt.figure(figsize=(10,5))
sns.barplot(items, keys, alpha=0.8)
plt.title("Top Words Overall")
plt.ylabel("Words", fontsize=12)
plt.xlabel("Counts", fontsize=12)
plt.savefig("graph.png")

# MAKING THE WORDCLOUD (as done in lab)
text = ""
text = " ".join(review for review in Tweets_df.tweet)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stopwords,min_font_size = 10).generate(text)
 
# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.savefig("cloud.png")