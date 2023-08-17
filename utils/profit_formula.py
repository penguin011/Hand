import json
import requests

from django.conf import settings

from utils.category_fee import category_fee


def profit_formula(sell_price:float, buy_price:int, currency:str, category_id:str, point:int, shipping_policy:str):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    currencies = requests.get(url).json()['rates']
    rate = currencies[currency]

    with open(file=str(settings.BASE_DIR / 'utils/shipping_fee.txt'),  mode='r', encoding='utf-8') as f:
        shipping_fee = f.read()
    shipping_fee = json.loads(shipping_fee)

    with open(file=str(settings.BASE_DIR / 'utils/profit_attrs.txt'),  mode='r', encoding='utf-8') as f:
        profit_attrs = f.read()
    profit_attrs = json.loads(profit_attrs)
    rate = rate*(1-float(profit_attrs['payoneer_fee'])/100)

    profit = int((sell_price*rate)-(0.3*rate)-(sell_price*float(category_fee[category_id])*rate*(1+float(profit_attrs['consumption_fee'])/100))-(sell_price*float(profit_attrs['oversea_fee'])/100*rate*(1+float(profit_attrs['consumption_fee'])/100))-(buy_price-point)-int(shipping_fee[shipping_policy])-int(profit_attrs['shipping_agency_fee']))

    return profit
    