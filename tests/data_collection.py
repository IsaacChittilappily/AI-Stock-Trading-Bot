import unittest
import pandas as pd
import sqlite3
import os
from ai_stock_trading_bot.data_collection.format_data import format_data
from ai_stock_trading_bot.data_collection.update_stock_db import updateStockPrices
from ai_stock_trading_bot.data_collection.data_collection import collect_data


class TestDataCollection(unittest.TestCase):
    
    def setUp(self):
        # Sample JSON data that mimics Alpha Vantage API response
        self.sample_data = {
            "Time Series (Daily)": {
                "2024-01-02": {
                    "1. open": "100.0",
                    "2. high": "105.0", 
                    "3. low": "99.0",
                    "4. close": "102.0",
                    "5. volume": "1000000"
                },
                "2023-01-01": {
                    "1. open": "98.0",
                    "2. high": "103.0",
                    "3. low": "97.0", 
                    "4. close": "100.0",
                    "5. volume": "900000"
                }
            }
        }
        
        # Test database path
        self.test_db = "test_database.db"

    def test_format_data(self):
        # Test data formatting
        df = format_data(self.sample_data, years=1)
        
        # Check if DataFrame has correct columns
        expected_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        self.assertEqual(list(df.columns), expected_columns)
        
        # Check data types
        self.assertTrue(isinstance(df.iloc[0]['Date'], pd.Timestamp))
        self.assertTrue(isinstance(df['Open'][0], float))
        
        # Check if data is sorted by date
        self.assertTrue(df['Date'].equals(df['Date'].sort_values()))

    def test_update_stock_db(self):
        # Create test DataFrame
        test_df = pd.DataFrame({
            'Date': ['2023-01-01', '2023-01-02'],
            'Open': [100.0, 101.0],
            'High': [102.0, 103.0],
            'Low': [98.0, 99.0],
            'Close': [101.0, 102.0],
            'Volume': [1000000, 1100000]
        })
        
        # Test database update
        updateStockPrices(self.test_db, 'AAPL', test_df)
        
        # Verify data was written correctly
        conn = sqlite3.connect(self.test_db)
        stored_df = pd.read_sql_query("SELECT * FROM AAPL", conn)
        conn.close()
        
        # Check if stored data matches input data
        pd.testing.assert_frame_equal(stored_df, test_df)

    def test_collect_data_invalid_api_key(self):
        # Test with invalid API key
        with self.assertRaises(Exception):
            collect_data("invalid_api_key", "AAPL", 1)

    def tearDown(self):
        # Clean up test database
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

if __name__ == '__main__':
    unittest.main()
