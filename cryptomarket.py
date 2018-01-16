import requests

url = 'https://api.coinmarketcap.com/v1/ticker/'
data = requests.get(url).json()


def top_increase():
    ordered_top_3_increase = sorted(data, key=lambda k: float(k['percent_change_24h']))[
                             97:]
    print('Top 3 increase in the last 24 hours: ')
    print(format('RANK', '>4') + ' | ' + format('NAME', '>18') + ' | '
          + format('CHANGE(24H)', '>8') + ' | ' + format('PRICE(USD)', '>8'))
    for currency in ordered_top_3_increase:
        rank = currency['rank']
        name = currency['name']
        percent_change = currency['percent_change_24h']
        price_usd = float(currency['price_usd'])
        print(format(rank, '>4') + ' | ' + format(name, '>18') + ' | ' + format(
            percent_change, '>10') + '%' + ' | ' + '$' + format(f'{price_usd:.2f}', '>8'))
    print()


top_increase()


def top_decrease():
    ordered_top_3_decrease = sorted(data, key=lambda k: float(k['percent_change_24h']),
                                    reverse=True)[97:]
    print('Top 3 decrease in the last 24 hours: ')
    print(format('RANK', '>4') + ' | ' + format('NAME', '>18') + ' | ' + format(
        'CHANGE(24H)', '>8') + ' | ' + format('PRICE(USD)', '>8'))
    for currency in ordered_top_3_decrease:
        rank = currency['rank']
        name = currency['name']
        percent_change = currency['percent_change_24h']
        price_usd = float(currency['price_usd'])
        print(format(rank, '>4') + ' | ' + format(name, '>18') + ' | ' + format(
            percent_change, '>10') + '%' + ' | ' + '$' + format(f'{price_usd:.2f}', '>8'))


top_decrease()
