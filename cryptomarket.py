import requests

url = 'https://api.coinmarketcap.com/v1/ticker/'
data = requests.get(url).json()


def crypto_report():
    for currency in data:
        rank = currency.get('rank')
        name = currency.get('name')
        price_usd = currency.get('price_usd')
        market_cap_usd = currency.get('market_cap_usd')
        # split_market_cap = ' '.join(market_cap_usd[i:i+3] for i in range(0, len(market_cap_usd), 3))

        try:
            change_24h = currency.get('percent_change_24h')
        except Exception as e:
            change_24h = None
        if change_24h is not None:
            currency_breakdown = (rank + ' | ' + name + ' | ' + '$' + price_usd + ' | ' + '$' 
                                  + market_cap_usd + ' | ' + change_24h + '%')
            print(currency_breakdown)
        else:
            pass
       
    
crypto_report()
