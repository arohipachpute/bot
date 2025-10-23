import sys
import time
from datetime import datetime
from src.config import BINANCE_API_KEY, BINANCE_SECRET_KEY
from binance.client import Client

# Initialize Binance client
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY, testnet=True)

# Logging function
def log_action(message):
    with open("bot.log", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

# TWAP order function (dry-run)
def place_twap_order(symbol, side, total_quantity, chunks, interval_sec, dry_run=True):
    quantity_per_chunk = total_quantity / chunks
    for i in range(1, chunks + 1):
        if dry_run:
            log_action(f"DRY-RUN: TWAP {side} {quantity_per_chunk:.6f} {symbol}, chunk {i}/{chunks} simulated.")
            print(f"DRY-RUN: TWAP {side} {quantity_per_chunk:.6f} {symbol}, chunk {i}/{chunks} simulated.")
        else:
            try:
                order = client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="MARKET",
                    quantity=quantity_per_chunk
                )
                log_action(f"TWAP order executed: {order}")
                print("TWAP order executed:", order)
            except Exception as e:
                log_action(f"Error placing TWAP order: {e}")
                print("Error:", e)
        if i < chunks:
            time.sleep(interval_sec)

# CLI arguments
if len(sys.argv) != 6:
    print("Usage: python twap.py SYMBOL BUY/SELL TOTAL_QUANTITY CHUNKS INTERVAL_SEC")
    sys.exit(1)

symbol = sys.argv[1].upper()
side = sys.argv[2].upper()
total_quantity = float(sys.argv[3])
chunks = int(sys.argv[4])
interval_sec = int(sys.argv[5])

# Place the TWAP order (dry-run by default)
place_twap_order(symbol, side, total_quantity, chunks, interval_sec, dry_run=True)
