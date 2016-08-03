import twitter

from config import (
	TWITTER_CONSUMER_KEY,
	TWITTER_CONSUMER_SECRET,
	TWITTER_ACCESS_TOKEN_KEY,
	TWITTER_ACCESS_TOKEN_SECRET,)

api = twitter.Api(
		consumer_key=TWITTER_CONSUMER_KEY,
		consumer_secret=TWITTER_CONSUMER_SECRET,
		access_token_key=TWITTER_ACCESS_TOKEN_KEY,
		access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

KANYE = '@kanyewest'
MAX_TWEETS = 200

statuses = api.GetUserTimeline(screen_name=KANYE, count=MAX_TWEETS)

with open('kanye.txt', 'w') as f:
	"""Use 'a' for append"""
	for status in statuses:
		try:
			f.write(status.text + '\n')
		except UnicodeEncodeError as e:
			unicode_str = status.text.encode('ascii', 'ignore')
			f.write(unicode_str + '\n')