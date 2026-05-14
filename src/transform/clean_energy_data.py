import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "europe_energy_prices.csv"

PROCESSED_DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "cleaned_energy_prices.csv"
)

# Creating a processed folder if it is missing
PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

# Loading raw dataset
df = pd.read_csv(RAW_DATA_PATH)

print("Raw dataset loaded.")
print(f"Dataset shape: {df.shape}")

# Cleaning Data

# Converting timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Removing duplicates
df = df.drop_duplicates()

# Removing missing prices
df = df.dropna(subset=["price_eur_mwh"])

# Removing unrealistic values
df = df[df["price_eur_mwh"] > -500]

# Sorting values
df = df.sort_values(by=["country", "timestamp"])

# Resetting index
df = df.reset_index(drop=True)

# Saving cleaned dataset
df.to_csv(PROCESSED_DATA_PATH, index=False)

print("\nTransformation completed successfully!")
print(f"Cleaned dataset shape: {df.shape}")

print("\nSample cleaned data:")
print(df.head())