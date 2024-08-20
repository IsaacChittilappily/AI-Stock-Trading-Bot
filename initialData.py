import requests
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
# this package automatically loads the .env file in the root directory - this ensures that the API keys are not exposed

api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
print(api_key)
