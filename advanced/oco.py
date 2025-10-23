import sys
from datetime import datetime
from src.config import BINANCE_API_KEY, BINANCE_SECRET_KEY
from binance.client import Client

# Initialize Binance client
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY, testnet=True)

# Logging function
def log_action(message):
    with open("bot.log", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

# OCO order function (dry-run example)
def place_oco_order(symbol, side, quantity, take_profit_price, stop_loss_price, dry_run=True):
    if dry_run:
        log_action(f"DRY-RUN: OCO {side} {quantity} {symbol}, TP: {take_profit_price}, SL: {stop_loss_price} simulated.")
        print(f"DRY-RUN: OCO {side} {quantity} {symbol}, TP: {take_profit_price}, SL: {stop_loss_price} simulated.")
        return
    try:
        order = client.futures_create_oco_order(
            symbol=symbol,
            side=side.upper(),
            quantity=quantity,
            price=str(take_profit_price),
            stopPrice=str(stop_loss_price),
            stopLimitPrice=str(stop_loss_price),  # Use same as stop price
            stopLimitTimeInForce="GTC"
        )
        log_action(f"OCO order executed: {order}")
        print("OCO order executed:", order)
    except Exception as e:
        log_action(f"Error placing OCO order: {e}")
        print("Error:", e)

# CLI arguments
if len(sys.argv) != 6:
    print("Usage: python oco.py SYMBOL BUY/SELL QUANTITY TAKE_PROFIT_PRICE STOP_LOSS_PRICE")
    sys.exit(1)

symbol = sys.argv[1].upper()
side = sys.argv[2].upper()
quantity = float(sys.argv[3])
take_profit_price = float(sys.argv[4])
stop_loss_price = float(sys.argv[5])

# Place the OCO order (dry-run by default)
place_oco_order(symbol, side, quantity, take_profit_price, stop_loss_price, dry_run=True)

