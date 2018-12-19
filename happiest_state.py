# Required imports or library dependencies
import re, sys, json
from tweet_sentiment import *
from stateDict import getStatesDict


# Is the tweet from a certain country?
def isCountry(tweet_json, country = 'United States'):
    try: return tweet_json['place']['country'] == country
    except: return False
    

# Get abbreviated state's form from encrypted place info
# Fill me.
def getStateFromPlace(placeInfo):
    stateABV = placeInfo[-2:]
    return stateABV


# Gets the state (cond. USA) info of the tweet.
def getUSAStateABV(tweet_json):
    try:
        placeInfo = tweet_json['place']['full_name']        
        stateABV = getStateFromPlace(placeInfo)
        return stateABV
    except: ''


# Is the state in the United States?
# Returns true flase.
# Fill me
'''def isStateInUSA(tweet_json, stateList):
    try:

    except: return False'''


# Is the tweet geo coded?
def isGeoEnabled(tweet_json):
    try: return tweet_json['user']['geo_enabled']
    except: return False


# Fill the rest.
# Details explained in class
def mostHappyUSState(sentDict, tweets_file):
    stateSenti = {}
    statesList = getStatesDict()
    tweets_file = open(tweets_file)
    sentDict = genSentDict(sentDict)    
        
    for tweet in tweets_file:
        tweet_json = json.loads(tweet)        
        
        try:
            score = getSentScoreOfTweet(tweet_json, sentDict)
            if isGeoEnabled(tweet_json) and isCountry(tweet_json):
                stateABV = getUSAStateABV(tweet_json)
                try:
                   state = statesList[stateABV]
                   try:stateSenti[state] += score
                   except: stateSenti[state] = score
                except: ''

        except: pass
    for key in stateSenti:
        print(key, stateSenti[key])
    sortDict = sorted(stateSenti, key=stateSenti.get)
    print(sortDict[-1])
        
if __name__ == '__main__':
    mostHappyUSState(sys.argv[1], sys.argv[2])
