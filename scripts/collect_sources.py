import feedparser
import json

feeds = [
"https://about.fb.com/news/feed/",
"https://techcrunch.com/tag/instagram/feed/",
"https://www.theverge.com/rss/instagram/index.xml"
]

entries = []

for url in feeds:
    feed = feedparser.parse(url)
    for item in feed.entries:
        entries.append({
            "title": item.title,
            "link": item.link,
            "summary": item.summary
        })

with open("updates.json","w") as f:
    json.dump(entries,f)
