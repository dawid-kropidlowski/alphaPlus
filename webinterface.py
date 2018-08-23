from urllib import request

data = request.urlopen('http://bossa.pl/pub/metastock/mstock/sesjaall/sesjaall.prn')


for line in data:
    daily_quotes = line.decode()
    daily_quotes = daily_quotes.split(',')
    daily_quotes = ' '.join(daily_quotes)
    print(daily_quotes)