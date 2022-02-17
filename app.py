import pandas as pd
import os
import json
import requests
from dotenv import load_dotenv
import hvplot.pandas
import questionary
from Functions.data_cleaning import clean_data
from Functions.indicator import indicator

load_dotenv()
fred_api_key = os.getenv('FRED_API_KEY')

category_name = questionary.select('Which currency pair do you want to evaluate?', choices = ['USD/EUR', 'JPY/USD', 'USD/GBP', 'CAD/USD', 'MXN/USD']).ask()
print('Now analyzing...')
categories = {'USD/EUR' : 'DEXUSEU',
              'Yen/USD' : 'DEXJPUS',
              'USD/GBP' : 'DEXUSUK',
              'CAD/USD' : 'DEXCAUS',
              'MXN/USD' : 'DEXMXUS'
             }
category_id = categories[category_name]

if category_name == 'USD/EUR':
    filepath = 'Graphs_and_things-vpl.ipynb'
    print("To see your results copy and paste the following command in your terminal:")
    print(f'voila {filepath}')


spot_rate, results = clean_data(fred_api_key,category_id)
    
#print results
print(f'Spot Rate = ${spot_rate: .4f}')
print(f'SMA10 = ${results[0]: .4f}')
print(f'SMA20 = ${results[1]: .4f}')
print(f'SMA30 = ${results[2]: .4f}')
print(f'SMA50 = ${results[3]: .4f}')
print(f'SMA100 = ${results[4]: .4f}')
print(f'SMA200 = ${results[5]: .4f}')
print(f'EMA10 = ${results[6]: .4f}')
print(f'EMA20 = ${results[7]: .4f}')
print(f'EMA30 = ${results[8]: .4f}')
print(f'EMA50 = ${results[9]: .4f}')
print(f'EMA100 = ${results[10]: .4f}')
print(f'EMA200 = ${results[11]: .4f}')

total = 0

for avg in results: 
    
    indicator_result = indicator(spot_rate,avg)
    total = total + indicator_result
print(f'{total/12*100: .2f}%')