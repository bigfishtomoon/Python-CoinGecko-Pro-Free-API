import json
import urllib3


class CoinAPI:

    def __init__(self, api_key=None):
        self.http = urllib3.PoolManager()
        self.timeout = 120
        self.retries = 3
        self.api_key = api_key
        if api_key:
            url_base = 'https://pro-api.coingecko.com/api/v3/'
            self.fields = {'x_cg_pro_api_key': api_key}
        else:
            url_base = 'https://api.coingecko.com/api/v3/'
            self.fields = {}
        self.api_base_url = url_base

    def request(self, url, params=None):
        try:
            url = f'{self.api_base_url}{url}'
            r = self.http.request('GET', url, fields=params,
                                  timeout=self.timeout, retries=self.retries)
            if r.status == 200:
                content = json.loads(r.data.decode('utf-8'))
                return content
        except:
            pass
        return False

    def params(self, params=None):
        fields = self.fields
        if params:
            fields.update(params)
        for key, value in fields.items():
            if type(value) == bool:
                fields[key] = str(value).lower()
        return fields

    def ping(self):
        url = 'ping'
        return self.request(url, self.params())

    def simple_price(self, ids='bitcoin', vs_currencies='usd', **kwargs):
        url = 'simple/price'
        kwargs['ids'] = ids
        kwargs['vs_currencies'] = vs_currencies
        params = self.params(kwargs)
        return self.request(url, params)

    def simple_token_price(self, id, contract_addresses, vs_currencies='usd', **kwargs):
        url = f'simple/token_price/{id}'
        kwargs['contract_addresses'] = contract_addresses
        kwargs['vs_currencies'] = vs_currencies
        params = self.params(kwargs)
        return self.request(url, params)

    def simple_supported_vs_currencies(self):
        url = 'simple/supported_vs_currencies'
        return self.request(url, self.params())

    def coins_list(self, include_platform, **kwargs):
        url = 'coins/list'
        kwargs['include_platform'] = include_platform
        params = self.params(kwargs)
        return self.request(url, params)

    def coins_markets(self, vs_currency='usd', **kwargs):
        url = 'coins/markets'
        kwargs['vs_currency'] = vs_currency
        params = self.params(kwargs)
        return self.request(url, params)

    def coins_id(self, id, **kwargs):
        url = f'coins/{id}'
        kwargs['id'] = id
        params = self.params(kwargs)
        return self.request(url, params)

    def coins_id_tickers(self, id, **kwargs):
        url = f'coins/{id}/tickers'
        kwargs['id'] = id
        params = self.params(kwargs)
        return self.request(url, params)

    def coins_id_history(self, id, date, **kwargs):
        url = f'coins/{id}/history'
        kwargs['id'] = id
        kwargs['date'] = date
        params = self.params(kwargs)
        return self.request(url, params)

    def coins_market_chart(self, id, vs_currency='usd', days=1, **kwargs):
        url = f'coins/{id}/market_chart'
        kwargs['id'] = id
        kwargs['vs_currency'] = vs_currency
        kwargs['days'] = days
        params = self.params(kwargs)
        return self.request(url, params)

    def coins_market_chart_range(self, id, vs_currency='usd', from_day=None, to_day=None, **kwargs):
        url = f'coins/{id}/market_chart/range'
        kwargs['id'] = id
        kwargs['vs_currency'] = vs_currency
        kwargs['from'] = from_day
        kwargs['to'] = to_day
        params = self.params(kwargs)
        return self.request(url, params)

    def coins_ohlc(self, id, vs_currency='usd', days=1, **kwargs):
        url = f'coins/{id}/ohlc'
        kwargs['id'] = id
        kwargs['vs_currency'] = vs_currency
        kwargs['days'] = days
        params = self.params(kwargs)
        return self.request(url, params)

    def contract_address(self, id, contract_address):
        url = f'coins/{id}/contract/{contract_address}'
        return self.request(url, self.params())

    def contract_address_market_chart(self, id, contract_address, vs_currency='usd', days=1, **kwargs):
        url = f'coins/{id}/contract/{contract_address}/market_chart/'
        kwargs['id'] = id
        kwargs['contract_address'] = contract_address
        kwargs['vs_currency'] = vs_currency
        kwargs['days'] = days
        params = self.params(kwargs)
        return self.request(url, params)

    def contract_address_market_chart_range(self, id, contract_address, vs_currency='usd', from_day=None, to_day=None, **kwargs):
        url = f'coins/{id}/contract/{contract_address}/market_chart/range'
        kwargs['id'] = id
        kwargs['contract_address'] = contract_address
        kwargs['vs_currency'] = vs_currency
        kwargs['from'] = from_day
        kwargs['to'] = to_day
        params = self.params(kwargs)
        return self.request(url, params)

    def asset_platforms(self):
        url = f'asset_platforms'
        return self.request(url, self.params())

    def coins_categories_list(self):
        url = f'coins/categories/list'
        return self.request(url, self.params())

    def coins_categories(self, **kwargs):
        url = f'coins/categories'
        params = self.params(kwargs)
        return self.request(url, params)

    def exchanges(self, per_page=250, page=1, **kwargs):
        url = f'exchanges'
        kwargs['per_page'] = per_page
        kwargs['page'] = page
        params = self.params(kwargs)
        return self.request(url, params)

    def exchanges_list(self, **kwargs):
        url = f'exchanges/list'
        params = self.params(kwargs)
        return self.request(url, params)

    def exchanges_id(self, id='binance'):
        url = f'exchanges/{id}'
        return self.request(url, self.params())

    def exchanges_id_tickers(self, id='binance', **kwargs):
        url = f'exchanges/{id}/tickers'
        params = self.params(kwargs)
        return self.request(url, params)

    def exchanges_id_volume_chart(self, id='binance', days=1, **kwargs):
        url = f'exchanges/{id}/volume_chart'
        kwargs['days'] = days
        params = self.params(kwargs)
        return self.request(url, params)

    def indexes(self, per_page=250, page=1, **kwargs):
        url = f'indexes'
        kwargs['per_page'] = per_page
        kwargs['page'] = page
        params = self.params(kwargs)
        return self.request(url, params)

    def indexes_market_id_id(self, market_id, id, **kwargs):
        url = f'indexes/{market_id}/{id}'
        kwargs['market_id'] = market_id
        kwargs['id'] = id
        params = self.params(kwargs)
        return self.request(url, params)

    def indexes_list(self):
        url = f'indexes/list'
        return self.request(url, self.params())

    def derivatives(self, **kwargs):
        url = f'derivatives'
        params = self.params(kwargs)
        return self.request(url, params)

    def derivatives_exchanges(self, **kwargs):
        url = f'derivatives/exchanges'
        params = self.params(kwargs)
        return self.request(url, params)

    def derivatives_exchanges_id(self, id, **kwargs):
        url = f'derivatives/exchanges/{id}'
        params = self.params(kwargs)
        return self.request(url, params)

    def derivatives_exchanges_list(self):
        url = f'derivatives/exchanges/list'
        return self.request(url, self.params())

    def exchange_rates(self):
        url = f'exchange_rates'
        return self.request(url, self.params())

    def search(self, query, **kwargs):
        url = f'search'
        kwargs['query'] = query
        params = self.params(kwargs)
        return self.request(url, params)

    def search_trending(self):
        url = f'search/trending'
        return self.request(url, self.params())

    def get_global(self):
        url = f'global'
        return self.request(url, self.params())
