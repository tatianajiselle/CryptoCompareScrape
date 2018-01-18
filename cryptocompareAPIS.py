# Project uses cryptocompare APIs to scrape historical data
# Running using virtualenvwrapper
# Created January 2018
# By: Tatiana Ensslin
# Exchanges scraped: Poloniex, gdax, binance, bittrex, kraken, and gemini

import requests
import json

# save data to appendable file
def save_to_file(data):
    f = open('Kraken/CC_HistoHour_ETH_BTC.txt', 'a')
    f.write(str(data))
    f.write('\n')
    return

#                                                         # 
#               ETH/BTC are fetched                       #
#                                                         #
# toTs: timestamp is the to date in epoch time            #
# date is the returned TimeFrom (latest date fetched)     #

# Historical hour data 
def histo_hour_eth_btc(to_ts, exchange):
    r = requests.get(
        'https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=BTC&limit=60&aggregate=1&toTs=' + to_ts + '&e=' + exchange).json()
    print(r)
    save_to_file(r)
    return r['TimeFrom']

# Historical day data
def histo_day_eth_btc(to_ts, exchange):
    r = requests.get(
        'https://min-api.cryptocompare.com/data/histoday?fsym=ETH&tsym=BTC&limit=60&aggregate=1&toTs=' + to_ts  + '&e=' + exchange).json()
    print(r)
    save_to_file(r)
    return r['TimeFrom']

#                                                         # 
#               BTC/ETH are fetched                       #
#                                                         #
# toTs: timestamp is the to date in epoch time            #
# date is the returned TimeFrom (latest date fetched)     #

def histo_hour_btc_eth(to_ts, exchange):
    r = requests.get(
        'https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=ETH&limit=60&aggregate=1&toTs=' + to_ts  + '&e=' + exchange).json()
    print(r)
    save_to_file(r)
    return r['TimeFrom']

def histo_day_btc_eth(to_ts, exchange):
    r = requests.get(
        'https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=ETH&limit=60&aggregate=1&toTs=' + to_ts  + '&e=' + exchange).json()
    print(r)
    save_to_file(r)
    return r['TimeFrom']

#                                                         # 
#               BTC/USD are fetched                       #
#                                                         #
# toTs: timestamp is the to date in epoch time            #
# date is the returned TimeFrom (latest date fetched)     #

def histo_day_btc_usd(to_ts, exchange):
    r = requests.get(
        'https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=60&aggregate=1&toTs=' + to_ts  + '&e=' + exchange).json()
    print(r)
    save_to_file(r)
    return r['TimeFrom']

def histo_hour_btc_usd(to_ts, exchange):
    r = requests.get(
        'https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=60&aggregate=1&toTs=' + to_ts  + '&e=' + exchange).json()
    print(r)
    save_to_file(r)
    return r['TimeFrom']


# Starts the historical date with hardcoded date. As long as
# the date is not before june 1, 2017 (endTime), it will call
# the api.
def main():

    # end historical data date
    # june 1, 2017 0:00:00 1496275200
    endTime = 1496275200

    # start historical data date
    # jan 10, 2018 0:00:00 1515542400
    startTime = 1515542400



    # HOURLY ETH to BTC
    date = histo_hour_eth_btc(str(startTime), 'Kraken')
    while (int(date) >= endTime):
    	date = histo_hour_eth_btc(str(date), 'Kraken')

    # DAILY ETH to BTC
    # date = histo_day_eth_btc(str(startTime), 'Kraken')
    # while (int(date) >= endTime):
    # 	date = histo_day_eth_btc(str(date), 'Kraken')



    # DAILY BTC to USD
    # date = histo_day_btc_usd(str(startTime),'Kraken')
    # while (int(date) >= endTime):
    #     date = histo_day_btc_usd(str(date),'Kraken')

    # HOURLY BTC to USD
    # date = histo_hour_btc_usd(str(startTime), 'Kraken')
    # while (int(date) >= endTime):
    #     date = histo_hour_btc_usd(str(date), 'Kraken')



    # HOURLY BTC to ETH
    # date = histo_hour_btc_eth(str(startTime), 'Kraken')
    # while (int(date) >= endTime):
    #     date = histo_hour_btc_eth(str(date), 'Kraken')

    # DAILY BTC to ETH
    # date = histo_day_btc_eth(str(startTime), 'Kraken')
    # while (int(date) >= endTime):
    #     date = histo_day_btc_eth(str(date), 'Kraken')


if __name__ == "__main__":  # main()
    import sys
    main()
