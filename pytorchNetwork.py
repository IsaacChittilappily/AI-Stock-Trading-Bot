from my_functions.pull_db_data import get_data_from_db

db_path = 'historical_data.db' 
table_name = 'AAPL'     
data = get_data_from_db(db_path, table_name)

print(data)