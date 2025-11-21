import requests
import pandas as pd
import datetime

# Étape 1: Extract
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    timestamp = datetime.datetime.now()

    # Étape 2: Transform
    rows = []
    for crypto, prices in data.items():
        rows.append({
            "crypto": crypto.capitalize(),
            "price_usd": prices["usd"],
            "price_eur": round(prices["usd"] * 0.92, 2),
            "change_24h": round(prices.get("usd_24h_change", 0), 2),
            "timestamp": timestamp
        })

    df = pd.DataFrame(rows)

    # Étape 3: Load
    csv_file = "crypto_prices.csv"
    header = not pd.io.common.file_exists(csv_file)  # Écrit l’en-tête seulement la 1ère fois
    df.to_csv(csv_file, mode="a", header=header, index=False)

    print(f"✅ Données sauvegardées dans {csv_file}")
    print(df)
else:
    print("❌ Erreur API:", response.status_code)