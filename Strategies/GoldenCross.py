import math
import backtrader as bt
from datetime import datetime


class GoldenCross(bt.Strategy):
    params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95), ('ticker', 'SPY'), ('oneplot', True))

    def __init__(self):

        self.inds = dict()

        for i, d in enumerate(self.datas):
            self.inds[d] = dict()
            self.inds[d]['fast_MA'] = bt.indicators.SMA(
                d.close,
                plotname='50 day Moving Average',
                period=self.params.fast
            )

            self.inds[d]['slow_MA'] = bt.indicators.SMA(
                d.close,
                period=self.params.slow,
                plotname='200 day Moving Average'
            )

            self.inds[d]['crossover'] = bt.indicators.CrossOver(
                self.inds[d]['fast_MA'],
                self.inds[d]['slow_MA']
            )

            if i > 0 and self.params.oneplot == True:
                d.plotinfo.plotmaster = self.datas[0]

    def next(self):
        for i, d in enumerate(self.datas):
            dt, dn = self.datetime.date(), d._name
            pos = self.getposition(d).size
            if pos == 0:
                if self.inds[d]['crossover'][0] == 1:
                    amount_to_buy = math.floor(self.params.order_percentage*self.broker.cash / d.close)
                    self.buy(data=d, size=amount_to_buy)

            # else:
            #     if self.inds[d]['crossover'][0] == 1:
            #         self.close(data=d)
            #         self.buy(data=d, size=1000)

            elif self.inds[d]['crossover'][0] == -1:
                self.close(data=d)


    # def notify_trade(self, trade):
    #     dt = self.data.datetime.date()
    #     if trade.isclosed:
    #         print('{} {} Closed: PnL Gross {}, Net {}'.format(
    #                                                             dt,
    #                                                             trade.data._name,
    #                                                             round(trade.pnl, 2),
    #                                                             round(trade.pnlcomm, 2)))
