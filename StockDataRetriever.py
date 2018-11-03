from urllib import request
from datetime import date

cnfg = {}

# open configuration file
config = open('config.txt', 'r')

# load configuration
for line in config:
    item = line.split('=')
    cnfg[item[0].replace(' ', '')] = item[1].replace('\n','')

# get items' indexes
ticker_index = int(cnfg['ticker']) - 1
date_index = int(cnfg['date']) - 1
open_index = int(cnfg['open']) - 1
high_index = int(cnfg['high']) - 1
low_index = int(cnfg['low']) - 1
close_index = int(cnfg['close']) - 1
vol_index = int(cnfg['vol']) - 1

last_day_close_url = cnfg['last_day_close_url']

# open url with data from last day close of stock market
last_day_close_data = request.urlopen(last_day_close_url)

# read the file
for line in last_day_close_data:
    # decoding data as they are seen by Python as binary
    daily_quotes = line.decode()
    daily_quotes = daily_quotes.split(',')

    # convert entries to appropriate data types
    quote_date = daily_quotes[date_index]
    quote_date = date(int(quote_date[:4]), int(quote_date[4:6]), int(quote_date[6:8]))
    daily_quotes[date_index] = quote_date

    daily_quotes[open_index] = float(daily_quotes[open_index])
    daily_quotes[high_index] = float(daily_quotes[high_index])
    daily_quotes[low_index] = float(daily_quotes[low_index])
    daily_quotes[close_index] = float(daily_quotes[close_index])
    daily_quotes[vol_index] = float(daily_quotes[vol_index])
