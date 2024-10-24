# function that takes in formatted data as a dataframe and updates the database with the relevant information

def updateStockPrices(db_name: str, symbol: str, df) -> None:

    import sqlite3

    # connect to the database using sqlite
    db = sqlite3.connect(db_name)

    # converts dataframe to sql database and if the table for that stock already exists, replace it with the new table 
    df.to_sql(symbol, db, if_exists='replace', index=False)

    # commit the changes and close the connection
    db.commit()
    db.close()

    return
