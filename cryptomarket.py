import requests
import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import table

url = 'http://coincap.io/front'
data = requests.get(url).json()

if not os.path.exists('df_image'):
    os.makedirs('df_image')
os.chdir('df_image')


def top_increase():
    top100_data = sorted(data, key=lambda k: (float(k['mktcap'])), reverse=True)[:100]
    ordered_data = sorted(top100_data, key=lambda k: (float(k['cap24hrChange'])), reverse=True)[:5]
    raw_data_increase = {}

    for currency in ordered_data:
        name = currency['long']
        market_cap = float(currency['mktcap'])
        market_cap_rounded = f'{market_cap:,.2f}'
        percent_change_24 = currency['cap24hrChange']
        price = float(currency['price'])
        price_rounded = f'{price:.2f}'

        raw_data_increase.setdefault('Name', [])
        raw_data_increase['Name'].append(name)
        raw_data_increase.setdefault('Market Cap(USD)', [])
        raw_data_increase['Market Cap(USD)'].append(market_cap_rounded)
        raw_data_increase.setdefault('%24hr', [])
        raw_data_increase['%24hr'].append(percent_change_24)
        raw_data_increase.setdefault('Price(USD)', [])
        raw_data_increase['Price(USD)'].append(price_rounded)

    df = pd.DataFrame(raw_data_increase, columns=['Name', 'Market Cap(USD)', '%24hr', 'Price(USD)'])

    print(df.to_string(index=False))

    # set fig size
    fig, ax = plt.subplots(figsize=(6.8, 2))
    # no axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    # no frame
    ax.set_frame_on(False)
    # plot table
    tab = table(ax, df, rowLabels=[''] * df.shape[0], loc='center')
    # set font manually
    tab.auto_set_font_size(False)
    tab.set_fontsize(8.8)
    # set scale
    tab.scale(1, 1.8)
    # save the result
    plt.savefig('coincapinc.png')


top_increase()


def top_decrease():
    top100_data = sorted(data, key=lambda k: (float(k['mktcap'])), reverse=True)[:100]
    ordered_data = sorted(top100_data, key=lambda k: (float(k['cap24hrChange'])))[:5]
    raw_data_decrease = {}

    for currency in ordered_data:
        name = currency['long']
        market_cap = float(currency['mktcap'])
        market_cap_rounded = f'{market_cap:,.2f}'
        percent_change_24 = currency['cap24hrChange']
        price = float(currency['price'])
        price_rounded = f'{price:.2f}'

        raw_data_decrease.setdefault('Name', [])
        raw_data_decrease['Name'].append(name)
        raw_data_decrease.setdefault('Market Cap(USD)', [])
        raw_data_decrease['Market Cap(USD)'].append(market_cap_rounded)
        raw_data_decrease.setdefault('%24hr', [])
        raw_data_decrease['%24hr'].append(percent_change_24)
        raw_data_decrease.setdefault('Price(USD)', [])
        raw_data_decrease['Price(USD)'].append(price_rounded)

        df = pd.DataFrame(raw_data_decrease, columns=['Name', 'Market Cap(USD)', '%24hr', 'Price(USD)'])

    print(df.to_string(index=False))

    # set fig size
    fig, ax = plt.subplots(figsize=(6.8, 2))
    # no axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    # no frame
    ax.set_frame_on(False)
    # plot table
    tab = table(ax, df, rowLabels=[''] * df.shape[0], loc='center')
    # set font manually
    tab.auto_set_font_size(False)
    tab.set_fontsize(8)
    # set scale
    tab.scale(1, 1.8)
    # save the result
    plt.savefig('coincapdec.png')


top_decrease()


def btc_chg():
    btc_url = 'http://coincap.io/history/30day/BTC'
    btc_data = requests.get(btc_url).json()
    price_list = []
    time_list = []
    df_price = {}
    
    for values in btc_data['price']:
        time = values[0]
        time = int(str(time)[:10])
        converted_time = datetime.datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

#         print(converted_time + ' ' + str(values[1]))
        
        df_price.setdefault('Datetime', [])
        df_price['Datetime'].append(converted_time)
        df_price.setdefault('Price', [])
        df_price['Price'].append(str(values[1]))

        df = pd.DataFrame(df_price, columns=['Datetime', 'Price'])

        price_list.append(str(values[1]))
        time_list.append(converted_time)
    
    print(df.to_string())
    
    df.to_csv('btc_30d_chg.csv')
    graph = pd.read_csv('btc_30d_chg.csv', parse_dates=True, index_col=1)
    graph['Price'].plot()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Bitcoin changes (30d)')
    plt.savefig('btc_changes.png')

btc_chg()


