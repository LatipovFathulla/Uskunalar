import requests


def _main():
    url = 'https://nbu.uz/uz/exchange-rates/json/'
    request = requests.get(url)
    return request.json()[-1]["cb_price"]


_main()
