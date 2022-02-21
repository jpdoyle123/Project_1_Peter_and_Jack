# Project 1: Technical Analysis of Currency Pairs

We have built a command line interface application that will perform technical analysis on a selected currency pair to provide the user guidance on whether to buy or sell

* Currency pairs: USD/EUR, JPY/USD, USD/GBP, CAD/USD, MXN/USD
* Analysis: Simple Moving Average and Exponential Moving Average over 10, 20, 30, 50, 100, and 200 day time frames

If the moving average is higher than the daily spot rate, you would buy that pair
Using up to date data from the Federal Reserve of St Louis, our application gives an output based on these moving averages to advise the user to buy or sell on a sliding scale from 0-100%

---

Due to the nature of our planned technical analysis of currency pairs, we felt it was best to use data from the Federal Reserve’s extensive database FRED. This database has up-to-date statistics across a wide-range of economic indicators, including the statistics we needed for our analysis. 

To build the application, we used the daily measure of the foreign currency exchange rates as our analytic variable. To read it into our jupyter notebook, we first registered with FRED for an api key. Then, we used a python interface called full_fred to help process our API requests for the data we needed. Once the request was processed, we read the data into a pandas dataframe and started the cleanup process. 

---

Data cleanup process: 
1. Read the data into a pandas dataframe
2. Remove missing values, and convert spot rate data type to float
3. Remove any extraneous columns
4. Set the date column as the index, and apply datetime format to the column
5. Rename the columns to be more relevant to our analysis

---
Approach:

To pull live data into the application the user needs to provide two input variables:

1. Their FRED API key stored in a .env file

    * This is achieved by having the user set up a .env file with their API key in the Functions folder. 
    * Then we can simply call the load_env() function from the dotenv library to pull that value in.
2. The category ID of the currency pair 
    * A questionary command prompts the user to select in plain text a currency pair.
    * A dictionary of key/value pairs was then used to map those to the category IDs that are used in the FRED API.

---

Moving averages are just one type of indicator that can be used in technical analysis. Next steps to enhance this application could include the addition of more advanced indicators to provide a more accurate assessment of a given currency’s relative strength.

In addition to adding more types of indicators we could provide different weights to different indicators. In our current version, each moving average is given equal weighting to the overall results.

## Technologies

This project leverages Python 3.7 and Jupyter Lab with the following packages:

* [pandas](https://pandas.pydata.org/) - For financial data analysis tools
* [dotenv](https://pypi.org/project/python-dotenv/) - To store personal API keys in as environment variables
* [hvplot](https://hvplot.holoviz.org/) - For interactive data visualizations

## Contributors

This project was created and completed by John Doyle (jpdoyle1999@gwu.edu) and Peter Lefebvre (peter.c.lefebvre@gmail.com) with the assistance of the GWU Fintech Bootcamp teaching staf.

