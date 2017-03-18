import twitter

class Notifier:
	'Notifies users via Twitter DM of well performing stocks.'

	symbol = ""
	sentiment = 0.0
	screen_name = ""

	api = twitter.Api(consumer_key="YOUR-CONSUMER-KEY",
										consumer_secret="YOUR-CONSUMER-SECRET",
										access_token_key="YOUR-ACCESS-TOKEN",
										access_token_secret="YOUR-ACCESS-TOKEN-SECRET",
										sleep_on_rate_limit=True)

	def __init__(self, screen_name, symbol, sentiment):
		self.screen_name = screen_name
		self.symbol = symbol
		self.sentiment = sentiment
		self.notify()

	def notify(self):
		if self.sentiment >= 0.1:
			message = self.symbol + " has a high sentiment score of " + str(self.sentiment) + ". "
			self.api.PostDirectMessage(screen_name=self.screen_name, text=message)

