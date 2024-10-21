# function to take data as a paramter in json form, and return a dataframe with the collumns labelled and formatted correctly
# also filters the data so that only the desired time period remains
def format_data(data, years: int):

    import pandas as pd

    # only take the time series entries from the data (as we do not need the other information)
    time_series = data['Time Series (Daily)']


    # convert the time series data into a dataframe
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.index = pd.to_datetime(df.index)
    df = df.rename_axis('Date').reset_index()

    # rename columns so they are more readable
    df = df.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    })

    # sort the data to filter out the values outside the range
    timePeriod = pd.Timestamp.now() - pd.DateOffset(years=years)
    df = df[df['Date'] >= timePeriod].sort_values('Date')

    # return the dataframe 
    return df