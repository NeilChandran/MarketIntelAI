import requests
import csv
import time

class FinancialScraper:
    def __init__(self, tickers):
        self.tickers = tickers
        self.api_url = "https://query1.finance.yahoo.com/v7/finance/quote"
        self.results = []

    def fetch_data(self, ticker):
        try:
            params = {"symbols": ticker}
            response = requests.get(self.api_url, params=params, timeout=5)
            data = response.json()
            quote = data["quoteResponse"]["result"][0]
            return {
                "ticker": ticker,
                "price": quote.get("regularMarketPrice"),
                "market_cap": quote.get("marketCap"),
                "pe_ratio": quote.get("trailingPE"),
                "eps": quote.get("epsTrailingTwelveMonths"),
                "sector": quote.get("sector", "N/A")
            }
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return None

    def scrape_all(self):
        for ticker in self.tickers:
            data = self.fetch_data(ticker)
            if data:
                self.results.append(data)
            time.sleep(1)

    def save_to_csv(self, filename):
        if not self.results:
            print("No results to save.")
            return
        keys = self.results[0].keys()
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.results)
        print(f"Saved results to {filename}")

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA"]
    scraper = FinancialScraper(tickers)
    scraper.scrape_all()
    scraper.save_to_csv("company_financials.csv")
