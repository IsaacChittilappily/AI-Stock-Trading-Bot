# scales a list of values taking the lowest value to be 0 and the highest to be 1

def min_max_scaler(arr: list) -> list:

    import numpy as np
    
    # get the min and max values from the list
    mini, maxi = min(arr), max(arr)

    # create a new list with the scaled values
    scaled = [(1/(maxi-mini)) * (val - mini) for val in arr]

    return scaled

