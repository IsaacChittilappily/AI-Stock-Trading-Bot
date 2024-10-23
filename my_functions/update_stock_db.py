# function that takes in formatted data as a dataframe and updates the database with the relevant information

def updateStockPrices(db_name: str, symbol: str, df) -> None:

    import sqlite3

    db = sqlite3.connect(db_name)
    # connect to the database using sqlite

    df.to_sql(symbol, db, if_exists='replace', index=False)
    # converts dataframe to sql database and if the table for that stock already exists, replace it with the new table 

    db.commit()
    db.close()
    # commit the changes and close the connection

    return
