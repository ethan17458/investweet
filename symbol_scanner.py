from lxml import html
import requests

class SymbolScanner:
	'Gets a list of all S&P 500 companies from wikipedia'
	url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
	company_list = []

	def __init__(self):
		page = requests.get(self.url)
		tree = html.fromstring(page.content)

		symbols = tree.xpath("//table[1]/tr/td[1]/a/text()")
		for symbol in symbols:
			self.company_list.append("$" + symbol)
	