from textblob import TextBlob

class SentimentAnalyzer:
	'Analyzes the sentiment of tweets about S&P 500 companies'
	tweets = []
	average_sentiment = 0.0
	analyzed_tweets = []
	sentiment_sum = 0.0

	def __init__(self, tweets):		
		self.tweets = tweets
		for tweet in self.tweets:
			sentiment = TextBlob(tweet).sentiment.polarity
			self.analyzed_tweets.append([tweet, sentiment])
		self.sentiment_sum = 0.0
		for tweet in self.analyzed_tweets:
			self.sentiment_sum += tweet[1]
		self.average_sentiment = float(float(self.sentiment_sum) / float(len(self.analyzed_tweets)))

	def reset(self):
		self.tweets = []
		self.average_sentiment = 0.0
		self.analyzed_tweets = []
		self.sentiment_sum = 0.0