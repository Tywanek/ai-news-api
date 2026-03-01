from flask import Flask, jsonify
import scraper
from cachetools import cached, TTLCache

app = Flask(__name__)

@cached(cache=TTLCache(maxsize=128, ttl=900))  # Cache for 15 minutes (900 seconds)
def get_cached_ai_news():
    try:
        return scraper.fetch_ai_news()
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/')
def status():
    return jsonify({"status": "ok"})

@app.route('/news')
def news():
    news_items = get_cached_ai_news()
    if isinstance(news_items, tuple):
        return news_items
    return jsonify([{"title": item["title"], "link": item["link"], "published_date": item["published_date"].isoformat(), "summary": item["summary"]} for item in news_items])
