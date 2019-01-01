import webscraper

new_quotes = webscraper.QuoteRetrieval(last_day_close=False, headers=True, start_date="test")

# new_quotes.save_quotes()
