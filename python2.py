import questionary

currency_pair = questionary.select('Which currency pair do you want to evaluate?', choices = ['USD/EUR']).ask()
print('Now analyzing...')
if currency_pair == 'USD/EUR':
    filepath = 'Graphs_and_things-vpl.ipynb'
    print("To see your results copy and paste the following command in your terminal:")
    print(f'voila {filepath}')
