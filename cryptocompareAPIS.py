import requests
import json

# save data to appendable file
def save_to_file(data):
    f = open('cryptoCompareData.txt', 'a')
    f.write(str(data))
    f.write('\ln')
    return

# Call cryptocompare api for historical hour data
# toTs: timestamp is the to date in epoch time
# date is the returned TimeFrom (latest date fetched)
# BTC and ETH are fetched
def histo_hour(to_ts):
    r = requests.get(
        'https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=BTC&limit=60&aggregate=1&toTs=' + to_ts).json()
    print(r)
    save_to_file(r)
    return r['TimeFrom']

# Call cryptocompare api for historical day data
# toTs: timestamp is the to date in epoch time
# date is the returned TimeFrom (latest date fetched)
# BTC and ETH are fetched
def histo_day(to_ts):
    r = requests.get(
        'https://min-api.cryptocompare.com/data/histoday?fsym=ETH&tsym=BTC&limit=60&aggregate=1&toTs=' + to_ts).json()
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

    # date = histo_hour(str(startTime))
    # while (int(date) >= endTime):
    # 	date = histo_hour(str(date))

    date = histo_day(str(startTime))
    while (int(date) >= endTime):
    	date = histo_day(str(date))


if __name__ == "__main__":  # main()
    import sys
    main()
