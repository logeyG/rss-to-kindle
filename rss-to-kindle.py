#!/usr/bin/python3

import feedparser
import datetime
import random
import requests

# from https://pushtokindle.fivefilters.org/
kindle_domains = {
	'free.kindle.com': 1,
	'kindle.com': 2,
	'kindle.cn': 3,
	'iduokan.com': 4,
	'pbsync': 5}

kindle_email = "{***your kindle email here***}"
# check your kindle email domain, it might be different
kindle_domain = kindle_domains['kindle.com']

# rss feed url of your choice
url = "https://www.theatlantic.com/feed/channel/ideas/"
feed = feedparser.parse(url)
posts_today = []

# get all of today's posts from rss feed
for post in feed.entries:
	date = "%d-%02d-%02d" % (post.published_parsed.tm_year, \
	post.published_parsed.tm_mon, \
	post.published_parsed.tm_mday)

	today = datetime.date.today().strftime('%Y-%m-%d')

	if date == today:
		posts_today.append(post)

# randomly select a single post to send to kindle
daily_post = random.choice(posts_today)

print("running rss to kindle for date: " + today)
print("post title: " + daily_post.title)
print("post link: " + daily_post.link)

# send http request to push to kindle site (generated from postman)
url = "https://pushtokindle.fivefilters.org/send.php"
querystring = {"url":daily_post.link,"context":"send"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
f"Content-Disposition: form-data; name=\"email\"\r\n\r\n{kindle_email}" \
"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
f"Content-Disposition: form-data; name=\"domain\"\r\n\r\n{kindle_domain}" \
"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

headers = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
#print(response.text)