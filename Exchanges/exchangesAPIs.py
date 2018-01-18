# Project uses mulpile exhange APIs to scrape historical data for every minute
# Running using virtualenvwrapper
# Created January 2018
# By: Tatiana Ensslin
# Exchanges scraped: Poloniex, gdax, binance, bittrex, kraken, and gemini

import requests
import json

# save data to appendable file
def save_to_file(data):
    f = open('Poloniex/BTC_XMR_4H.txt', 'a')
    f.write(str(data))
    f.write('\n')
    return


# start = 1498867200 July 1, 2017 00:00:00
# end = year 2286
def poloniex():
    r = requests.get('https://poloniex.com/public?command=returnChartData&currencyPair=BTC_XMR&start=1405699200&end=9999999999&period=14400').json()
    print(r)
    save_to_file(r)
    return

def main():

    poloniex();


if __name__ == "__main__":  # main()
    import sys
    main()

