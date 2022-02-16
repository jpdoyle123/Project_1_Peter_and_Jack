import pandas as pd
import os
import json
import requests
from dotenv import load_dotenv
import hvplot.pandas

def clean_data(fred_api_key,category_id):
    
    load_dotenv()


    type(fred_api_key)

    url = f'https://api.stlouisfed.org/fred/series/observations?series_id={category_id}&api_key={fred_api_key}&file_type=json'

    data = requests.get(url).json()

    exchange_df = pd.DataFrame(data['observations'])

    exchange_df = exchange_df.dropna()

    exchange_df = exchange_df[exchange_df['value'] != '.']

    exchange_df['value'] = exchange_df['value'].astype('float')

    exchange_df['inverse_rate'] = 1 / exchange_df['value']

    exchange_df = exchange_df[['date', 'value', 'inverse_rate']]

    exchange_df = exchange_df.set_index('date')

    exchange_df.index = pd.to_datetime(exchange_df.index)

    exchange_df = exchange_df.rename(columns = {'value' : 'spot_rate'})

    exchange_df['sma10'] = exchange_df['spot_rate'].rolling(window=10, min_periods = 10).mean()
    exchange_df['sma20'] = exchange_df['spot_rate'].rolling(window=20, min_periods = 10).mean()
    exchange_df['sma30'] = exchange_df['spot_rate'].rolling(window=30, min_periods = 10).mean()
    exchange_df['sma50'] = exchange_df['spot_rate'].rolling(window=50, min_periods = 10).mean()
    exchange_df['sma100'] = exchange_df['spot_rate'].rolling(window=100, min_periods = 10).mean()
    exchange_df['sma200'] = exchange_df['spot_rate'].rolling(window=200, min_periods = 10).mean()
    exchange_df = exchange_df.dropna()
    exchange_df

    exchange_df['ema10'] = exchange_df['spot_rate'].ewm(span=10).mean()
    exchange_df['ema20'] = exchange_df['spot_rate'].ewm(span=20).mean()
    exchange_df['ema30'] = exchange_df['spot_rate'].ewm(span=30).mean()
    exchange_df['ema50'] = exchange_df['spot_rate'].ewm(span=50).mean()
    exchange_df['ema100'] = exchange_df['spot_rate'].ewm(span=100).mean()
    exchange_df['ema200'] = exchange_df['spot_rate'].ewm(span=200).mean()
    exchange_df

    #get current rates and averages for display
    #get current spot rate
    current_spot_rate = exchange_df['spot_rate'].iloc[-1]

    #get current SMAs
    current_sma10 = exchange_df['sma10'].iloc[-1]
    current_sma20 = exchange_df['sma20'].iloc[-1]
    current_sma30 = exchange_df['sma30'].iloc[-1]
    current_sma50 = exchange_df['sma50'].iloc[-1]
    current_sma100 = exchange_df['sma100'].iloc[-1]
    current_sma200 = exchange_df['sma200'].iloc[-1]

    #get current EMAs
    current_ema10 = exchange_df['ema10'].iloc[-1]
    current_ema20 = exchange_df['ema20'].iloc[-1]
    current_ema30 = exchange_df['ema30'].iloc[-1]
    current_ema50 = exchange_df['ema50'].iloc[-1]
    current_ema100 = exchange_df['ema100'].iloc[-1]
    current_ema200 = exchange_df['ema200'].iloc[-1]
    
    return current_spot_rate, [current_sma10, current_sma20, current_sma30, current_sma50, current_sma100, current_sma200, current_ema10, current_ema20, current_ema30, current_ema50, current_ema100, current_ema200]
          
