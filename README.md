# Binance Futures Trading Bot

A Python trading bot for Binance Futures Testnet that executes Market, Limit, and TWAP orders via command-line interface.

## Requirements

- Python 3.8+
- Binance Futures Testnet account
- API Key and Secret

## Installation
```bash
pip install python-binance python-dotenv
```

Create `.env` file:
```
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```


## Files

- `bot.py` - Main trading bot
- `test_connection.py` - Verify API connection
- `bot_trades.log` - Trade logs

## Get API Keys

1. Visit https://testnet.binancefuture.com
2. Login and go to API Key Management
3. Generate API key and secret
4. Add to `.env` file

## Disclaimer

This bot uses Binance Testnet with virtual funds. For educational purposes only.
