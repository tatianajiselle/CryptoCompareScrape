# Project uses mulpile exhange APIs to scrape historical data for every minute
# Running using virtualenvwrapper
# Created January 2018
# By: Tatiana Ensslin
# Exchanges scraped: Poloniex, gdax, binance, bittrex, kraken, and gemini

import requests
import json

# save data to appendable file
def save_to_file(exchange, data, trading_pair):
    f = open(exchange + '/'+ trading_pair, 'a')
    f.write(str(data))
    return


# start = 1498867200 July 1, 2017 00:00:00
# end = year 2286
def poloniex(trading_pair):
    r = requests.get('https://poloniex.com/public?command=returnChartData&currencyPair='
                     + trading_pair
                     + '&start=1405699200&end=9999999999&period=14400'
                     ).json()
    print(r)
    save_to_file('Poloniex', r, trading_pair)
    return


def binance():
    r = requests.get('https://api.binance.com/api/v1/klines').json()
    print(r)
    save_to_file('Binance', r, 'Binance_Kline')
    return

def bittrex(trading_pair,time_interval):
    r = requests.get('https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName='
                     + trading_pair
                     + '&tickInterval='
                     + time_interval
                     + '&_=1499127220008').json()
    print(r)
    save_to_file('Bittrex', r, trading_pair + '_' + time_interval)
    return

def main():

 poloniex('BTC_ETH');
  binance();
    bittrex('BTC-WAVES', 'oneMin');
    bittrex('BTC-WAVES', 'thirtyMin');


if __name__ == "__main__":  # main()
    import sys
    main()

