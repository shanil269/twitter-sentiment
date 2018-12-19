# Required imports or library dependencies
import re, sys, json
from tweet_sentiment import *

# Fill me.
# Details explained in class.
def gettopTenHashTags(tweets_file, n = 10):
    hashTagFreq = {}
    tweets_file = open(tweets_file)
        
    for tweet in tweets_file:
        tweet_json = json.loads(tweet)        
        
        # Fill me.
        terms = getENTweet(tweet_json)
        for term in terms:
            try:
                if term[0] == '#':
                    try:
                        hashTagFreq[term] += 1
                    except: hashTagFreq[term] = 1
            except: ''

    sortedTags = sorted(hashTagFreq,
                        key=hashTagFreq.get,
                        reverse=True)
    
    return sortedTags[1:n]


        
if __name__ == '__main__':    
    toptenTags = gettopTenHashTags(sys.argv[1])
    print(toptenTags)
    
    
    
