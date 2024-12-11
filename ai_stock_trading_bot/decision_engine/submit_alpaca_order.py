# function to submit a paper trade order to Alpaca, given the API connection, symbol, side and quantity#

def submit_paper_trade(api, symbol: str, qty: float, side: str) -> dict:
    """
    Submit a paper trade order to Alpaca
    
    Args:
        api (tradeapi.REST): Alpaca API connection
        symbol (str): The stock symbol
        qty (float): Quantity of shares
        side (str): 'buy' or 'sell'
        
    Returns:
        dict: Order details from Alpaca
    """
    try:
        # Validate inputs
        if not symbol or not isinstance(symbol, str):
            raise ValueError("Symbol must be a non-empty string")
        
        if not qty or qty <= 0:
            raise ValueError("Quantity must be a positive number")
        
        if not side or side.lower() not in ['buy', 'sell']:
            raise ValueError("Side must be either 'buy' or 'sell'")
            
        # check buying power for buy orders - if the user does not have enough money the request should not be permitted
        if side.lower() == 'buy':
            account = api.get_account()
            last_trade = api.get_latest_trade(symbol)
            if float(account.buying_power) < qty * last_trade.price:
                raise ValueError("Insufficient buying power")
        
        # submit the order
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force='gtc'
        )
        
        # return the order
        return order
        
    except Exception as e:
        print(f"Error submitting order: {e}")
        return None
    
