import re, sys, json
from tweet_sentiment import *

# Fill the rest
# Details explained in class.
# Input: The downloaded tweets file
# Output: The freq dictionary {key: tweet terms, value: frequency as probability}
def frequency(tweets_file):
    freq = {}
    tweets_file = open(tweets_file)
    total = 0
    
    for tweet in tweets_file:
        tweet_json = json.loads(tweet)
        tweet_terms = getENTweet(tweet_json)

        total += len(tweet_terms)
        
        for term in tweet_terms:
            term = term.lower()
            try:
                freq[term] += 1
            except: freq[term] = 1

    return freq

def printFrequency(freqDict):
    for key in freqDict.keys():
        try:
            print("%s %.4f" % ( key, freqDict[key] ) )

        except: ''

if __name__ == '__main__':
    printFrequency(frequency(sys.argv[1]))
    
