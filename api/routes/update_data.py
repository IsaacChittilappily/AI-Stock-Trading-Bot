from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
from ai_stock_trading_bot.data_collection.data_collection import collect_data
from flask_cors import CORS

update_data_blueprint = Blueprint('update_data', __name__)
CORS(update_data_blueprint) # Enable CORS for the entire blueprint

@update_data_blueprint.route('/update_stock_data', methods=['POST'])
def update_stock_data():
    try:
        # get symbol from request JSON
        data = request.get_json()
        if 'symbol' not in data:
            return jsonify({'error': 'Symbol not provided'}), 400
            
        symbol = data['symbol']
        years = data.get('years', 10)  # default to 10 years if not specified
        
        # load environment variables
        load_dotenv()
        alpha_vantage_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        
        if not alpha_vantage_key:
            return jsonify({'error': 'Alpha Vantage API key not found'}), 500
            
        # collect data for the symbol
        collect_data(alpha_vantage_key, symbol, years)
        
        return jsonify({
            'message': f'Successfully updated database for {symbol}',
            'symbol': symbol,
            'years': years
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
