import os, sys, argparse
import pandas as pd
import alpaca_trade_api as tradeapi
from datetime import datetime
import backtrader as bt
from backtrader import Cerebro

from GoldenCross import GoldenCross

with open("Keys/alpaca_api.txt", "r") as f:
    key_id = f.readline()
    secret_key = f.readline()

api = tradeapi.REST(key_id, secret_key, api_version='v2')
spy = api.alpha_vantage.historic_quotes('SPY', adjusted=True, output_format='pandas')
spy.columns = [' '.join(v.split()[1:]) for v in spy.columns]
spy = spy.iloc[::-1]

cerebro = Cerebro()
cerebro.broker.set_cash(100000)
feed = bt.feeds.PandasData(dataname=spy)
cerebro.adddata(feed)
cerebro.addstrategy(GoldenCross)
cerebro.run()
cerebro.plot()
