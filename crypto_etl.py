import pandas as pd
import requests
from datetime import datetime
import os

# Step 1: Get data from CoinGecko API
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd&include_market_cap=true&include_24hr_change=true"
response = requests.get(url)
data = response.json()
print(data)

# Step 2: Prepare the data
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
rows = []
for coin, info in data.items():
    rows.append({
        "Timestamp": timestamp,
        "Coin": coin.capitalize(),
        "Price (USD)": info['usd'],
        "Market Cap (USD)": info['usd_market_cap'],
        "24h Change (%)": round(info['usd_24h_change'], 2)
    })

df = pd.DataFrame(rows)

# Step 3: Save to CSV
output_path = "data/crypto_prices.csv"
file_exists = os.path.exists(output_path)
df.to_csv(output_path, mode='a', index=False, header=not file_exists)

print("✅ Crypto prices saved to:", output_path)
