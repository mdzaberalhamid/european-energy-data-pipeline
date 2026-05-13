import requests
import pandas as pd
import os

# Countries / bidding zones
zones = {
    "Germany": "DE-LU",
    "Denmark_West": "DK1",
    "Denmark_East": "DK2",
    "France": "FR",
    "Netherlands": "NL"
}

# Empty list to store dataframes
all_data = []

# Looping through zones
for country, zone in zones.items():

    print(f"Fetching data for {country}...")

    url = (
        f"https://api.energy-charts.info/price?"
        f"bzn={zone}&start=2025-01-01&end=2025-01-07"
    )

    response = requests.get(url)
    data = response.json()

    # Creating dataframe
    df = pd.DataFrame({
        "timestamp": data["unix_seconds"],
        "price_eur_mwh": data["price"]
    })

    # Adding metadata
    df["country"] = country
    df["zone"] = zone

    # Converting timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    all_data.append(df)

# Combining all countries
final_df = pd.concat(all_data, ignore_index=True)

# Creating folder if missing
os.makedirs("data/raw", exist_ok=True)

# Saving CSV
output_path = "data/raw/europe_energy_prices.csv"
final_df.to_csv(output_path, index=False)

print("\nData saved successfully!")
print(final_df.head())