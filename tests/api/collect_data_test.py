import unittest
from api import create_app
import json

class TestCollectData(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        
    def test_update_stock_data(self):
        # test with valid data
        test_data = {
            'symbol': 'AAPL',
            'years': 5
        }
        r = self.client.post('/update_stock_data',
                           json=test_data,
                           headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.data)
        self.assertEqual(data['symbol'], 'AAPL')
        self.assertEqual(data['years'], 5)
        
        # test missing symbol
        test_data = {
            'years': 5
        }
        r = self.client.post('/update_stock_data',
                           json=test_data,
                           headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code, 400)
        
        # test default years parameter
        test_data = {
            'symbol': 'MSFT'
        }
        r = self.client.post('/update_stock_data',
                           json=test_data,
                           headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.data)
        self.assertEqual(data['years'], 10)

if __name__ == '__main__':
    unittest.main()
