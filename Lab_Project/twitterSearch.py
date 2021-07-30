import twint
import nest_asyncio
import datetime
import pandas

nest_asyncio.apply()
c = twint.Config()

# c.Username = "the_hindu"
c.Username = "timesofindia"
c.Search = "sabarimala"
c.Since = "2017-01-01"
c.Until = "2019-01-01"
#c.Min_likes = 1
c.Limit = 1000
c.Pandas = True
c.Store_csv = True
c.Output = "Output.csv"
c.Hide_output = True
#c.Lang = "en"
# c.Translate = True
# c.TranslateDest = "en"

twint.run.Search(c)

Tweets_df = twint.storage.panda.Tweets_df
#print(Tweets_df)

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
# del Tweets_df["urls"]
del Tweets_df["user_id"]
del Tweets_df["user_id_str"]
# del Tweets_df["quote_url"]
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

#Tweets_df_left = Tweets_df.style.set_properties(**{'text-align': 'left'})
# print(Tweets_df.to_string())
#print(Tweets_df_left)

# import re

# def get_links(text):
#     text=re.sub(r'\S+\.com\S+','',text) #remove urls
#     text=re.sub(r'\@\w+','',text) #remove mentions
#     text =re.sub(r'\#\w+','',text) #remove hashtags

#     links = []
#     for i in text:
#         if re.search(r'http\S+', i)
#         link = re.search(r'http\S+', i)
#         links.append(link)
#     return links

df = twint.storage.panda.Tweets_df
# links = []
# links = df['tweet'].apply(lambda x: get_links(x))
# # print()
# print(links)

# print(df['tweet'].to_string())

with open('links.csv', 'w') as f:
    for ind in df.index:
        f.writelines(df['urls'][ind])
#         f.write('\n')