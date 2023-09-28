import requests
import json
from config import TOKEN, keys

class ConvertionExcepton(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
           raise ConvertionExcepton(f'Невозможно перевести одинаковые валюты {base}')
        try:
           quote_ticker = keys[quote]
        except KeyError:
           raise ConvertionExcepton(f'Не удалось обработать валюту {quote}')
        try:
           base_ticker = keys[base]
        except KeyError:
           raise ConvertionExcepton(f'Не удалось обработать валюту {base}')
        try:
           amount = float(amount)
        except ValueError:
           raise ConvertionExcepton(f'Не удалось обработать валюту {amount}')
    
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total = json.loads(r.content)[keys[base]]
        return total