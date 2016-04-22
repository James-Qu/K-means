import json as simplejson
import re

#commandline arg
numOfCluster=10
iniSeedFile="InitialSeeds.txt"
ttDataFile="Tweets.json"
output="output.txt"

#import data
File=open(ttDataFile)
#inputTweet = {}
inputTweet=[]
for line in File.readlines():
    data=simplejson.loads(line)
    test=data['text'].replace('\u',' ')
    test = re.sub(r"http://[a-zA-Z0-9-\./]* ", " ", test)
    test = re.sub(r"http://[a-zA-Z0-9-\./]*$", " ", test)
    test=re.sub(r'[^\w]', ' ', test)
    test=test.lower()
    print test
    inputTweet.append([data['id'],test])
    #inputTweet={'id':data['id'],'content':test}
    #inputTweet[data['id']]=test
    #inputTweet['content']=test
print inputTweet
#print inputTweet[323929272685318147]

# get id_array and content_array
idArray=[]
contentArray=[]
for tweet in inputTweet:
    idArray.append(tweet[0])
    words=[]
    for w in tweet[1].split(" "):
        if w not in words:
            #print 'W:',w
            words.append(w)
    contentArray.append(words)
#print idArray,contentArray

# method take two word lists and return jaccard distance
def jaccard(b,c):
    union=0
    intersection=0
    for word in b:
        if word in c:
            intersection=intersection+1
    union=len(b)+len(c)-intersection
    print 'union:',union
    print 'inter:',intersection
    result=1-float(intersection)/float(union)
    return result

print jaccard(inputTweet[66],inputTweet[67])
print inputTweet[66]
print inputTweet[67]