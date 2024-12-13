# this function takes in the closing price of one day and the predicted closing price of the next day
# and if the percentage difference between them is too high/too low it will buy/sell accordingly

def trade_decision(close: float, predicted_close: float, buy_threshold: float, sell_threshold: float) -> int:

    # make sure the thresholds are negative and positive (input sanitation)
    buy_threshold = abs(buy_threshold)
    sell_threshold = -abs(sell_threshold)
    
    # calculates the percentage difference between the predicted closing price and the old price
    diff = ((predicted_close - close) / close) * 100


    # if the percentage difference is above/below the buy/sell threshold, return 'buy' or 'sell'
    if diff <= sell_threshold: return 'sell'
    elif diff >= buy_threshold: return 'buy'
    
    # in all other cases return None, which indicates a hold decision (will evaluate to False in the main function)
    return None

