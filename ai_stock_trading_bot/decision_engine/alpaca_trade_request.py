import alpaca_trade_request
from dotenv import load_dotenv

load_dotenv()

def buySellHold(decision):
    match decision:

        case 0:
            return
        
        case 1:
            