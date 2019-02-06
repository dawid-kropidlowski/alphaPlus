import unittest

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


if __name__ == '__main__':
    unittest.main()
