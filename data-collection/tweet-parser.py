import twitter
from twitter import TwitterError

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
MAX_TWEETS = 1000
fname = 'kanye'
file = '.'.join([fname, 'txt'])

with open(file, 'w') as f:
    """Use 'a' for append"""
    tweet_count = 0
    MAX_TWEETS = 0
    # Max id is a parameter which returns the data only previous to it
    MAX_ID = None

    try:
        while True:
            statuses = api.GetUserTimeline(screen_name=KANYE, max_id=MAX_ID)
            num_tweets = len(statuses)
            MAX_TWEETS += num_tweets

            if num_tweets == 0:
                # No more tweets
                break
            
            MAX_ID = min(statuses, key=lambda x: x.id).id
            
            for status in statuses:
                
                try:
                    f.write(status.text + '\n')

                except UnicodeEncodeError as e:
                    # Ignore ascii for now
                    unicode_str = status.text.encode('ascii', 'ignore')
                    f.write(unicode_str + '\n')
                
                else:
                    tweet_count += 1 

            print "%d/%d tweets written" % (tweet_count, MAX_TWEETS)
    
    except TwitterError as e:
        
        print e
        print "Possibly no more api requests"

print file, "finished writing"