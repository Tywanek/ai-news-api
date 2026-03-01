from fastapi import FastAPI, HTTPException
import scraper
from cachetools import cached, TTLCache
from datetime import datetime
import time

app = FastAPI()

@cached(cache=TTLCache(maxsize=128, ttl=900))  # Cache for 15 minutes (900 seconds)
def get_cached_ai_news():
    try:
        return scraper.fetch_ai_news()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/news", response_model=list[dict])
async def news():
    news_items = get_cached_ai_news()
    return [{"title": item["title"], "link": item["link"], "published_date": datetime.fromtimestamp(time.mktime(item["published_date"])).isoformat(), "summary": item["summary"]} for item in news_items]
