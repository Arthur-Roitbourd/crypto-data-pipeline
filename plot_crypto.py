import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv("crypto_prices.csv", parse_dates=["timestamp"])

# Pour cet exemple, on va simuler plusieurs jours si tu n’as qu’une ligne
# (ou tu peux relancer le script plusieurs fois dans la journée)

# On groupe par crypto et on trace l’évolution
plt.figure(figsize=(10, 6))

for crypto in df["crypto"].unique():
    subset = df[df["crypto"] == crypto].sort_values("timestamp")
    plt.plot(subset["timestamp"], subset["price_usd"], label=crypto, marker="o")

plt.title("📈 Évolution du prix des cryptos (USD)")
plt.xlabel("Date")
plt.ylabel("Prix (USD)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Sauvegarder
plt.tight_layout()
plt.savefig("crypto_dashboard.png")
plt.show()

print("✅ Graphique sauvegardé : crypto_dashboard.png")