import os
import zipfile
from datetime import date
from json import load, dump
from urllib import request


class QuoteRetrieval:

    def __init__(self, source="bossa.pl", start_date=date(1990, 1, 1), end_date=date.today(), last_day_close=True,
                 fin_instrument="stock", tickers="all", headers=False):
        """
        QuoteRetrieval is used to retrieve quotes from the web, reformat them as a dictionary that is then saved in a
        .json file

        :param source: web portal from which the data is to be retrieved (currently only bossa.pl is implemented)
        :param start_date: date from when data will be retrieved
        :param end_date: date to when data will be retrieved
        :param last_day_close: boolean indicating if data should be last day close or not, if True then start_date and
            end_date are ignored
        :param fin_instrument: indicates data on which financial instruments should be retrieved (currently only stocks
            have been implemented)
        :param tickers: list of tickers or other similar identification of financial instruments to be retrieved
        :param headers: boolean indicating whether the source file has headers or not, if True then first line of source
            file will be ignored
        """
        self._source = source

        if type(start_date) == date:
            self._start_date = start_date
        else:
            raise ValueError("start_date must be of date type")

        if type(end_date) == date:
            self._end_date = end_date
        else:
            raise ValueError("end_date must be of date type")

        if type(last_day_close) == bool:
            self._last_day_close = last_day_close
        else:
            raise ValueError("last_day_close must be of date type")

        if tickers == str or tickers == list:
            self._tickers = tickers
        else:
            raise ValueError("tickers must be of str or list type")

        if fin_instrument == str:
            self._fin_instrument = fin_instrument
        else:
            raise ValueError("fin_instrument must be of str type")

        if headers == bool:
            self._headers = headers
        else:
            raise ValueError("headers must be of bool type")

        self._url = ""
        self._data = {}
        self._quotes = {}
        self._headers_back = False
        self._load_configuration()
        self._retrieve_quotes()

    def _load_configuration(self):

        # open configuration file

        config_file = open('config.json', 'r')
        cnfg = load(config_file)
        config_file.close()

        if self._last_day_close:
            date_range = "last day close"
        else:
            date_range = "full range"

        cnfg = cnfg["sources"][self._source]["type"][self._fin_instrument]["range"][date_range]

        # load url containing the data and structure

        self._url = cnfg["url"]
        self._data = cnfg["data"]

    def _retrieve_quotes(self):

        # there is a different way to retrieve data from .zip files and different for text-like files (csv etc.)
        if self._url.split('.')[len(self._url.split('.')) - 1] != 'zip':

            # open url containing data and load data
            with request.urlopen(self._url) as quotes_file:
                self._read_quotes_file(quotes_file)

        # retrieve data from .zip file
        else:
            temp_data_path = 'data\\temporary'

            # create a folder to keep temporary data in
            if not os.path.exists(temp_data_path):
                os.mkdir(temp_data_path)

            if os.path.exists('%s\\quotes_datafile.zip' % temp_data_path):
                os.remove('%s\\quotes_datafile.zip' % temp_data_path)

            # retrieve zip from url and save it in temporary folder
            request.urlretrieve(self._url, '%s\\quotes_datafile.zip' % temp_data_path)

            # go through the zip and open files containing quotes for given tickers
            with zipfile.ZipFile('%s\\quotes_datafile.zip' % temp_data_path, 'r') as data_zip:
                # if all tickers from the file are required then go through all the quotes and extract them
                if self._tickers == 'all':
                    for data_file in data_zip.filelist:
                        with data_zip.open(data_file, 'r') as quotes_file:
                            self._read_quotes_file(quotes_file)
                else:
                    for ticker in self._tickers:
                        with data_zip.open('%s.mst' % ticker, 'r') as quotes_file:
                            self._read_quotes_file(quotes_file)

    def _read_quotes_file(self, quotes_file):

        if self._headers_back:
            self._headers_back = False
            self._headers = True

        # read the file
        for line in quotes_file:
            # decoding data as they are seen by Python as binary
            if self._headers:
                self._headers = False
                self._headers_back = True
                continue

            daily_quotes = line.decode()
            daily_quotes = daily_quotes.split(',')

            ticker = daily_quotes[self._data["ticker"] - 1]

            if ticker in self._tickers or self._tickers == "all":

                quote_date_str = daily_quotes[self._data["date"] - 1]
                quote_date = date(int(quote_date_str[:4]), int(quote_date_str[4:6]), int(quote_date_str[6:]))

                if self._start_date <= quote_date <= self._end_date or self._last_day_close:
                    if ticker in self._quotes:
                        pass
                    else:
                        self._quotes[ticker] = {}

                    self._quotes[ticker][quote_date_str] = {}

                    # assign values
                    for key in self._data:
                        if key == "ticker" or key == "date":
                            continue
                        else:
                            self._quotes[ticker][quote_date_str][key] = daily_quotes[self._data[key] - 1].replace(
                                "\r\n", "")

        quotes_file.close()

    def save_quotes(self):

        # open file to add data
        for ticker in self._quotes:

            # check if there is a file with quotes for this ticker
            try:
                with open("data\%s.json" % ticker, "r") as quotes_data_file:
                    # load quotes from file
                    daily_quotes_data = load(quotes_data_file)
                    quotes_data_file.close()

                # check if there are already entries for a given date, if yes, then move on
                try:
                    for quote_date in self._quotes[ticker]:
                        if quote_date not in daily_quotes_data:
                            daily_quotes_data[quote_date] = self._quotes[ticker][quote_date]
                except ValueError:
                    continue

                with open("data\%s.json" % ticker, "w") as quotes_data_file:
                    dump(daily_quotes_data, quotes_data_file)
                    quotes_data_file.close()
                    del daily_quotes_data

            except (FileNotFoundError, ValueError):

                # there is no such file yet so it needs to be created or file exists but is empty
                daily_quotes_data = {}
                for quote_date in self._quotes[ticker]:
                    daily_quotes_data[quote_date] = self._quotes[ticker][quote_date]

                with open("data\%s.json" % ticker, "w") as quotes_data_file:
                    dump(daily_quotes_data, quotes_data_file)
                    quotes_data_file.close()
                    del daily_quotes_data
