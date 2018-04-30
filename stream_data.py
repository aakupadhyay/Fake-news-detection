
import tweepy  # twitter api module - python version
import datetime  # python datetime module
import json  # python json module
import os  # python os module, used for creating folders

OAuth = tweepy.OAuthHandler('PeH7lROp4ihy4QyK87FZg', '1BdUkBd9cQK6JcJPll7CkDPbfWEiOyBqqL2KKwT3Og')
OAuth.set_access_token('1683902912-j3558MXwXJ3uHIuZw8eRfolbEGrzN1zQO6UThc7',
                       'e286LQQTtkPhzmsEMnq679m7seqH4ofTDqeArDEgtXw')


class StreamListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        output_folder_date = 'data/{0}'.format(datetime.datetime.now().strftime('%Y_%m_%d'))
        if not os.path.exists(output_folder_date): os.makedirs(output_folder_date)
        output_file = output_folder_date + '/data.txt'
        try:
            jdata = json.loads(str(raw_data))
            f = open(output_file, 'a+')
            f.write(json.dumps(jdata) + '\n')
            f.close()
        except:
            print 'Data writing exception.'


def main():
    while (True):
        sl = StreamListener()
        stream = tweepy.Stream(OAuth, sl)
        try:
            stream.filter(track=['News', 'fake', 'donald', 'trump', 'russian', 'clinton', 'hillary', 'AlexJones', 'fakenews', 'obama'])
        except:
            print 'Exception occur!'


if __name__ == '__main__':
    main()
