import os
import unittest
from datetime import date

from datahandler import DataLoader
from financialengine import DescriptiveStatistics, VarianceCovarianceAnalyser


class TestDescriptiveStatistics(unittest.TestCase):

    def test_average(self):
        test_quotes = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "close",
                                 "").get_quotes()
        average_closing_price = DescriptiveStatistics(test_quotes).average()

        self.assertEqual(average_closing_price, 15.9)

    def test_std_dev(self):
        test_quotes = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "close",
                                 "").get_quotes()
        std_dev = DescriptiveStatistics(test_quotes).standard_deviation()

        self.assertEqual(round(std_dev, 5), 3.12357)

    def test_variance(self):
        test_quotes = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "close",
                                 "").get_quotes()
        variance = DescriptiveStatistics(test_quotes).variance()
        self.assertEqual(round(variance, 14), 9.75666666666667)


class TestVarianceCovarianceAnalyser(unittest.TestCase):

    def test_covariance_equal_sets(self):
        test_quotes1 = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "close",
                                  "").get_quotes()
        test_quotes2 = DataLoader(os.path.join("tests", "test_data2"), date(2018, 11, 1), date(2018, 11, 30), "close",
                                  "").get_quotes()

        covariance = VarianceCovarianceAnalyser(test_quotes1, test_quotes2).covariance()

        self.assertEqual(round(covariance, 11), 0.02666666667)

    def test_covariance_different_sets(self):
        test_quotes1 = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "close",
                                  "").get_quotes()
        test_quotes2 = DataLoader(os.path.join("tests", "test_data3"), date(2018, 11, 1), date(2018, 11, 30), "close",
                                  "").get_quotes()

        covariance = VarianceCovarianceAnalyser(test_quotes1, test_quotes2).covariance()

        self.assertEqual(round(covariance, 11), -0.30202140309)

    def test_covariance_same_data(self):
        test_quotes1 = DataLoader(os.path.join("tests", "test_data"), date(2018, 11, 1), date(2018, 11, 30), "close",
                                  "").get_quotes()

        covariance = VarianceCovarianceAnalyser(test_quotes1, test_quotes1).covariance()
        variance = DescriptiveStatistics(test_quotes1).variance()

        self.assertEqual(covariance, variance)
