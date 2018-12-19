# Required imports or library dependencies
import re, sys, json
from tweet_sentiment import *


MAX_VALUE = 5
MIN_VALUE = -5

# Generate predicted Sentiment Dictionary from tweet score and unknown tweet terms.
# May want to use try except block
# The predSentDict updates automatically that is why we do not return anything.
# Fill the rest, details explained in class.
def genPredSentDict(score, numTerms, uTerms, predSentDict):    
    for uTerm in uTerms:
        try:
            # Fill me.
            currScore, currNumTerms = predSentDict[uTerm]
            currScore += score
            currNumTerms += numTerms
            predSentDict[uTerm] = [currScore, numTerms]
        except: predSentDict[uTerm] = [score, numTerms]
        

# Analyse The tweet
# Input: Tweet terms as list, and the sentiment dictionary - hashmap/map
# Output: tweet score, unknown terms as a set data structure.
# Fill the rest. 
# Details explained in class.
def tweetAnalysis(tweet_terms, sentDict):    
    tweet_score = 0
    unknown_terms = set()    
    for term in tweet_terms:
	# Fill me
	# Incomplete! Have to fill the rest.
        try:
            tweet_score += sentDict[term.lower()]
        except: unknown_terms.add(term.lower())
    
    return tweet_score, unknown_terms


# Refine the new sentiment dicionary!
# Details explained in class.
# Update the new sentiment dictionary, therefore no explicit return
# Fill the rest.
def refinePredSentDict(newSentDict):
    for key in newSentDict.keys():
	# fill me.
        value1, value2 = newSentDict[key]
        value = value1 / value2
        if value > MAX_VALUE:
            value = MAX_VALUE
        if value < MIN_VALUE:
            value = MIN_VALUE
        newSentDict[key] = value


def printSentDict(sentDict):
    for key in sentDict.keys():
        value = sentDict[key]
        try:
            print("%s %.4f" % (key, value))
        except: ''


def initPredSentDict(sentDict, tweets_file):
    newSentDict = {}    
    tweets_file = open(tweets_file)
    sentDict = genSentDict(sentDict)
    
    for tweet in tweets_file:
        tweet_json = json.loads(tweet)
        tweet_terms = getENTweet(tweet_json)

        nTerms = len(tweet_terms)
        score, uTerms = tweetAnalysis(tweet_terms, sentDict)
        genPredSentDict(score, nTerms, uTerms, newSentDict)        
        
    return newSentDict


def getPredSentDict(sentDict, tweets_file):
    predDict = initPredSentDict(sentDict, tweets_file)
    refinePredSentDict(predDict)
    return predDict


if __name__ == '__main__':
    predDict = getPredSentDict(sys.argv[1], sys.argv[2])
    printSentDict(predDict)
