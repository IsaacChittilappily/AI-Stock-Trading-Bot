# this function takes in the closing price of one day and the predicted closing price of the next day
# and if the percentage difference between them is too high/too low it will buy/sell accordingly

def trade_decision(close: float, predictedClose: float, buyThreshold: float, sellThreshold: float) -> int:

    # make sure the thresholds are negative and positive (input sanitation)
    buyThreshold = abs(buyThreshold)
    sellThreshold = -abs(sellThreshold)
    
    # calculates the percentage difference between the predicted closing price and the old price
    diff = ((predictedClose - close) / close) * 100


    # if the percentage difference is above/below the buy/sell threshold, return a 1 or -1 to indicate a buy or sell decision
    if diff <= sellThreshold: return -1
    elif diff >= buyThreshold: return 1
    
    # in all other cases return 0, which indicates a hold decision
    return 0

