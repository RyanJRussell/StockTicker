import requests
import yfinance as yf
import time
import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
STOCK_SYMBOLS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
MUTUAL_FUNDS = ['FXAIX']
REFRESH_INTERVAL = 10  # seconds

def fetch_stock_price(symbol):
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}'
    try:
        response = requests.get(url)
        data = response.json()
        price = data.get('c')
        return f"{symbol}: ${price:.2f}" if price else f"{symbol}: N/A"
    except Exception as e:
        return f"{symbol}: Error"

def fetch_fund_price(symbol):
    try:
        fund = yf.Ticker(symbol)
        price = fund.info.get('regularMarketPrice')
        return f"{symbol}: ${price:.2f}" if price else f"{symbol}: N/A"
    except Exception:
        return f"{symbol}: Error"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("=== Stock & Fund Ticker ===")
        stock_prices = [fetch_stock_price(sym) for sym in STOCK_SYMBOLS]
        fund_prices = [fetch_fund_price(sym) for sym in MUTUAL_FUNDS]
        print(" | ".join(stock_prices + fund_prices))
        time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    main()
