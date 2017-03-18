from sentiment_analyzer import SentimentAnalyzer
from symbol_scanner import SymbolScanner
from twitter_scanner import TwitterScanner
from notifier import Notifier
import time

symbols = SymbolScanner().company_list

for symbol in symbols:
	time.sleep(5)
	twitter = TwitterScanner(symbol)
	tweets = twitter.tweets
	sentiment = SentimentAnalyzer(tweets)
	print "Symbol: " + symbol + " Avg Sentiment: " + str(sentiment.average_sentiment)
	#Notifier("YOUR_TWITTER_USERNAME", symbol, sentiment.average_sentiment)
	sentiment.reset()
	twitter.reset()