import json

tweets = []
retweets_list = []
for line in open("farmers-protest-tweets-2021-03-5.json", "r"):
    tweets.append(json.loads(line))


for i in range(len(tweets)):
    retweets_list.append([tweets[i]["url"], tweets[i]["retweetCount"]])

retweets_list = sorted(retweets_list, key=lambda x:x[1], reverse=True)
print(retweets_list)