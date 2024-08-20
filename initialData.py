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

df = pd.DataFrame.from_dict(time_series, orient='index')
df.index = pd.to_datetime(df.index)

one_year_ago = pd.Timestamp.now() - pd.DateOffset(years=1)

df = df[df.index >= one_year_ago].sort_index()

print(df)
db = sqlite3.connect('historical_data.db')
cursor = db.cursor

df.to_sql('Stock Prices', db, if_exists='replace', index=False)

db.commit()
db.close()
