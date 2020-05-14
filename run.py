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
parser.add_option("-p", "--percent", dest="percent", help="What percent of money are you investing")
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
    data_list = options.data.strip()
else:
    data_list = input("Stocks to evaluate >").strip()
    if data_list == "":
        raise ValueError("You must input tickers")
    elif not (data_list in [n.split('.')[0] for n in os.listdir("Data")]):
        raise ValueError("Tickers must part part of {}".format([n.split('.')[0] for n in os.listdir("Data")]))

if options.percent is not None:
    percent = float(options.percent)
else:
    percent = float(input("Percent of money you are investing >"))


strategies_dict[strategy_key].params.ticker = data_list
strategies_dict[strategy_key].params.order_percentage = percent


cerebro = Cerebro()
cerebro.broker.set_cash(100000)


data = pd.read_csv("Data/{}.csv".format(data_list), index_col="date", parse_dates=True)
feed = bt.feeds.PandasData(dataname=data, name=data_list)
cerebro.adddata(feed)

cerebro.addstrategy(strategies_dict[strategy_key])
cerebro.run()
cerebro.plot()
