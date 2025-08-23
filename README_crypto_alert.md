# Crypto Price Alert - Starter Script

This repo contains a single-file Python tool `crypto_price_alert.py` that polls CoinGecko for crypto prices and sends email alerts when user-defined thresholds are crossed.

## What it does
- Polls CoinGecko simple price API for specified coin IDs (e.g., `bitcoin`, `ethereum`).
- Logs prices to CSV with UTC timestamps.
- Sends aggregated email alerts when thresholds are crossed (supports `below` and `above` thresholds).

## Requirements
- Python 3.8+
- `requests` package
- Optional: `schedule` package for scheduling (the script uses `time.sleep` by default)

Install dependencies:
```
pip install requests schedule
```

## Usage
1. Edit `config_example.json` with your coins, thresholds and email SMTP details.
2. Run:
```
python3 crypto_price_alert.py --config config_example.json
```
Or use CLI options to override config values:
```
python3 crypto_price_alert.py --coins bitcoin,ethereum --interval 60 --thresholds bitcoin:below:40000,ethereum:above:2000 --notify-email you@example.com --smtp-server smtp.example.com --smtp-port 587 --smtp-user you --smtp-pass secret
```

## Packaging / Selling tips
- Add a simple GUI (Tkinter or a tiny Flask UI) for non-technical buyers.
- Provide a Dockerfile and a one-click deploy guide for Render/Heroku.
- Offer customization (support for more exchanges, SMS alerts via Twilio, historical charts) as paid add-ons.
- Provide an installation + setup service listing when selling the script on marketplaces.

## License
MIT
