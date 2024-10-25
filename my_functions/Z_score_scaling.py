# scaling method that uses mean and standard deviation to scale values

def Z_score_scaler(arr: list) -> list:

    import numpy as np

    # get the mean and standard deviation using numpy
    mean = np.mean(arr)
    std = np.std(arr)

    # return the scaled values
    return (arr - mean) / std
