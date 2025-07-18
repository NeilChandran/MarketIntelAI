import requests
from datetime import datetime
import csv

class MarketTrendsReporter:
    def __init__(self, keywords):
        self.keywords = keywords
        self.api_key = "DEMO_KEY"  # Replace with real key for production API
        self.endpoint = "https://newsapi.org/v2/everything"
        self.results = []

    def query_news(self, query, days=7):
        today = datetime.now()
        from_param = (today - timedelta(days=days)).strftime('%Y-%m-%d')
        try:
            params = {
                "q": query,
                "from": from_param,
                "sortBy": "publishedAt",
                "language": "en",
                "apiKey": self.api_key
            }
            resp = requests.get(self.endpoint, params=params, timeout=10)
            articles = resp.json().get("articles", [])
            for art in articles:
                self.results.append({
                    "keyword": query,
                    "title": art.get("title"),
                    "url": art.get("url"),
                    "publishedAt": art.get("publishedAt"),
                })
        except Exception as e:
            print(f"Error fetching news for {query}: {e}")

    def generate_report(self):
        for kw in self.keywords:
            self.query_news(kw)

    def save_to_csv(self, fname):
        if not self.results:
            print("No articles to save.")
            return
        keys = self.results[0].keys()
        with open(fname, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(self.results)
        print(f"Saved report to {fname}")

if __name__ == "__main__":
    keywords = ["startup", "funding", "series A", "product launch", "technology"]
    reporter = MarketTrendsReporter(keywords)
    reporter.generate_report()
    reporter.save_to_csv("market_trends.csv")

