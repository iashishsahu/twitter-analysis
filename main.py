import tweepy
from textblob import TextBlob
consumer_key='gdEkt0myLE58f1QWT6bXgXBvf'
consumer_secret ='kYP3w0TE7Ogim5P7zHKoIluqwE820ByaLWjosGY9wg7eQsVJpC'
access_token = '1392178314425421824-DpjaDJhuaudq1bzlQjEsuT2l2KZEhs'
access_token_secret ='rwsHRRApBtKm0Asih3hgUPosdcf4NkViLodjX3mwo0vYw'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('Wanda MAximoff')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)