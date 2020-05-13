import alpaca_trade_api as tradeapi


with open("Keys/alpaca_api.txt", "r") as f:
    key_id = f.readline()
    secret_key = f.readline()

api = tradeapi.REST(key_id, secret_key, api_version='v2')
spy = api.alpha_vantage.historic_quotes('SPY', adjusted=True, output_format='pandas')
spy.columns = [' '.join(v.split()[1:]) for v in spy.columns]
spy = spy.iloc[::-1]

spy.to_csv("SPY.csv")
