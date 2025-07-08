# 📈 Crypto Price Alert Bot

A fully functional Telegram bot that helps users **track cryptocurrency prices** and get **automatic alerts** when a chosen coin reaches a target price.

## 🚀 Features

- 🔔 **Set Price Alerts**: Track your favorite coins with custom target prices.
- 💰 **Check Current Price**: Instantly check the live USD price of any major coin.
- 📊 **Top Gainers & Losers**: See what coins gained or lost the most in the last 24 hours.
- 🧾 **View Active Alerts**: See all of your active alerts with options to update or remove them.
- ❌ **Cancel All Alerts**: Instantly remove all alerts with one tap.
- 📋 **Easy to use menu**: All features accessible from a main keyboard menu.

## 🛠 Technologies Used

- Python 3.11+
- [Aiogram 3.x](https://github.com/aiogram/aiogram)
- SQLite (via `sqlite3`)
- CoinGecko API (for live price data)
- httpx (async requests)

## 🧠 How it works

1. Users press ➕ `Set Alert` to create a new price trigger.
2. If the coin is valid and the price hasn't been reached yet, the alert is saved.
3. The bot checks prices every 5 minutes in the background.
4. If the current price is **equal or above the target**, the bot sends a notification and removes that alert.

## 🔧 Setup

1. **Clone the repository**  
```bash
git clone https://github.com/RiaLnN/Crypto-Price-Alert-Bot.git
cd crypto-alert-bot
```
## 📎 Commands
Command	Description
- /start: Start the bot and show main menu
- help button: show help message
- ➕ Set Alert:	Set a price alert for any coin
- 📥 View Alerts:	View your current alerts
- ❌ Cancel All:	Cancel all alerts
- 💰 Check Price:	Check the current price of a coin
- 📈 Top Gainers:	Show top 10 coins by growth
- 🔻 Top Losers:	Show top 10 coins by drop
