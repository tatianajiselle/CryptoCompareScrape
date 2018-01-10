import requests
import json

# save data to appendable file
def saveToFile(data):
	f = open('cryptoCompareData.txt', 'a')
	f.write(str(data))
	return

# Call cryptocompare api for historical hour data
# toTs: timestamp is the to date in epoch time
# date is the returned TimeFrom (latest date fetched)
# BTC and ETH are fetched
def histoHour(toTs): 
	r = requests.get('https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=BTC&limit=60&aggregate=1&toTs=' + toTs).json()
	print (r)
	saveToFile(r)
	date = r['TimeFrom']
	return date

# Starts the historical date with hardcoded date. As long as
# the date is not before june 1, 2017 (endTime), it will call 
# the api.
def main(): 

	# end historical data date
	# june 1, 2017 0:00:00 1496275200
	endTime = 1496275200

	#start historical data date
	# jan 10, 2018 0:00:00 1515542400
	startTime = 1515542400	

	date = histoHour(str(startTime))

	while (int(date) >= endTime):
		date = histoHour(str(date))


if __name__ == "__main__":# main()
    import sys
    main()
