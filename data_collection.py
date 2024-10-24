import os
from dotenv import load_dotenv
from my_functions.HTML_requests import get_request
from my_functions.format_data import format_data
from my_functions.update_stock_db import updateStockPrices

load_dotenv()

apiKey = os.getenv('ALPHA_VANTAGE_API_KEY')
symbol = 'TSLA'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={apiKey}'
years = 10


fullData = get_request(url)
formattedData = format_data(data=fullData, years=years)

updateStockPrices('historical_data.db', symbol, formattedData)