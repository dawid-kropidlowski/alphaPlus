from datahandler import DataLoader

ticker = "11BIT"
load_ticker = DataLoader(ticker=ticker)
load_ticker.load_quotes()

# new_quotes = webscraper.QuoteRetriever()

# new_quotes.save_quotes()
