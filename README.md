# investweet
Analyzes hype about publicly traded companies on twitter

1. Searches for mentions of publicly traded companies on Twitter: i.e "$AAPL"
2. Analyzes the sentiment of each mention
3. Average the sentiment of each tweet
4. If the sentiment is abnormally high, notifies the user via Twitter direct message.

Notifications are turned off by default due to Twitter's blockage on automated DM's. 

To reduce the number of times you are notified, you can increase the threshold of sentiment (0.1 by default) so that the notifier sends messages less frequently.

# Known issues
The sentiment average seems to not be resetting correctly with each new company analyzed.

Excess notifications causes the application to be blocked by Twitter's API.

# Instructions

1. Fill in main.py with your username
2. Fill in notifier.py and twitter_scanner.py with your Twitter API credentials
3. Run main.py

I know there are many improvements to be made, this is simply the first semi-working version :)
