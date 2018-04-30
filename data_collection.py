from __future__ import division
import sys, tweepy, operator
# from tweepy import OAuthHandler
from dateutil.parser import parse
import json
import os
from pattern.en import positive

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

D = 0
M = 0
N = 0
A = 0
B = 0
C = 0

"""api = twitter.api(consumer_key='PeH7lROp4ihy4QyK87FZg', consumer_secret='1BdUkBd9cQK6JcJPll7CkDPbfWEiOyBqqL2KKwT3Og', access_token_key='1683902912-j3558MXwXJ3uHIuZw8eRfolbEGrzN1zQO6UThc7', access_token_secret='e286LQQTtkPhzmsEMnq679m7seqH4ofTDqeArDEgtXw')"""


def get_recent_tweets(user, total_n=50):
    data = {}
    unbiasseddata = {}
    max_id = None
    total = 0
    n = 0

    global D
    global M
    global N
    global A
    global B
    global C

    while True:
        unbiassedtweets = api.search(geocode="44.467186,-73.214804,9mi", screen_name=user, count=total_n, max_id=max_id)

        if len(unbiassedtweets) == 0: break
        for unbiassedtweet in unbiassedtweets:
            n += 1

            if unbiassedtweet.id not in unbiasseddata:
                D += 1
                if positive(unbiassedtweet.text, threshold=0.1):
                    C += 1
                unbiasseddata[unbiassedtweet.id] = str(unbiassedtweet)
                if ("news" in unbiassedtweet.text or "News" in unbiassedtweet.text or "NEWS" in unbiassedtweet.text):
                    N += 1
                    if positive(unbiassedtweet.text, threshold=0.1):
                        B += 1
                        C -= 1
            if n >= total_n: break
        max_id = min([s.id for s in unbiassedtweets]) - 1
        if n >= total_n: break

    # return unbiasseddata.values()

    total = 0
    n = 0
    while True:
        """
        rawtweets = api.user_timeline(screen_name=user, count=total_n, max_id=max_id)
        """
        """rawtweets=api.geo_search(query="USA", granularity="country")
        """
        query = "Elections OR Clinton OR Donald OR Fake OR Hillary OR Obama OR Russian OR Trump OR Fake news OR news"
        rawtweets = api.search(q=query, geocode="39.8,-95.583068847656,2500km", screen_name=user, count=total_n,
                               max_id=max_id)

        if len(rawtweets) == 0: break
        for rawtweet in rawtweets:
            n += 1

            if rawtweet.id not in data:
                data[rawtweet.id] = str(rawtweet)
                if rawtweet.id in unbiasseddata:
                    M += 1
                    if positive(rawtweet.text, threshold=0.1):
                        A += 1
                        C -= 1
                        B -= 1
            if n >= total_n: break
        max_id = min([s.id for s in rawtweets]) - 1
        if n >= total_n: break

    return data.values()


def main():
    fin = "collected_tweets.txt"  # f is the file that stores the tweets that you have collected

    """
    Step 1: Generate the list of screen names of the users in your collected tweets. Each user has an identical screen name.
    """
    screen_names = set()
    for line in open(fin).readlines():
        tweet = json.loads(line)
        screen_name = tweet['user']['screen_name']
        screen_names.add(screen_name)

    """
    p: the number of most recent tweets of each user
    """
    outfile = "sample.txt"
    sample_tweets = []
    p = 2000  # in this example, I set it to 20. You can set a number that you prefered.
    for screen_name in screen_names:
        tweets = get_recent_tweets(screen_name, p)
        sample_tweets.extend(tweets)
    if os.path.exists(outfile):
        os.remove(outfile)
    fout = open(outfile, "a+")
    for tweet in sample_tweets:
        fout.write(json.dumps(tweet) + '\n')
    print "There are {0} unique users in your collected tweets. \nFor each user, {1} historical tweets have been colleced. \n{2} tweets have been collected and stored in the file.".format(
        len(screen_names), p, len(sample_tweets))
    fout.close()

    print "D=", D
    print "M=", M
    print "N=", N
    print "A=", A
    print "B=", B
    print "C=", C

    if not N == 0:
        print "API Recall=", (M / N)
    if not M == 0:
        print "Quality Precision=", (A / M)
    if not (A + B + C) == 0:
        print "Quality Recall=", (A / (A + B + C))


if __name__ == '__main__':
    main()


