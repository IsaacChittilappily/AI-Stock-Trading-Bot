import os
from dotenv import load_dotenv
from functions.HTML_requests import get_request
from functions.format_data import format_data
from functions.update_stock_db import updateStockPrices

load_dotenv()

apiKey = os.getenv('ALPHA_VANTAGE_API_KEY')
symbol = 'MSFT'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={apiKey}'
years = 10


fullData = get_request(url)
formattedData = format_data(fullData, years=10)
updateStockPrices(symbol, formattedData)