import tweepy
from time import sleep

CONSUMER_KEY = 'yg8X18mjPzVqqNSrvem0edR9m'
CONSUMER_SECRET = 'VcHMmcmbsS8oj5KtfD9XPlfnL3T4HQIsqthHrUPs063HSY6Fhn'
ACCESS_KEY = '3256983120-BapNg0Ec7t6QNjw9xWl9PkVFk2VVKJ6pTcXhRod'
ACCESS_SECRET = 'LA7PrJTUQnA8sHiyhrKQurCVDSQNFC3dv6YJpzH5rveSU'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

print("just a few more steps to finish this bot \n")

q = input('Which hashtag do you to want search? ')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notif=True)


for tweet in tweepy.Cursor(api.search, q='#'+q).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        # Follow the user who tweeted
        tweet.user.follow()
        print('Followed the user')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break