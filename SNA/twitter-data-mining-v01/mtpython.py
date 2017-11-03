import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'Ur5J5gHT6uYg7zms7GaLUNYWf'
consumer_secret = 'SXSyveGpYiTzjifwC84IZ7IJBP7Lx138nODPhGW7CkykjIKTyu'
access_token = '2471507719-kvni00S7JySj8Iq3PUD80d01jrh8HpSodLnoABo'
access_secret = 'EjbRRnAf9E8CgedjX9qBZ2XZABnRGI8vHeHft50CU6f8S'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
