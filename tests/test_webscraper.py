import unittest

from webscraper import QuoteRetriever


class QuoteRetrievalInitializerTest(unittest.TestCase):
    def test_start_date(self):
        start_date = "wrong_data_type"
        with self.assertRaises(TypeError):
            QuoteRetriever(start_date=start_date)

    def test_end_date(self):
        end_date = "wrong_data_type"
        with self.assertRaises(TypeError):
            QuoteRetriever(end_date=end_date)

    def test_last_day_close(self):
        last_day_close = "wrong_data_type"
        with self.assertRaises(TypeError):
            QuoteRetriever(last_day_close=last_day_close)

    def test_tickers(self):
        tickers = 10
        with self.assertRaises(TypeError):
            QuoteRetriever(tickers=tickers)

    def test_fin_instrument(self):
        fin_instrument = 10
        with self.assertRaises(TypeError):
            QuoteRetriever(fin_instrument=fin_instrument)

    def test_headers(self):
        headers = "wrong_data_type"
        with self.assertRaises(TypeError):
            QuoteRetriever(headers=headers)


if __name__ == '__main__':
    unittest.main()
