from TwitterSearch import *
from pattern.en import positive
import json

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Fake', 'Donald', 'Trump','fake news', 'news']) # let's define all words we would like to have a look for
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key='PeH7lROp4ihy4QyK87FZg',
        consumer_secret='1BdUkBd9cQK6JcJPll7CkDPbfWEiOyBqqL2KKwT3Og',
        access_token='1683902912-j3558MXwXJ3uHIuZw8eRfolbEGrzN1zQO6UThc7',
        access_token_secret= 'e286LQQTtkPhzmsEMnq679m7seqH4ofTDqeArDEgtXw'
    )
    count =0
    fname = open('search_api.txt', 'w')
    for tweet in ts.search_tweets_iterable(tso):
        if positive(tweet['text'], threshold=0.1):
            count = count + 1
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        fname.write(json.dumps(tweet['text']).replace('\"','') + "\n")

    print count

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)