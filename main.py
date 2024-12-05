import os
from dotenv import load_dotenv, find_dotenv
from ai_stock_trading_bot.data_collection.data_collection import collect_data
# loads my env file which stores my alphavantage 
load_dotenv()

# parameters of the data collection function
apikey = os.getenv('ALPHA_VANTAGE_API_KEY')
symbol = 'AAPL'
years = 10


collect_data(apikey, symbol, years)

# import ai_stock_trading_bot.models.pytorchNetwork