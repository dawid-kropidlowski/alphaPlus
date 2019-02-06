import unittest
from datetime import date

from datahandler import DataLoader


class DataHandlerInitializerTest(unittest.TestCase):
    def test_ticker_type(self):
        ticker = 20
        with self.assertRaises(TypeError):
            DataLoader(ticker=ticker)

    def test_start_date_type(self):
        start_date = "wrong date"
        with self.assertRaises(TypeError):
            DataLoader(start_date=start_date, ticker="11BIT")

    def test_end_date(self):
        end_date = "wrong date"
        with self.assertRaises(TypeError):
            DataLoader(end_date=end_date, ticker="11BIT")

    def test_quote_type(self):
        quote_type = 20
        with self.assertRaises(TypeError):
            DataLoader(quote_type=quote_type, ticker="11BIT")


class TestDataLoading(unittest.TestCase):
    def test_open_quotes(self):
        test_quotes = DataLoader("test_data", date(2018, 11, 1), date(2018, 11, 30), "open", "tests")

        open_quotes = [12.0, 12.0, 18.0, 11.0, 19.0, 17.0, 14.0, 15.0, 14.0, 10.0, 17.0, 17.0, 18.0, 16.0, 11.0, 19.0,
                       20.0, 11.0, 19.0, 15.0, 14.0, 20.0, 20.0, 16.0, 20.0, 20.0, 14.0, 16.0, 18.0, 15.0]

        self.assertEqual(test_quotes.get_quotes(), open_quotes)


if __name__ == '__main__':
    unittest.main()
