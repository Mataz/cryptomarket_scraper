import requests

url = 'https://api.coinmarketcap.com/v1/ticker/'
data = requests.get(url).json()


def top_increase():
    ordered_data = sorted(data, key=lambda 
                          k: (float(k['percent_change_24h']), (k['percent_change_7d'])), reverse=True)[:5]
    print('Top 5 increase in the last 24 hours (and their 7d changes): ')
    print(format('RANK', '>4') + ' | ' + format('NAME', '>21') + ' | '
          + format('CHANGE(24H)', '>8') + ' | ' + format('CHANGE(7D)', '>11') + ' | '
          + format('PRICE(USD)', '>12'))
    for currency in ordered_data:
        rank = currency['rank']
        name = currency['name']
        percent_change_24h = currency['percent_change_24h']
        percent_change_7d = currency['percent_change_7d']
        price_usd = float(currency['price_usd'])
        print(format(rank, '>4') + ' | ' + format(name, '>21') + ' | ' 
              + format(percent_change_24h, '>10') + '%' + ' | ' + format(percent_change_7d, '>10')
              + '%' + ' | ' + '$' + format(f'{price_usd:.2f}', '>10'))
    print()

    
def top_decrease():
    ordered_data = sorted(data, key=lambda
        k: (float(k['percent_change_24h']), (k['percent_change_7d'])), reverse=True)[95:]
    print('Top 5 from the bottom, of increase or decrease in the last 24 hours '
          '(and their 7d changes): ')
    print(format('RANK', '>4') + ' | ' + format('NAME', '>21') + ' | '
          + format('CHANGE(24H)', '>8') + ' | ' + format('CHANGE(7D)', '>11') + ' | '
          + format('PRICE(USD)', '>12'))
    for currency in ordered_data:
        rank = currency['rank']
        name = currency['name']
        percent_change = currency['percent_change_24h']
        percent_change_7d = currency['percent_change_7d']
        price_usd = float(currency['price_usd'])
        print(format(rank, '>4') + ' | ' + format(name, '>21') + ' | ' 
              + format(percent_change_24h, '>10') + '%' + ' | ' + format(percent_change_7d, '>10')
              + '%' + ' | ' + '$' + format(f'{price_usd:.2f}', '>10'))

        
top_increase()
top_decrease()
