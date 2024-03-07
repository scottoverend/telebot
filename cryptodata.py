from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

cg.ping()

# /simple/price endpoint with the required parameters
cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}

