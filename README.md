# rss-to-kindle
Reads an RSS feed and pushes a random post of the day to your kindle, utilizing the excellent service [PushToKindle](https://www.fivefilters.org/push-to-kindle/).

### Usage
`pip install feedparser`

`python3 rss-to-kindle.py`

I've got this running via a cron job on my raspberry pi:
```
# runs rss-to-kindle every day at 5pm
0 17 * * * python3 /home/pi/rss-to-kindle.py >> /home/pi/rss-to-kindle.log 2>&1
```
