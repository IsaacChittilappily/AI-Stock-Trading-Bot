import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
from ai_stock_trading_bot.data_collection.data_collection import collect_data
from ai_stock_trading_bot.decision_engine.submit_alpaca_order import submit_paper_trade

# loads my env file which stores my keys
load_dotenv()

# parameters of the data collection function
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
ALPACA_API_BASE_URL = os.getenv('ALPACA_API_BASE_URL')
symbol = 'NVDA'
years = 10
tradingApi = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_API_BASE_URL)

# collect_data(ALPHA_VANTAGE_API_KEY, symbol, years)

# import ai_stock_trading_bot.models.pytorchNetwork

# submit_paper_trade(tradingApi, symbol, 1, 'buy')
