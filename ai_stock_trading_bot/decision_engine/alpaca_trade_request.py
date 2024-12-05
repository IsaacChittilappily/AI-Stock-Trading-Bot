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
    # Create order data
    order_side = OrderSide.BUY if side.lower() == 'buy' else OrderSide.SELL
    
    market_order = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=order_side,
        time_in_force=TimeInForce.GTC
    )
    
    try:
        # Submit order
        order = trading_client.submit_order(market_order)
        print(f"Order submitted successfully: {order}")
        return order
    except Exception as e:
        print(f"Error submitting order: {e}")
        return None


if __name__ == '__main__':
    submit_trade_order('AAPL', 1, 'buy')