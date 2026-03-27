import pandas as pd

def process_data(file_path):
    df = pd.read_csv(file_path)

    # Feature Engineering
    df["price_per_km"] = df["price"] / df["distance"]

    df["is_peak_hour"] = df["hour"].apply(
        lambda x: 1 if x in [7,8,9,17,18,19] else 0
    )

    df["weather_encoded"] = df["short_summary"].astype("category").cat.codes

    df.to_csv(file_path, index=False)

    return df