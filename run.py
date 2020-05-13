import os, sys, optparse
import backtrader as bt
from backtrader import Cerebro
import pandas as pd
##########################################################
from Strategies.GoldenCross import GoldenCross
from Strategies.BuyHold import BuyHold

##########################################################
strategies_dict = {
    "golden_cross": GoldenCross,
    "buy_hold": BuyHold
}
##########################################################
# Get Data
##########################################################

parser = optparse.OptionParser()
parser.add_option("-s", "--strategy", dest="strategy", help="Which Strategy do you want to run")
(options, args) = parser.parse_args()

if options.strategy is not None:
    strategy_key = options.strategy.strip()
else:
    strategy_key = input("Strategy to run >").strip()
    if strategy_key == "":
        raise ValueError("You must input an strategy")
    elif strategy_key.strip() not in strategies_dict.keys():
        raise ValueError("Strategy must part part of {}".format(strategies_dict.keys()))

data = pd.read_csv('SPY.csv', index_col='date', parse_dates=True)
cerebro = Cerebro()
cerebro.broker.set_cash(100000)
feed = bt.feeds.PandasData(dataname=data)
cerebro.adddata(feed)
cerebro.addstrategy(strategies_dict[strategy_key])
cerebro.run()
cerebro.plot()
