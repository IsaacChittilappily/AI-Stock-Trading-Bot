# this function pulls the stock data from the database, with parameters for the database name and the table name

def get_data_from_db(db_path: str, table_name: str):
    import sqlite3
    import numpy as np
    
    # connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # fetch the data
    query = f"SELECT Open, High, Low, Close, Volume FROM {table_name}"
    cursor.execute(query)
    data = cursor.fetchall()

    # close the connection
    conn.close()

    # convert to numpy array, with floats as the data type
    data = np.array(data, dtype=float)

    return data
