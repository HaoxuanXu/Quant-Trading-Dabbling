import backtrader as bt
from backtrader import Cerebro
import pandas as pd
##########################################################
from Strategies.GoldenCross import GoldenCross
from Strategies.BuyHold import BuyHold

##########################################################
# Get Data
##########################################################
data = pd.read_csv('SPY.csv')
cerebro = Cerebro()
cerebro.broker.set_cash(100000)
feed = bt.feeds.PandasData(dataname=data)
cerebro.adddata(feed)
cerebro.addstrategy(BuyHold)
cerebro.run()
cerebro.plot()
