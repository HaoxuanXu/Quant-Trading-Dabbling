import math
import backtrader as bt


class GoldenCross(bt.Strategy):
    params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95), ('ticker', 'SPY'))

    def __init__(self):
        self.fast_MA = bt.indicators.SMA(
            self.data.close,
            period=self.params.fast,
            plotname='50 day Moving Average'
        )

        self.slow_MA = bt.indicators.SMA(
            self.data.close,
            period=self.params.slow,
            plotname='200 day Moving Average'
        )

        self.crossover = bt.indicators.CrossOver(
            self.fast_MA,
            self.slow_MA
        )

    def next(self):
        if self.position.size == 0 and self.crossover > 0:
            amount_to_invest = self.params.order_percentage * self.broker.cash
            self.size = math.floor(amount_to_invest / self.data.close)

            print("Buy {} shares of {} at ${} per share".format(self.size, self.params.ticker, self.data.close))

            self.buy(size=self.size)

        if self.position.size > 0 > self.crossover:
            print("Sell {} shares of {} at ${} per share".format(self.size, self.params.ticker, self.data.close))

            self.close()

