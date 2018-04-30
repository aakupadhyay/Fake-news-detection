import json

fn = 'data/2017_05_15/data.txt'
out = open('fakenews.txt','w')

for line in open(fn).readlines():
    datum = json.loads(line)
    if 'retweeted' in datum :
        if(datum['retweeted'] == False):
            # print True
            out.write(json.dumps(datum['text']).replace('\"','') + '\n')