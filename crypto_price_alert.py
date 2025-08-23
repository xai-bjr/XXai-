"""
crypto_price_alert.py
----------------------
A premium script to monitor cryptocurrency prices and send Telegram alerts
when the price crosses a target threshold.

Author: XXai
License: MIT
Year: 2025
"""

import requests
import time

# ==== CONFIGURATION ====
COIN = "bitcoin"          # coin id from CoinGecko (e.g., "bitcoin", "ethereum")
CURRENCY = "usd"          # currency for price (usd, eur, etc.)
TARGET_PRICE = 30000.0    # price alert threshold
CHECK_INTERVAL = 60       # check every 60 seconds

# ==== TELEGRAM SETTINGS ====
# 1. Create a bot with BotFather: https://t.me/botfather
# 2. Copy the token it gives you.
# 3. Send /start to your bot from your Telegram account and get your chat_id
#    (use: https://api.telegram.org/bot<token>/getUpdates)
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# ==== FUNCTIONS ====
def get_price(coin: str, currency: str) -> float:
    """Fetch the current price of a coin in a currency from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin, "vs_currencies": currency}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[coin][currency]
    except Exception as e:
        print(f"[ERROR] Could not fetch price: {e}")
        return -1

def send_telegram_message(message: str):
    """Send a message to Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload, timeout=10)
        print("[INFO] Sent Telegram alert 🚀")
    except Exception as e:
        print(f"[ERROR] Could not send Telegram message: {e}")

def main():
    print("=== CRYPTO PRICE ALERT BOT ===")
    print(f"Monitoring {COIN.upper()} price in {CURRENCY.upper()} ...")
    print(f"Target alert set at: {TARGET_PRICE} {CURRENCY.upper()}")
    print("Press CTRL+C to stop.\n")

    while True:
        price = get_price(COIN, CURRENCY)
        if price == -1:
            time.sleep(CHECK_INTERVAL)
            continue

        print(f"[INFO] Current {COIN.upper()} price: {price} {CURRENCY.upper()}")

        if price >= TARGET_PRICE:
            alert_msg = (
                f"🚨 ALERT 🚨\n"
                f"{COIN.upper()} just hit {price} {CURRENCY.upper()}!\n"
                f"Target: {TARGET_PRICE} {CURRENCY.upper()}"
            )
            send_telegram_message(alert_msg)
            break

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
