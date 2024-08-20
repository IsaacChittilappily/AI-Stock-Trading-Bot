import requests
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
# this function automatically loads the .env file in the root directory - this ensures that the API keys are not exposed

alpha_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
symbol = 'AAPL'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={alpha_api_key}'

def get_data(url: str) -> str:
    r = requests.get(url)
    data = r.json()
    return data

data = get_data(url)
time_series = data['Time Series (Daily)']

# convert the time series data into a dataframe
df = pd.DataFrame.from_dict(time_series, orient='index')
df.index = pd.to_datetime(df.index)
df = df.rename_axis('Date').reset_index()
df = df.rename(columns={
    '1. open': 'Open',
    '2. high': 'High',
    '3. low': 'Low',
    '4. close': 'Close',
    '5. volume': 'Volume'
})

one_year_ago = pd.Timestamp.now() - pd.DateOffset(years=1)
df = df[df['Date'] >= one_year_ago].sort_values('Date')


db = sqlite3.connect('historical_data.db')
cursor = db.cursor()


df.to_sql('stock_data', db, if_exists='replace', index=False)


# commit the changes and close the connection
db.commit()
db.close()