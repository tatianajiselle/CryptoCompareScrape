import requests

def saveToFile(data):
	f = open('cryptoCompareData.txt', 'a')
	f.write(data)
	return

def historicalHour(): #Call cryptocompare api for historical hour data
	r = requests.get('https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=BTC&limit=60&aggregate=1&toTs=1514797200')
	print (r.text)
	saveToFile(r.text)
	return

def main(): 
	historicalHour();

if __name__ == "__main__":# main()
    import sys
    main()
