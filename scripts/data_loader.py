import pandas as pd
import urllib.request
import io
import os

def download_and_prepare_raw_data():
    raw_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    os.makedirs(raw_dir, exist_ok=True)
    raw_file = os.path.join(raw_dir, 'food_delivery_raw.csv')
    
    if os.path.exists(raw_file) and os.path.getsize(raw_file) > 1000:
        print(f"Raw dataset already exists at {raw_file}")
        return pd.read_csv(raw_file)

    print("Fetching real Online Food Delivery benchmark dataset...")
    base_url = "https://raw.githubusercontent.com/Ritik1129/Food_Delivery_Dataset/main/"
    tables = {
        'orders': base_url + "order_details_table.csv",
        'delivery_person': base_url + "delivery_person_table.csv",
        'location': base_url + "location_details_table.csv"
    }

    dfs = {}
    for name, url in tables.items():
        print(f"Downloading {name} table...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            dfs[name] = pd.read_csv(io.BytesIO(data))
        print(f"  {name} shape: {dfs[name].shape}")

    # Merge on 'ID'
    print("Merging tables on 'ID'...")
    merged_df = dfs['orders'].merge(dfs['delivery_person'], on='ID', how='inner')
    merged_df = merged_df.merge(dfs['location'], on='ID', how='inner')

    print(f"Merged dataset shape: {merged_df.shape}")
    merged_df.to_csv(raw_file, index=False)
    print(f"Saved raw dataset to {raw_file}")
    return merged_df

if __name__ == '__main__':
    df = download_and_prepare_raw_data()
    print("Columns:", df.columns.tolist())
    print(df.head(3))
