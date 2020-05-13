import os, sys, optparse
import backtrader as bt
from backtrader import Cerebro
import pandas as pd

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
parser.add_option("-d", "--data", dest="data", help="what stocks are you evaluating this strategy on")
(options, args) = parser.parse_args()

if options.strategy is not None:
    strategy_key = options.strategy.strip()
else:
    strategy_key = input("Strategy to run >").strip()
    if strategy_key == "":
        raise ValueError("You must input an strategy")
    elif strategy_key.strip() not in strategies_dict.keys():
        raise ValueError("Strategy must part part of {}".format(strategies_dict.keys()))

if options.data is not None:
    data_list = options.data.strip().split()
else:
    data_list = input("Stocks to evaluate >").strip().split(' ')
    if data_list == "":
        raise ValueError("You must input tickers")
    elif not all(item in [n.split('.')[0] for n in os.listdir("Data")] for item in data_list):
        raise ValueError("Tickers must part part of {}".format([n.split('.')[0] for n in os.listdir("Data")]))
    elif data_list == "all":
        data_list = []
        for data in os.listdir("Data"):
            data_list.append((data, data.split('.')[0]))

data_list = ["".join((n, ".csv")) for n in data_list]
cerebro = Cerebro()
cerebro.broker.set_cash(100000)

for i in range(len(data_list)):
    data = pd.read_csv("Data/{}".format(data_list[i]), index_col="date", parse_dates=True)
    feed = bt.feeds.PandasData(dataname=data, name=data_list[i][1])
    cerebro.adddata(feed)

cerebro.addstrategy(strategies_dict[strategy_key], oneplot=False)
cerebro.run()
cerebro.plot()
