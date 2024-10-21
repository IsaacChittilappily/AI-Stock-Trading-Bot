# function that takes in formatted data as a dataframe and updates the database with the relevant information

def updateStockPrices(symbol: str, df) -> None:

    import sqlite3

    db = sqlite3.connect('historical_data.db')
    # connect to the database using sqlite

    df.to_sql(f'{symbol}_stock_data', db, if_exists='replace', index=False)
    # if the table for that stock already exists, replace it with the new table 

    db.commit()
    db.close()
    # commit the changes and close the connection

    return
