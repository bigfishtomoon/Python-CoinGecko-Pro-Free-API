# A Python CoinGecko Pro &amp; Free API
Python3 wrapper around the [CoinGecko](https://www.coingecko.com/en/api) API (V3)

### Usage Pro API

```python
from .api import CoinAPI
cgc = CoinAPI(api_key='CG-XXXXX')
```

### Usage Free API

```python
from .api import CoinAPI
cgc = CoinAPI()
```

### Examples

The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.\
**Any optional parameters** can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)

For any parameter:

- **\*Lists** are supported as input for multiple-valued comma-separated parameters\
  (e.g. see /simple/price usage examples).\*
- **\*Booleans** are supported as input for boolean type parameters; they can be `str` ('true', 'false'') or `bool` (`True`, `False`)\
  (e.g. see /simple/price usage examples).\*

Examples:

```python
# /simple/price endpoint with the required parameters
>>> cgc.simple_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 31778}}

>>> cgc.simple_price(ids='bitcoin,litecoin',vs_currencies='usd')
{'bitcoin': {'usd': 31774}, 'litecoin': {'usd': 69.32}}

>>> cgc.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd,eur')
# OR (lists can be used for multiple-valued arguments)
>>> cgc.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies=['usd', 'eur'])
{'bitcoin': {'usd': 3459.39, 'eur': 3019.33}, 'ethereum': {'usd': 106.91, 'eur': 93.31}, 'litecoin': {'usd': 32.72, 'eur': 28.56}}
```

### API documentation

https://www.coingecko.com/api/docs/v3

### Usage

- _ping_
  - **/ping** (Check API server status)
    ```python
    cgc.ping()
    ```
- _simple_
  - **/simple/price**
    ```python
    cgc.simple_price()
    ```
  - **/simple/token_price/{id}**
    ```python
    cgc.simple_token_price()
    ```
  - **/simple/supported_vs_currencies**
    ```python
    cgc.simple_supported_vs_currencies()
    ```
- _coins_
  - **/coins/list**
    ```python
    cgc.coins_list()
    ```
  - **/coins/markets**
    ```python
    cgc.coins_markets()
    ```
  - **/coins/{id}**
    ```python
    cgc.coins_id()
    ```
  - **/coins/{id}/tickers**
    ```python
    cgc.coins_id_tickers()
    ```
  - **/coins/{id}/history**
    ```python
    cgc.coins_id_history()
    ```
  - **/coins/{id}/market_chart**
    ```python
    cgc.coins_market_chart()
    ```
  - **/coins/{id}/market_chart/range**
    ```python
    cgc.coins_market_chart_range()
    ```
  - **/coins/{id}/ohlc** (Get coin's OHLC (beta))
    ```python
    cgc.coins_ohlc()
    ```
- _contract_
  - **/coins/{id}/contract/{contract_address}**
    ```python
    cgc.contract_address()
    ```
  - **/coins/{id}/contract/{contract_address}/market_chart/**
    ```python
    cgc.contract_address_market_chart()
    ```
  - **/coins/{id}/contract/{contract_address}/market_chart/range**
    ```python
    cgc.contract_address_market_chart_range()
    ```
- _asset_platforms_
  - **/asset_platforms**
    ```python
    cgc.asset_platforms()
    ```
- _categories_
  - **/coins/categories/list**
    ```python
    cgc.coins_categories_list()
    ```
  - **coins/categories**
    ```python
    cgc.coins_categories()
    ```
- _exchanges_
  - **/exchanges**
    ```python
    cgc.exchanges()
    ```
  - **/exchanges/list**
    ```python
    cgc.exchanges_list()
    ```
  - **/exchanges/{id}**
    ```python
    cgc.exchanges_id()
    ```
  - **/exchanges/{id}/tickers**
    ```python
    cgc.exchanges_id_tickers()
    ```
  - **/exchanges/{id}/volume_chart**
    ```python
    cgc.exchanges_id_volume_chart()
    ```
- _finance_
  - **/finance_platforms** (List all finance platforms)
    ```python
    cgc.get_finance_platforms()
    ```
  - **/finance_products** (List all finance products)
    ```python
    cgc.get_finance_products()
    ```
- _indexes_
  - **/indexes** (List all market indexes)
    ```python
    cgc.indexes()
    ```
  - **/indexes/{market_id}/{id}** (Get market index by market id and index id)
    ```python
    cgc.indexes_market_id_id()
    ```
  - **/indexes/list** (List market indexes id and name)
    ```python
    cgc.indexes_list()
    ```
- _derivatives_
  - **/derivatives** (List all derivative tickers)
    ```python
    cgc.derivatives()
    ```
  - **/derivatives/exchanges** (List all derivative exchanges)
    ```python
    cgc.derivatives_exchanges()
    ```
  - **/derivatives/exchanges/{id}** (Show derivative exchange data)
    ```python
    cgc.derivatives_exchanges_id()
    ```
  - **/derivatives/exchanges/list**
    ```python
    cgc.derivatives_exchanges_list()
    ```
- _exchange_rates_
  - **/exchange_rates**
    ```python
    cgc.exchange_rates()
    ```
- _search_
  - **/search/trending**
    ```python
    cgc.search()
    ```
    ```
- _trending_
  - **/search/trending** 
    ```python
    cgc.search_trending()
    ```
- _global_
  - **/global** (Get cryptocurrency global data)
    ```python
    cgc.get_global()
    ```

## License

[MIT](https://choosealicense.com/licenses/mit/)
