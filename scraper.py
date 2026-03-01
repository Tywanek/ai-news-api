import feedparser
from datetime import datetime, timedelta

def fetch_ai_news():
    url = "https://news.google.com/rss/search?q=Artificial+Intelligence&hl=en-US&gl=US&ceid=US:en"
    response = feedparser.parse(url)
    
    if response.status != 200:
        raise Exception("Failed to fetch RSS feed")
    
    news_items = []
    for entry in response.entries:
        news_item = {
            "title": entry.title,
            "link": entry.link,
            "published_date": entry.published_parsed,
            "summary": entry.summary
        }
        news_items.append(news_item)
    
    return news_items
