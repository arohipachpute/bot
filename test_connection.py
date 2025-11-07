from binance import Client
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# Initialize Binance Futures Testnet client
client = Client(api_key, api_secret, testnet=True)
client.API_URL = "https://testnet.binancefuture.com"

try:
    # Fetch account information
    account_info = client.futures_account()
    print("✅ Connection successful!")
    print(f"Total wallet balance: {account_info['totalWalletBalance']} USDT")
except Exception as e:
    print("❌ Connection failed:", e)
