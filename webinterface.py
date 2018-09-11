from urllib import request

cnfg = {}

# open configuration file
config = open('config.txt', 'r')

# load configuration
for line in config:
    item = line.split('=')
    cnfg[item[0].replace(' ', '')] = item[1].replace('\n','')

print(cnfg)

last_day_close_url = cnfg['last_day_close_url']

# open url with data from last day close of stock market
last_day_close_data = request.urlopen(last_day_close_url)

# read the file
for line in last_day_close_data:
    # decoding data as they are seen by Python as binary
    daily_quotes = line.decode()
    daily_quotes = daily_quotes.split(',')
#    daily_quotes = ' '.join(daily_quotes)
#    print(daily_quotes)