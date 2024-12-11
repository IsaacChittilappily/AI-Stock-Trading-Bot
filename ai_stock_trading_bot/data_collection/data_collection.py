# this procedure combines all the other functions, and collects data for a certain stock

def collect_data(apikey: str, symbol: str, years: int):

    # imports the relevant packages from my files
    from ai_stock_trading_bot.data_collection.HTML_requests import get_request
    from ai_stock_trading_bot.data_collection.format_data import format_data
    from ai_stock_trading_bot.data_collection.update_stock_db import updateStockPrices

    # constructs the url to call alphavantage api
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={apikey}'

    # call the relevant functions to gather and format the data
    fullData = get_request(url)
    
    formattedData = format_data(data=fullData, years=years)
    
    updateStockPrices('ai_stock_trading_bot/database/historical_data.db', symbol, formattedData)

    return

