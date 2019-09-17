import requests as r
import tweepy 

consumer_key = 'QFKYIB0rcjNOn0cO9bIfn5QRg'
consumer_secret = 'gAguz7Iw4J1uGtnyir6JLnRy0h7ftH2dm3BMtNTACgHRF3VOOl'
access_key = '850685620796227584-ncWVgjdfO1bEQARuxcSFQybhSWTto9x'
access_secret = 'HRYSqgwC8gCiPqKNYHz1PXkiOlWJXqP5BZ21QuCeAnDPi'

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

result = api.user_timeline(screen_name = 'realDonaldTrump', count=200)
print(result)
total_count = len(result)
while len(result) > 0:
    oldest = result[-1].id - 1

    print('Trying to get tweets for id > {}'.format(oldest))

    result = api.user_timeline(screen_name = 'realDonaldTrump', count=200,max_id=oldest)
    total_count += len(result)
    print(result)

print(total_count)



		