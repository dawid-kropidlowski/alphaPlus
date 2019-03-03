import os
import unittest
from datetime import date

from datahandler import DataLoader
from financialengine import DescriptiveStatistics
from webscraper import QuoteRetriever


class IntegrationTests(unittest.TestCase):

    def test_data_flow(self):
        test_path = os.path.dirname(__file__)
        test_path = os.path.join(os.path.split(test_path)[0], "data")

        try:
            os.remove(os.path.join(test_path, "11BIT.json"))
        except FileNotFoundError:
            pass

        test_data_retriever = QuoteRetriever(last_day_close=False, headers=True)

        test_data_retriever.save_quotes()

        test_data = DataLoader("11BIT", date(2018, 11, 1), date(2018, 11, 30)).get_quotes()

        average = DescriptiveStatistics(test_data).average()
        self.assertEqual(round(average, 2), 273.35)
