from flask import Blueprint, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from ai_stock_trading_bot.decision_engine.trade_decision import trade_decision
from ai_stock_trading_bot.decision_engine.submit_alpaca_order import submit_paper_trade

load_dotenv()

make_trade_blueprint = Blueprint('make_trade', __name__)
CORS(make_trade_blueprint)

model_map = {
    'pytorch': 'ai_stock_trading_bot.models.pytorchNetwork',
    'iteration1': 'ai_stock_trading_bot.models.iteration1',
    'iteration2': 'ai_stock_trading_bot.models.iteration2', 
    'iteration3': 'ai_stock_trading_bot.models.iteration3'
}

@make_trade_blueprint.route('/make_trade', methods=['POST'])
def make_trade():
    try:
        # Get data from request
        data = request.get_json()
        
        if 'model_name' not in data:
            return jsonify({'error': 'Model name not provided'}), 400
        
        if 'symbol' not in data:
            return jsonify({'error': 'Stock symbol not provided'}), 400
            
        model_name = data['model_name']
        symbol = data['symbol']
        
        # Get optional parameters with defaults from .env
        buy_threshold = data.get('buy_threshold', float(os.getenv('BUY_THRESHOLD', 0.02)))
        sell_threshold = data.get('sell_threshold', float(os.getenv('SELL_THRESHOLD', -0.02)))
        api_key = data.get('api_key', os.getenv('ALPACA_API_KEY'))
        secret_key = data.get('secret_key', os.getenv('ALPACA_SECRET_KEY'))
        
        # Validate model name
        if model_name not in model_map:
            return jsonify({'error': f'Invalid model name. Choose from: {list(model_map.keys())}'}), 400
            
        # Import the selected model's predict_stock_price function
        module = __import__(model_map[model_name], fromlist=['predict_stock_price'])
        predict_stock_price = getattr(module, 'predict_stock_price')
        
        # Get prediction
        print(f'Running {model_name} network...')
        close_price, prediction = predict_stock_price(symbol)
        
        # Make trading decision
        action = trade_decision(close_price, prediction, buy_threshold, sell_threshold)
        
        # Submit paper trade if action is buy or sell
        trade_result = None
        if action:
            trade_result = submit_paper_trade(symbol, action, api_key, secret_key)
        
        return jsonify({
            'message': 'Successfully ran model prediction and trading decision',
            'model': model_name,
            'symbol': symbol,
            'prediction': prediction,
            'action': action,
            'trade_result': trade_result
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
