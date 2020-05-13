import alpaca_trade_api as tradeapi
import time


with open("Keys/alpaca_api.txt", "r") as f:
    key_id = f.readline()
    secret_key = f.readline()

api = tradeapi.REST(key_id, secret_key, api_version='v2')

# List of most traded ETFs
ticker_list = ['SPY', 'QQQ', 'IWM', 'EEM', 'HYG', 'EFA', 'TLT', 'XLF', 'GLD']

for t in ticker_list:
    print("Retrieving {} data...".format(t))
    data = api.alpha_vantage.historic_quotes(t, adjusted=True, output_format='pandas')
    data.columns = [' '.join(v.split()[1:]) for v in data.columns]
    data = data.iloc[::-1]

    data.to_csv("Data/{}.csv".format(t))
    print ("{} data retrieved!!!".format(t))
    time.sleep(12)

print("Data Retrieval Process Complete!! ")
