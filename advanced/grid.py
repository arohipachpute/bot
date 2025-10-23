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

# Grid order function (dry-run)
def place_grid_orders(symbol, lower_price, upper_price, steps, quantity_per_order, dry_run=True):
    price_step = (upper_price - lower_price) / (steps - 1)
    for i in range(steps):
        buy_price = lower_price + i * price_step
        sell_price = lower_price + (i + 1) * price_step if i < steps - 1 else upper_price

        if dry_run:
            log_action(f"DRY-RUN: Grid BUY {quantity_per_order} {symbol} at {buy_price:.2f}")
            log_action(f"DRY-RUN: Grid SELL {quantity_per_order} {symbol} at {sell_price:.2f}")
            print(f"DRY-RUN: Grid BUY {quantity_per_order} {symbol} at {buy_price:.2f}")
            print(f"DRY-RUN: Grid SELL {quantity_per_order} {symbol} at {sell_price:.2f}")
        else:
            try:
                client.futures_create_order(
                    symbol=symbol,
                    side="BUY",
                    type="LIMIT",
                    quantity=quantity_per_order,
                    price=str(buy_price),
                    timeInForce="GTC"
                )
                client.futures_create_order(
                    symbol=symbol,
                    side="SELL",
                    type="LIMIT",
                    quantity=quantity_per_order,
                    price=str(sell_price),
                    timeInForce="GTC"
                )
                log_action(f"Grid orders placed at BUY: {buy_price:.2f}, SELL: {sell_price:.2f}")
            except Exception as e:
                log_action(f"Error placing grid order: {e}")
                print("Error:", e)

# CLI arguments
if len(sys.argv) != 6:
    print("Usage: python grid.py SYMBOL LOWER_PRICE UPPER_PRICE STEPS QUANTITY_PER_ORDER")
    sys.exit(1)

symbol = sys.argv[1].upper()
lower_price = float(sys.argv[2])
upper_price = float(sys.argv[3])
steps = int(sys.argv[4])
quantity_per_order = float(sys.argv[5])

# Place grid orders (dry-run by default)
place_grid_orders(symbol, lower_price, upper_price, steps, quantity_per_order, dry_run=True)
