import unittest
from api import create_app
import json

class TestMakeTrade(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        
    def test_make_trade(self):
        # test with valid data
        test_data = {
            'symbol': 'AAPL',
            'buy_threshold': 2.0,
            'sell_threshold': 2.0
        }
        r = self.client.post('/make_trade',
                           json=test_data,
                           headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.data)
        self.assertIn('decision', data)
        self.assertIn(data['decision'], ['buy', 'sell', None])
        
        # test missing symbol
        test_data = {
            'buy_threshold': 2.0,
            'sell_threshold': 2.0
        }
        r = self.client.post('/make_trade',
                           json=test_data,
                           headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code, 400)
        
        # test missing thresholds
        test_data = {
            'symbol': 'MSFT'
        }
        r = self.client.post('/make_trade',
                           json=test_data,
                           headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.data)
        self.assertIn('decision', data)
        self.assertIn(data['decision'], ['buy', 'sell', None])

if __name__ == '__main__':
    unittest.main()
