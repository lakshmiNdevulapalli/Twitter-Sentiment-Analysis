# -*- coding: utf-8 -*-		#sets the file encoding for emoji

__author__ = 'petermarozzi'
import json
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import re

tweets_data_path = 'output.json'
tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()

tweets['tweet'] = list(map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data))

if __name__ == '__main__':
    tweets_data_path = 'output.json'
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

tweets = pd.DataFrame()
texts = []

for line, tweet in enumerate(tweets_data):
    try:
        texts.append(tweet['text'])
    except:
        continue
# print "Error line %d" % (line)

tweets['text'] = texts


def key_words(row):
    words = []
    text = row["text"].lower()
    if "ðŸ˜­" in text or "ðŸ˜ª" in text or "ðŸ˜£" in text or "ðŸ˜’" in text or "â˜¹ï¸" in text:
        words.append("Sad")
    if "ðŸ˜‹" in text or "ðŸ˜Š" in text or "ðŸ˜ƒ" in text or "ðŸ˜Œ" in text or "ðŸ˜" in text or "ðŸ˜‰" in text or "ðŸ˜™" in text or "ðŸ™‚" in text or "ðŸ˜" in text:
        words.append("Happy")
    if "ðŸ˜" in text or "â¤ï¸" in text or "ðŸ’" in text or "ðŸ’•" in text or "ðŸ˜˜" in text or "ðŸ’—" in text or "ðŸ’ž" in text or "ðŸ’–" in text or "ðŸ’›" in text:
        words.append("Loving")
    if "ðŸŽ‰" in text or "ðŸŽ‚" in text or "ðŸŽ" in text or "ðŸ’" in text or "ðŸ‘‘" in text or "ðŸŒ¹" in text:
        words.append("Celebratory")
    if "ðŸ‘" in text or "ðŸ‘Œ" in text or "ðŸ¤™ðŸ½" in text or "ðŸ‘" in text:
        words.append("Ok")
    if "ðŸ˜…" in text or "ðŸ˜†" in text or "ðŸ˜‚" in text:
        words.append("Funny")
    if "ðŸ™€" in text or "ðŸ˜³" in text or "ðŸ˜±" in text:
        words.append("Scared")
    if "ðŸ˜´" in text:
        words.append("Tired")
    if "ðŸ˜¡" in text or "ðŸ˜ " in text:
        words.append("Angry")
    if "ðŸ™ðŸ»" in text or "ðŸ™‡ðŸ»" in text:
        words.append("Hopeful")
    if "ðŸ˜·" in text or "ðŸ¤§" in text:
        words.append("Sick")
    if "ðŸ¤”" in text:
        words.append("Thoughtful")
    if "ðŸ˜Ž" in text:
        words.append("Cool")
    return ",".join(words)


tweets["words"] = tweets.apply(key_words, axis=1)
counts = tweets["words"].value_counts()
print(counts)

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Key Words', fontsize=15)
ax.set_ylabel('Number of Tweets', fontsize=15)
ax.set_title('Key Words', fontsize=15, fontweight='bold')
counts[1:100].plot(ax=ax, kind='bar', color='purple')

pylab.show()