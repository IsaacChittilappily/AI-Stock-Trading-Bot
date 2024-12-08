import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# Load environment variables
load_dotenv()
ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
ALPACA_API_BASE_URL = os.getenv('ALPACA_API_BASE_URL')

# Initialize trading client
trading_client = TradingClient(ALPACA_API_KEY, ALPACA_SECRET_KEY, paper=True)

def submit_trade_order(symbol: str, qty: float, side: str) -> dict:
    """
    Submit a market order to Alpaca
    
    Args:
        symbol (str): The stock symbol
        qty (float): Quantity of shares
        side (str): 'buy' or 'sell'
        
    Returns:
        dict: Order details from Alpaca
    """
    # Validate inputs
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")
    if not qty or qty <= 0:
        raise ValueError("Quantity must be a positive number")
    if not side or side.lower() not in ['buy', 'sell']:
        raise ValueError("Side must be either 'buy' or 'sell'")
        
    # Create order data
    order_side = OrderSide.BUY if side.lower() == 'buy' else OrderSide.SELL
    
    market_order = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=order_side,
        time_in_force=TimeInForce.GTC
    )
    
    try:
        # Check if we have enough buying power for buy orders
        if side.lower() == 'buy':
            account = trading_client.get_account()
            if float(account.buying_power) < qty * trading_client.get_latest_trade(symbol).price:
                raise ValueError("Insufficient buying power")
                
        # Submit order
        order = trading_client.submit_order(market_order)
        print(f"Order submitted successfully: {order}")
        return order
    
    except Exception as e:
        print(f"Error submitting order: {e}")
        return None

if __name__ == '__main__':
    # Test with proper error handling
    try:
        result = submit_trade_order('AAPL', 1, 'buy')
        if result is None:
            print("Order submission failed")
    except ValueError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
