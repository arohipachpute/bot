#!/usr/bin/env python3
"""
Simplified Binance Futures Testnet Trading Bot
Author: Your Name
"""

import os
import time
import logging
import argparse
from binance import Client, exceptions
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# Configure logging
logging.basicConfig(
    filename="bot_trades.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        # Set API URL to Binance Futures Testnet
        self.client.API_URL = "https://testnet.binancefuture.com"
        logger.info("Initialized Binance Futures Testnet client")

    def place_market_order(self, symbol, side, quantity):
        """Place a market order"""
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(f"Market Order: {side} {quantity} {symbol}")
            logger.info(order)
            print(f"✅ Market {side} order placed successfully.")
            return order
        except exceptions.BinanceAPIException as e:
            logger.error(f"API Error: {e}")
            print(f"❌ API Error: {e}")
        except Exception as e:
            logger.exception("Error placing market order")
            print(f"❌ Unexpected error: {e}")

    def place_limit_order(self, symbol, side, quantity, price):
        """Place a limit order"""
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logger.info(f"Limit Order: {side} {quantity} {symbol} @ {price}")
            logger.info(order)
            print(f"✅ Limit {side} order placed successfully at {price}.")
            return order
        except exceptions.BinanceAPIException as e:
            logger.error(f"API Error: {e}")
            print(f"❌ API Error: {e}")
        except Exception as e:
            logger.exception("Error placing limit order")
            print(f"❌ Unexpected error: {e}")

    def twap_order(self, symbol, side, total_quantity, slices, interval):
        """Place multiple market orders using TWAP logic"""
        slice_qty = total_quantity / slices
        print(f"📊 Starting TWAP order: {slices} slices of {slice_qty} {symbol}")
        for i in range(slices):
            print(f"🕐 Executing slice {i+1}/{slices}...")
            self.place_market_order(symbol, side, slice_qty)
            if i < slices - 1:
                time.sleep(interval)
        print("✅ TWAP order completed.")
        logger.info("TWAP order completed.")


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair, e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--otype", required=True, choices=["MARKET", "LIMIT", "TWAP"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price for LIMIT orders")
    parser.add_argument("--slices", type=int, default=3, help="TWAP slices")
    parser.add_argument("--interval", type=int, default=5, help="Seconds between TWAP slices")

    args = parser.parse_args()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("❌ Missing API keys. Please check your .env file.")
        return

    bot = BasicBot(api_key, api_secret, testnet=True)

    if args.otype == "MARKET":
        bot.place_market_order(args.symbol, args.side, args.quantity)

    elif args.otype == "LIMIT":
        if not args.price:
            print("❌ LIMIT order requires a --price argument.")
            return
        bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)

    elif args.otype == "TWAP":
        bot.twap_order(args.symbol, args.side, args.quantity, args.slices, args.interval)


if __name__ == "__main__":
    main()
