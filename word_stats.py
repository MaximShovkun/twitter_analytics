import csv

rows = csv.reader(open('realDonaldTrump_tweets.csv'))
reetwets_cout = 0
tweets_cout = 0
for row in rows:
    word = row[2]
    if word.startswith("b'RT") or word.startswith('b"RT'):
        reetwets_cout += 1
    else:
        tweets_cout += 1
print('Tw: {}, Rt: {}'.format(tweets_cout, reetwets_cout))
