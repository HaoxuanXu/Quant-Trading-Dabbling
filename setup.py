import requests
from tiingo import TiingoClient
import alpaca_trade_api
import finviz

tiingo_config = {"session": True}
alpaca_config = {}

with open("Keys/alpaca_api.txt", "r") as f:
    alpaca_config["key_id"] = f.readline()
    alpaca_config["secret_key"] = f.readline()

with open("Keys/tiingo_api.txt", "r") as f:
    tiingo_config["api_key"] = f.read()

print(alpaca_config["key_id"])
print(alpaca_config["secret_key"])

client = TiingoClient(tiingo_config)

historical_prices = client.get_ticker_price("GOOGL",
                                            fmt='csv',
                                            startDate='2017-08-01',
                                            endDate='2017-08-02',
                                            frequency='5min')

historical_prices
