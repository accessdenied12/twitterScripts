#!/usr/bin/env python
#
#Dumps tweets from home timeline to stdout
#
import tweepy

consumer_key = "insert consumer key"
consumer_secret = "Insert Consumer Secret"
access_token = "Insert access token"
access_token_secret = "Insert access token secret"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)


public_tweets = api.home_timeline()
for tweet in public_tweets:
	print tweet.text





