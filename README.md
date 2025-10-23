# Arohi Binance Futures Order Bot

A **CLI-based trading bot** for **Binance USDT-M Futures** with core and advanced order types, input validation, structured logging, and dry-run simulation. Designed to test trading strategies safely on **Binance Testnet** before using real funds.

---

## 🚀 Features

### Core Orders
- **Market Orders**: Buy/sell instantly at market price.  
- **Limit Orders**: Place orders at a specific target price.  

### Advanced Orders
- **Stop-Limit Orders**: Trigger a limit order when a stop price is reached.  
- **OCO (One-Cancels-the-Other)**: Place take-profit & stop-loss simultaneously.  
- **TWAP (Time-Weighted Average Price)**: Split large orders into smaller chunks over time for better execution.  

### Validation & Logging
- Validates **symbols, quantities, and prices** before placing orders.  
- Logs all actions, errors, and simulated executions in `bot.log`.  

---

## 🗂 Project Structure

arohi_binance_bot/
│
├── src/
│ ├── market_orders.py # Market order logic
│ ├── limit_orders.py # Limit order logic
│ ├── advanced/
│ │ ├── oco.py # OCO order logic
│ │ └── twap.py # TWAP strategy
│ └── test_connection.py # Test Binance API connection
├── bot.log # Logs of orders/actions
├── config.py # API keys and configuration
├── report.pdf # Assignment report
└── README.md # Project documentation
## ⚙️ Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/arohipachpute/arohi_binance_bot.git
cd arohi_binance_bot
Install dependencies

bash
Copy code
pip install python-binance
Add Binance API keys in src/config.py (Testnet recommended)

python
Copy code
BINANCE_API_KEY = "your_api_key_here"
BINANCE_SECRET_KEY = "your_secret_key_here"
BASE_URL = "https://testnet.binancefuture.com"
💻 Usage Examples
Test Connection
bash
Copy code
python -m src.test_connection
Market Order
bash
Copy code
python -m src.market_orders BTCUSDT BUY 0.01
Limit Order
bash
Copy code
python -m src.limit_orders BTCUSDT BUY 0.01 30000
TWAP Order (Dry-run)
bash
Copy code
python -m src.advanced.twap BTCUSDT BUY 0.05 5 10
OCO Order
bash
Copy code
python -m src.advanced.oco BTCUSDT BUY 0.01 32000 28000
⚠️ Notes
Always test on Binance Testnet before trading with real money.

Keep API keys private; do not commit them.

Advanced strategies (like Grid Orders) can be added in future updates.

