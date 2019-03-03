import os
from datetime import date
from json import load


class DataLoader:
    # initialize object, ticker is necessary
    def __init__(self, ticker, start_date=date(1900, 1, 1), end_date=date.today(), quote_type='close',
                 data_location='data'):

        if type(ticker) == str:
            self._ticker = ticker
        elif ticker is None:
            raise NameError("ticker is missing, provide a ticker first!")
        else:
            raise TypeError("ticker should be of type str")

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

        if type(data_location) == str:
            self._data_location = os.path.join(os.path.dirname(__file__), data_location)
        else:
            raise TypeError("data_location should of str type and point to folder where data are stored")

        self._quotes = {}

    # method to read quotes from a file
    def _load_quotes(self):
        # open the appropriate file corresponding to requested ticker
        with open(os.path.join(self._data_location, "%s.json" % self._ticker), 'r') as data_file:

            # load contents of a file to a Python object using the json module
            quotes_json = load(data_file)
            data_file.close()

            # iterate quotes date by date
            for dates_str in quotes_json:

                year = int(dates_str[:4])
                month = int(dates_str[4:6])
                day = int(dates_str[6:8])

                dates = date(year, month, day)

                # if a quote is in the set time interval then load it
                if self._start_date <= dates <= self._end_date:
                    self._quotes[dates_str] = float(quotes_json[dates_str][self._quote_type])

    # a public method to get quotes
    def get_quotes(self):
        self._load_quotes()
        return self._quotes
