import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import table

url = 'https://api.coinmarketcap.com/v1/ticker/'
data = requests.get(url).json()
if not os.path.exists('df_image'):
    os.makedirs('df_image')
os.chdir('df_image')

def top_increase():
    ordered_data = sorted(data, key=lambda 
                          k: (float(k['percent_change_24h']), (k['percent_change_7d'])), reverse=True)[:5]
    raw_data_increase = {}
    
    for currency in ordered_data:
        rank = currency['rank']
        name = currency['name']
        percent_change_24h = currency['percent_change_24h']
        percent_change_7d = currency['percent_change_7d']
        price_usd = float(currency['price_usd'])
        price_usd = f'{price_usd:.2f}'

        raw_data_increase.setdefault('Rank', [])
        raw_data_increase['Rank'].append(rank)
        raw_data_increase.setdefault('Name', [])
        raw_data_increase['Name'].append(name)
        raw_data_increase.setdefault('Change last 24h (%)', [])
        raw_data_increase['Change last 24h (%)'].append(percent_change_24h)
        raw_data_increase.setdefault('Change last 7d (%)', [])
        raw_data_increase['Change last 7d (%)'].append(percent_change_7d)
        raw_data_increase.setdefault('Price(USD)', [])
        raw_data_increase['Price(USD)'].append(price_usd)

    df = pd.DataFrame(raw_data_increase, columns=['Rank', 'Name', 'Change last 24h (%)', 'Change last 7d (%)', 'Price(USD)'])

    print(df.to_string(index=False))

    # set fig size
    fig, ax = plt.subplots(figsize=(9.5, 2.7))
    # no axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    # no frame
    ax.set_frame_on(False)
    # plot table
    tab = table(ax, df, rowLabels=['']*df.shape[0], loc='center')
    # set font manually
    tab.auto_set_font_size(False)
    tab.set_fontsize(10)
    # set scale
    tab.scale(1, 2.5)
    # save the result
    plt.savefig('cryptopinc.png')

    
def top_decrease():
    ordered_data = sorted(data, key=lambda
        k: (float(k['percent_change_24h']), (k['percent_change_7d'])), reverse=True)[95:]
    raw_data_decrease = {}
    
    for currency in ordered_data:
        rank = currency['rank']
        name = currency['name']
        percent_change = currency['percent_change_24h']
        percent_change_7d = currency['percent_change_7d']
        price_usd = float(currency['price_usd'])
        price_usd = f'{price_usd:.2f}'
        
        raw_data_decrease.setdefault('Rank', [])
        raw_data_decrease['Rank'].append(rank)
        raw_data_decrease.setdefault('Name', [])
        raw_data_decrease['Name'].append(name)
        raw_data_decrease.setdefault('Change last 24h (%)', [])
        raw_data_decrease['Change last 24h (%)'].append(percent_change_24h)
        raw_data_decrease.setdefault('Change last 7d (%)', [])
        raw_data_decrease['Change last 7d (%)'].append(percent_change_7d)
        raw_data_decrease.setdefault('Price(USD)', [])
        raw_data_decrease['Price(USD)'].append(price_usd)

    df = pd.DataFrame(raw_data_decrease,
                          columns=['Rank', 'Name', 'Change last 24h (%)',
                                   'Change last 7d (%)', 'Price(USD)'])

    print(df.to_string(index=False))

    # set fig size
    fig, ax = plt.subplots(figsize=(9.5, 2.7))
    # no axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    # no frame
    ax.set_frame_on(False)
    # plot table
    tab = table(ax, df, rowLabels=[''] * df.shape[0], loc='center')
    # set font manually
    tab.auto_set_font_size(False)
    tab.set_fontsize(10)
    # set scale
    tab.scale(1, 2.5)
    # save the result
    plt.savefig('cryptopdec.png')
        
top_increase()
top_decrease()
