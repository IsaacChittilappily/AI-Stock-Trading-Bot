import requests
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv
from functions import get_HTML_request


def get_data(url: str) -> str:

    r = requests.get(url)
    data = r.json()
    return data
# function to make a request to the api endpoint and retrieve the data

def updateStockPrices(symbol: str, apiKey: str, years: int) -> None:

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={apiKey}'
    data = get_data(url)
    time_series = data['Time Series (Daily)']


    # convert the time series data into a dataframe
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.index = pd.to_datetime(df.index)
    df = df.rename_axis('Date').reset_index()

    # rename columns so they are more readable
    df = df.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    })

    timePeriod = pd.Timestamp.now() - pd.DateOffset(years=years)
    df = df[df['Date'] >= timePeriod].sort_values('Date')

    db = sqlite3.connect('historical_data.db')
    # connect to the database using sqlite

    df.to_sql(f'{symbol}_stock_data', db, if_exists='replace', index=False)
    # if the table for that stock already exists, replace it with the new table 

    db.commit()
    db.close()
    # commit the changes and close the connection


load_dotenv()
# this function automatically loads the .env file in the root directory - this ensures that the API keys are not exposed

updateStockPrices('AAPL', os.getenv('ALPHA_VANTAGE_API_KEY'), 10)
# retrieves the stock data for Apple for the last 5 years