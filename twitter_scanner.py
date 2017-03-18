import twitter

class TwitterScanner:
	'Scans Twitter for mentions of publicly traded companies in the S&P 500.'

	api = twitter.Api(consumer_key="YOUR-CONSUMER-KEY",
										consumer_secret="YOUR-CONSUMER-SECRET",
										access_token_key="YOUR-ACCESS-TOKEN",
										access_token_secret="YOUR-ACCESS-TOKEN-SECRET")
	symbol = ""
	tweets = []

	def __init__(self, symbol):
		self.symbol = symbol
		self.search()

	def search(self):
		import urllib
		date = self.get_current_date()
		results = self.api.GetSearch(raw_query=urllib.urlencode({
																	"q": self.symbol,
																	"result_type": "recent",
																	"since": date,
																	"count": 200
																}))
		self.parse_tweets(results)
		
	def parse_tweets(self, statuses):
		for status in statuses:
			self.tweets.append(status.text)

	def get_current_date(self):
		import time
		return time.strftime("%Y-%m-%d")

	def reset(self):
		self.symbol = ""
		self.tweets[:] = []
