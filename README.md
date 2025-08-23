# Crypto Price Alert - Starter Script

This repo contains a single-file Python tool `crypto_price_alert.py` that polls CoinGecko for crypto prices and sends email alerts when user-defined thresholds are crossed.

---

## What it does
- Polls CoinGecko simple price API for specified coin IDs (e.g., `bitcoin`, `ethereum`).
- Logs prices to CSV with UTC timestamps.
- Sends aggregated email alerts when thresholds are crossed (supports `below` and `above` thresholds).
- Runs on any system with Python 3.8+ — lightweight, portable, and simple to deploy.

---

## Screenshots

Here’s what the tool looks like in action:

![Terminal Demo](images/terminal_demo.png)  
*Script running in the terminal, tracking Bitcoin & Ethereum prices.*

![Email Alert](images/email_alert.png)  
*Example email alert when thresholds are triggered.*

---

## Why this tool?
Most people don’t have the time (or nerves) to refresh charts every 5 minutes.  
This script solves **“price anxiety”** by automatically monitoring the market for you.  
Whether you’re a day trader or a long-term investor, it ensures you’ll **never miss big moves**.

Instead of being glued to your phone or laptop, you can relax and let the script do the boring work of watching charts. It will only disturb you when something important happens — like a major dip or breakout. That means **less stress, fewer missed opportunities, and more peace of mind**.

---

## Key Features
- **Simple configuration**: All settings stored in a JSON file — no coding required.  
- **Multi-coin support**: Track multiple cryptocurrencies at once.  
- **Threshold-based alerts**: Set specific price targets, both above and below.  
- **Email integration**: Direct alerts to your inbox using SMTP.  
- **Lightweight & fast**: No heavy frameworks, just Python + requests.  

---

## Requirements
- Python 3.8+
- `requests` package
- Optional: `schedule` package for scheduling (the script uses `time.sleep` by default)

Install dependencies:
```bash
pip install requests schedule


python3 crypto_price_alert.py \
  --coins bitcoin,ethereum \
  --interval 60 \
  --thresholds bitcoin:below:40000,ethereum:above:2000 \
  --notify-email you@example.com \
  --smtp-server smtp.example.com \
  --smtp-port 587 \
  --smtp-user you \
  --smtp-pass secret

## About Me

Hey there 👋 I’m **XXai®**, a web developer with a passion for automation, clean code, and building tools that actually make life easier.  

I’ve always believed programming is more than just typing code — it’s about solving real problems and saving people time. That’s why I enjoy working on projects like this crypto alert system: small, powerful, and practical.  

When I’m not coding, I’m usually exploring new tech trends, reading about finance, or experimenting with side projects. I enjoy blending **traditional knowledge** (the way things have always been done) with **forward-thinking ideas** (new tools, modern stacks, and creative solutions).  

- 💻 Skilled in **Python, JavaScript, and web frameworks**.  
- 🚀 Currently building automation tools & scripts for traders and everyday users.  
- 🌍 Open to collaborations, freelance gigs, and interesting challenges.  
- 📩 Contact: [your-email@example.com]  

If this project helped you, consider giving it a ⭐ and sharing it with others. I’d love to hear feedback, ideas, or even just a “hey” from fellow developers and crypto enthusiasts.  
