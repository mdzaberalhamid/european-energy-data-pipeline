import pandas as pd
from pathlib import Path
from src.config.db_config import engine

# Paths
BASE_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "cleaned_energy_prices.csv"
)

# Loading processed dataset
df = pd.read_csv(PROCESSED_DATA_PATH)

print("Processed dataset loaded successfully!")
print(f"Dataset shape: {df.shape}")

# Loading into PostgreSQL
df.to_sql(
    name="energy_prices",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nData loaded into PostgreSQL successfully!")