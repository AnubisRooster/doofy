# Using a CSV file that was exported from =Spotify, plug it into the CSV reader down below.
# Change the second number in the range function to the number of songs that are in the playlist
import random

num = random.choice(range(2, 572))
x = num
import csv

with open("list.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    data = [row for row in csv.reader(csvfile)]
song_name = data[x][0]
artist_name = data[x][1]
song_id = data[x][5]

#Now that the bot has the song, input your twitter API info down below

import tweepy

consumer_key = ("yourkey")
consumer_secret = ("yoursecretkey")
access_token = ("accesstoken")
access_token_secret = ( "tokensecret")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

# this allows you to add a link to the tweet if you choose to do so

print(song_name + ' by ' + artist_name + '\n')
url_link = input('Add link here:')

# update the status
api.update_status(
    status="Slade's Spin of the Day" '\n #SSTD \n' + song_name + " by " + artist_name + " \n" + "#" + artist_name.replace(
        " ", "") + '\n' + url_link)
print('Tweet Posted! \n Have a Nice Day!')
