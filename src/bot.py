import tweepy
import tkinter

consumer_key = 'your_consumer_key_here'
consumer_secret = 'your_consumer_secret_key_here'
access_token = 'your_access_token_here'
access_token_secret = 'your_secret_access_token_here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)
print (user.location)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print("Followed People That Follow You" + user.name)

root = Tk()

