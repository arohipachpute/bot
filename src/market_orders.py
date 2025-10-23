import sys
from datetime import datetime
from src.config import BINANCE_API_KEY, BINANCE_SECRET_KEY
from binance.client import Client

# Initialize Binance client
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY, testnet=True)

# Log function
def log_action(message):
    with open("bot.log", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

# Market order function (dry-run example)
def place_market_order(symbol, side, quantity, dry_run=True):
    if dry_run:
        log_action(f"DRY-RUN: {side} {quantity} {symbol} order simulated.")
        print(f"DRY-RUN: {side} {quantity} {symbol} order simulated.")
        return
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        log_action(f"Order executed: {order}")
        print("Order executed:", order)
    except Exception as e:
        log_action(f"Error placing order: {e}")
        print("Error:", e)

# CLI arguments
if len(sys.argv) != 4:
    print("Usage: python market_orders.py SYMBOL BUY/SELL QUANTITY")
    sys.exit(1)

symbol = sys.argv[1].upper()
side = sys.argv[2].upper()
quantity = float(sys.argv[3])

# Place the order (dry-run by default)
place_market_order(symbol, side, quantity, dry_run=True)

