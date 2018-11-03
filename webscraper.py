from urllib import request
from datetime import date

class QuoteRetrieval:
    def __init__(self, source = "bossa.pl", start_date = date(1990,1,1), end_date = date.today(),
                 data=['o', 'h', 'l','c', 'v'], tickers = "all"):
        self.source = source
        self.start_date = start_date
        self.end_date = end_date
        self.data = data
        self.tickers = tickers