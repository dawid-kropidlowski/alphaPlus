import os
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

    def test_freq_type(self):
        freq = 10
        with self.assertRaises(TypeError):
            DataLoader(freq=freq, ticker="11BIT")

    def test_freq_values(self):
        freq = 'b'
        with self.assertRaises(ValueError):
            DataLoader(freq=freq, ticker="11BIT")


class TestDataLoading(unittest.TestCase):

    def test_open_quotes(self):
        test_quotes = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "open", "")

        open_quotes = {'20181101': 12.0, '20181102': 12.0, '20181103': 18.0, '20181104': 11.0, '20181105': 19.0,
                       '20181106': 17.0, '20181107': 14.0, '20181108': 15.0, '20181109': 14.0, '20181110': 10.0,
                       '20181111': 17.0, '20181112': 17.0, '20181113': 18.0, '20181114': 16.0, '20181115': 11.0,
                       '20181116': 19.0, '20181117': 20.0, '20181118': 11.0, '20181119': 19.0, '20181120': 15.0,
                       '20181121': 14.0, '20181122': 20.0, '20181123': 20.0, '20181124': 16.0, '20181125': 20.0,
                       '20181126': 20.0, '20181127': 14.0, '20181128': 16.0, '20181129': 18.0, '20181130': 15.0}

        self.assertEqual(test_quotes.get_quotes(), open_quotes)

    def test_high_quotes(self):
        test_quotes = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "high", "")

        high_quotes = {'20181101': 16.0, '20181102': 15.0, '20181103': 17.0, '20181104': 19.0, '20181105': 14.0,
                       '20181106': 12.0, '20181107': 20.0, '20181108': 19.0, '20181109': 16.0, '20181110': 19.0,
                       '20181111': 10.0, '20181112': 11.0, '20181113': 12.0, '20181114': 14.0, '20181115': 15.0,
                       '20181116': 10.0, '20181117': 15.0, '20181118': 17.0, '20181119': 20.0, '20181120': 13.0,
                       '20181121': 13.0, '20181122': 13.0, '20181123': 17.0, '20181124': 12.0, '20181125': 10.0,
                       '20181126': 11.0, '20181127': 16.0, '20181128': 11.0, '20181129': 16.0, '20181130': 18.0}

        self.assertEqual(test_quotes.get_quotes(), high_quotes)

    def test_low_quotes(self):
        test_quotes = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "low", "")

        low_quotes = {'20181101': 17.0, '20181102': 18.0, '20181103': 12.0, '20181104': 11.0, '20181105': 20.0,
                      '20181106': 16.0, '20181107': 13.0, '20181108': 16.0, '20181109': 17.0, '20181110': 13.0,
                      '20181111': 18.0, '20181112': 11.0, '20181113': 18.0, '20181114': 13.0, '20181115': 20.0,
                      '20181116': 17.0, '20181117': 14.0, '20181118': 18.0, '20181119': 15.0, '20181120': 14.0,
                      '20181121': 10.0, '20181122': 15.0, '20181123': 18.0, '20181124': 10.0, '20181125': 19.0,
                      '20181126': 19.0, '20181127': 19.0, '20181128': 13.0, '20181129': 12.0, '20181130': 15.0}

        self.assertEqual(test_quotes.get_quotes(), low_quotes)

    def test_close_quotes(self):
        test_quotes = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "close", "")

        close_quotes = {'20181101': 12.0, '20181102': 18.0, '20181103': 11.0, '20181104': 19.0, '20181105': 17.0,
                        '20181106': 14.0, '20181107': 15.0, '20181108': 14.0, '20181109': 10.0, '20181110': 17.0,
                        '20181111': 17.0, '20181112': 18.0, '20181113': 16.0, '20181114': 11.0, '20181115': 19.0,
                        '20181116': 20.0, '20181117': 11.0, '20181118': 19.0, '20181119': 15.0, '20181120': 14.0,
                        '20181121': 20.0, '20181122': 20.0, '20181123': 16.0, '20181124': 20.0, '20181125': 20.0,
                        '20181126': 14.0, '20181127': 16.0, '20181128': 18.0, '20181129': 15.0, '20181130': 11.0}

        self.assertEqual(test_quotes.get_quotes(), close_quotes)

    def test_volumes(self):
        test_volumes = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "volume",
                                  "")

        volumes = {'20181101': 7911.0, '20181102': 6831.0, '20181103': 1892.0, '20181104': 1824.0, '20181105': 1169.0,
                   '20181106': 1090.0, '20181107': 5869.0, '20181108': 7072.0, '20181109': 4181.0, '20181110': 3971.0,
                   '20181111': 4776.0, '20181112': 5232.0, '20181113': 3122.0, '20181114': 6601.0, '20181115': 1276.0,
                   '20181116': 1483.0, '20181117': 6479.0, '20181118': 2294.0, '20181119': 5622.0, '20181120': 6252.0,
                   '20181121': 5422.0, '20181122': 6811.0, '20181123': 5853.0, '20181124': 6692.0, '20181125': 7188.0,
                   '20181126': 4200.0, '20181127': 5709.0, '20181128': 3278.0, '20181129': 4914.0, '20181130': 1508.0}

        self.assertEqual(test_volumes.get_quotes(), volumes)

    def test_frequency_w(self):
        test_quotes = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "close", "",
                                 freq='w')

        close_quotes = {'20181101': 12.0, '20181108': 14.0, '20181115': 19.0, '20181122': 20.0, '20181129': 15.0}

        self.assertEqual(test_quotes.get_quotes(), close_quotes)

    def test_frequency_m(self):
        test_quotes = DataLoader(os.path.join("tests", "11BIT_test"), date(2018, 5, 2), date(2018, 11, 30), "close", "",
                                 freq='m')

        close_quotes = {'20180502': 350.00, '20180604': 488.00, '20180704': 434.00, '20180806': 441.00,
                        '20180906': 335.50, '20181008': 303.50, '20181108': 295.00}

        self.assertEqual(test_quotes.get_quotes(), close_quotes)

    def test_frequency_y(self):
        test_quotes = DataLoader(os.path.join("tests", "11BIT_test"), date(2017, 1, 2), date(2018, 11, 30), "close", "",
                                 freq='y')

        close_quotes = {'20170102': 147.10}

        self.assertEqual(test_quotes.get_quotes(), close_quotes)


if __name__ == '__main__':
    unittest.main()
