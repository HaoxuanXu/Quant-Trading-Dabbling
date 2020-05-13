import requests
from lxml import etree
from bs4 import BeautifulSoup

# We will focus on stocks from S&P 500 and top 100 ETFs
####################################################################################
stock_lists = []
wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
page = requests.get(wiki_url)
tree = etree(page)
cleaned_soup = tree.findall("a", class_="external text")

for stock in cleaned_soup:
    stock_lists.append(stock.text)

final_stock_list = [stock for stock in stock_lists if stock != "reports"]
print(final_stock_list)

#####################################################################################
etf_list = []
etf_url = "https://etfdb.com/compare/volume/"
etf_page = requests.get(etf_url)
etf_soup = BeautifulSoup(etf_page.text, "lxml")

# Pair-Trading Strategy

# Use market-topology.com to find potential pairs
