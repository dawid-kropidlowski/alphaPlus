from datetime import date
from json import load


class DataLoader:
    def __init__(self, ticker, start_date=date(1900, 1, 1), end_date=date.today(), quote_type='close'):

        if type(ticker) == str:
            self._ticker = ticker
        else:
            raise TypeError("ticker should be of type str.")

        if type(start_date) == date:
            self._start_date = start_date
        else:
            raise TypeError("start_date should be of type date")

        if type(end_date) == date:
            self._end_date = end_date
        else:
            raise TypeError("end_date should be of type date")

        if type(quote_type) == str:
            self._quote_type = quote_type
        else:
            raise TypeError("quote_type should be of type str")

        self._quotes = []

    def load_quotes(self):
        with open("data\\%s.json" % self._ticker, 'r') as data_file:

            quotes_json = load(data_file)

            for dates_str in quotes_json:

                year = int(dates_str[:4])
                month = int(dates_str[4:6])
                day = int(dates_str[6:8])

                dates = date(year, month, day)

                if self._start_date <= dates <= self._end_date:
                    self._quotes.append(float(quotes_json[dates_str][self._quote_type]))

    def get_quotes(self):
        return self._quotes
