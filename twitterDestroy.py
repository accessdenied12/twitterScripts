#!/usr/bin/env python
#
#Delete tweets and unfavorite previously favorited tweets
#
import tweepy

consumer_key = "insert consumer key"
consumer_secret = "Insert Consumer Secret"
access_token = "Insert access token"
access_token_secret = "Insert access token secret"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



for status in tweepy.Cursor(api.user_timeline).items():
	api.destroy_status(status.id)
	print status.text

unfavorite_count = 0
for favorite in tweepy.Cursor(api.favorites).items():
	unfavorite_count += 1
	try:
		print "Un-liking %d: %s %s" % (favorite.id, favorite.created_at, favorite.text)
		api.destroy_favorite(favorite.id)
	except tweepy.TweepError :
		print "Rate Limit Exceeded, sleeping for 15 minutes, error code %s" % (tweepy.TweepError)
		time.sleep(60 * 15)
		continue


print "We unfavorited %s tweets" % (unfavorite_count)

			
