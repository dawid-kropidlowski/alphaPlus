# alphaPlus
Some stock analysing Python scripts
The aim of this repository is to develop some scripts that will hopefully be useful in analysing stocks and building investment portfolios.

First steps to do:
  1. Write code that will be reading a configuration file providing url to data and how to read the data file (which column contains what data). + a list of isins to retrieve
  2. Code that will retrieve data file from url, read it and convert to json (for more standardized approach).
  3. Code that will retrieve data file from url, compare with current database and append missing data.
  4. Code that will check and append daily data.
  
Moving further, to do:
 1. Calculating average values for data set - with the possibility to specify time period
 2. Calculating standard deviations  - with the possibility to specify time period
 3. Calculating covariances and correlations between two sets of data - as above, specifying a time period.
  One problem that was already found is what to do if dates differ between two data sets? E.g there is a quotation missing for one day for one of the stocks?
  4. Calculating historical ratios, such as:
    - Sharpe ratio
    - Downside deviation (modification of standard deviation)
    - Beta coefficient
    - Jensen's alpha
    - ...
  5. Somehow get fundamental data for stocks and use them to calculate different ratios for fundamental analysis useful in growth/value investing.
