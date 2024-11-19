# this procedure combines all the other functions, and collects data for a certain stock

def collect_data(apikey: str, symbol: str, years: int):

    # imports the relevant packages from my files
    from data_collection.HTML_requests import get_request
    from data_collection.format_data import format_data
    from data_collection.update_stock_db import updateStockPrices

    # constructs the url to call alphavantage api
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={apikey}'

    # call the relevant functions to gather and format the data
    fullData = get_request(url)
    formattedData = format_data(data=fullData, years=years)
    
    updateStockPrices('historical_data.db', symbol, formattedData)

    return 


if __name__ == '__main___':

    import os
    from dotenv import load_dotenv

    # loads my env file which stores my alphavantage 
    load_dotenv()

    # parameters of the final function
    apikey = os.getenv('ALPHA_VANTAGE_API_KEY')
    symbol = 'AAPL'
    years = 10

    collect_data(apikey, symbol, years)
