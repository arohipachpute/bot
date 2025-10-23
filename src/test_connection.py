from binance.client import Client
from src.config import BINANCE_API_KEY, BINANCE_SECRET_KEY

# Initialize Binance Client (Testnet mode)
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY, testnet=True)

try:
    account_info = client.futures_account()
    print("✅ Connection successful!")
    print("Account balance:", account_info['totalWalletBalance'])
except Exception as e:
    print("❌ Connection failed:", e)
