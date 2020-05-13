import finviz
import requests
from finviz.screener import Screener

# Identify potential stocks for short squeeze strategy

short_squeeze_candidates = []

filters = ["fa_quickratio_o10", "sh_short_o25"]
stock_list = Screener(filters=filters, table='Performance')

for stock in stock_list:
    short_squeeze_candidates.append(stock["Ticker"])

print(short_squeeze_candidates)