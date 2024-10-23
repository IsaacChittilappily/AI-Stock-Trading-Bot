def get_data_from_db(db_path, table_name):
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

    # convert to numpy array
    data = np.array(data, dtype=float)

    return data

db_path = 'historical_data.db' 
table_name = 'AAPL'     
data = get_data_from_db(db_path, table_name)

X_min = np.min(data, axis=0)
X_max = np.max(data, axis=0)
X_scaled = (data - X_min) / (X_max - X_min)
print(X_scaled)