class DescriptiveStatistics:

    def __init__(self, quotes_series):

        if type(quotes_series) == dict:
            self._quotes_series = quotes_series
        else:
            raise TypeError("quotes_series should be a dictionary with dates as keys and quotes as values!")

    def average(self):

        sum = 0
        count = 0

        for quote_date in self._quotes_series:
            sum += self._quotes_series[quote_date]
            count += 1

        try:
            avg = sum / count
        except ZeroDivisionError:
            avg = 0

        return avg

    def standard_deviation(self):

        sum = 0
        count = 0
        avg = self.average()

        for quote_date in self._quotes_series:
            sum += (self._quotes_series[quote_date] - avg) ** 2
            count += 1
        try:
            std_dev = (sum / count) ** 0.5
        except ZeroDivisionError:
            std_dev = 0

        return std_dev

    def variance(self):

        sum = 0
        count = 0
        avg = self.average()

        for quote_date in self._quotes_series:
            sum += (self._quotes_series[quote_date] - avg) ** 2
            count += 1
        try:
            var = sum / count
        except ZeroDivisionError:
            var = 0

        return var

class VarianceCovarianceAnalyser:

    def __init__(self, quotes_set1, quotes_set2, skip_non_matching=True):

        if type(quotes_set1) == dict:
            self._quotes_set1 = quotes_set1
        else:
            raise TypeError("quotes_set1 should be a dictionary with dates as keys and quotes as values!")

        if type(quotes_set2) == dict:
            self._quotes_set2 = quotes_set2
        else:
            raise TypeError("quotes_set2 should be a dictionary with dates as keys and quotes as values!")

        if type(skip_non_matching) == bool:
            self._skip_non_matching = skip_non_matching
        else:
            raise TypeError("skip_non_matching is a boolean operator")

        # making sure that first set of quotes is longer in case of differences in lengths
        if len(self._quotes_set1) < len(self._quotes_set2):
            temp_set = self._quotes_set1
            self._quotes_set1 = self._quotes_set2
            self._quotes_set2 = temp_set
            del temp_set

        not_aligned_dates = []

        for quote_date in self._quotes_set1:
            if quote_date not in self._quotes_set2:
                not_aligned_dates.append(quote_date)

        for quote_date in not_aligned_dates:
            self._quotes_set1.pop(quote_date)

        not_aligned_dates = []

        for quote_date in self._quotes_set2:
            if quote_date not in self._quotes_set1:
                not_aligned_dates.append(quote_date)

        for quote_date in not_aligned_dates:
            self._quotes_set2.pop(quote_date)

        """
        VarianceCovarianceAnalyser is a class which aim is to take sets of quotes and return such metrics as variance, 
        covariance and correlation.
        :param quotes_set1: One of the sets of quotes
        :param quotes_set2: One of the sets of quotes
        :param skip_non_matching: Boolean indicating how the software should behave if there are any dates mismatch in
        the two sets of quotes provided. If set to True software will skip quotes if quote for that date is missing in
        any of the provided sets. If set to False then if a quote is missing the software will copy value from the last
        available date - WARNING! may lead to erroneous results. 
        """

    def covariance(self):
        average1 = DescriptiveStatistics(self._quotes_set1).average()
        average2 = DescriptiveStatistics(self._quotes_set2).average()
        numerator = 0
        count = 0

        for quote_date in self._quotes_set1:
            diff2 = self._quotes_set2[quote_date] - average2
            diff1 = self._quotes_set1[quote_date] - average1
            numerator += diff1 * diff2
            count += 1

        try:
            cov = numerator / count

        except ZeroDivisionError:
            cov = 0

        return cov

    def correlation(self):

        std_dev1 = DescriptiveStatistics(self._quotes_set1).standard_deviation()
        std_dev2 = DescriptiveStatistics(self._quotes_set2).standard_deviation()
        cov = self.covariance()

        corr = cov / (std_dev1 * std_dev2)
        return corr
