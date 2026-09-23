import pandas as pd
import numpy as np
import os

def haversine_np(lat1, lon1, lat2, lon2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

def load_and_clean_data(raw_path=None, processed_path=None):
    if raw_path is None:
        raw_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'food_delivery_raw.csv')
    if processed_path is None:
        processed_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'food_delivery_clean.csv')

    df = pd.read_csv(raw_path)
    print("Initial shape:", df.shape)

    # 1. Clean string columns - strip spaces
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    # 2. Replace 'NaN', 'null', 'nan', 'NaN ' with np.nan
    df.replace({'NaN': np.nan, 'nan': np.nan, 'null': np.nan, '': np.nan}, inplace=True)

    # 3. Clean Target variable 'Time_taken(min)' -> 'delivery_time_min' (analogous to handleRate in Zomato reference)
    def clean_time_taken(val):
        if pd.isna(val):
            return np.nan
        val = str(val).replace('(min)', '').strip()
        try:
            return float(val)
        except:
            return np.nan

    df['delivery_time_min'] = df['Time_taken(min)'].apply(clean_time_taken)

    # 4. Clean Weatherconditions: e.g. "conditions Fog" -> "Fog"
    df['Weatherconditions'] = df['Weatherconditions'].apply(
        lambda x: str(x).replace('conditions', '').strip() if pd.notna(x) else np.nan
    )

    # 5. Clean Numeric columns
    df['Delivery_person_Age'] = pd.to_numeric(df['Delivery_person_Age'], errors='coerce')
    df['Delivery_person_Ratings'] = pd.to_numeric(df['Delivery_person_Ratings'], errors='coerce')
    df['multiple_deliveries'] = pd.to_numeric(df['multiple_deliveries'], errors='coerce')
    df['Vehicle_condition'] = pd.to_numeric(df['Vehicle_condition'], errors='coerce')

    # 6. Parse Order Date and Time
    # Order_Date format is DD-MM-YYYY
    df['Order_Date_parsed'] = pd.to_datetime(df['Order_Date'], format='%d-%m-%Y', errors='coerce')
    df['day_of_week'] = df['Order_Date_parsed'].dt.day_name()
    df['is_weekend'] = df['Order_Date_parsed'].dt.dayofweek.apply(lambda x: 1 if x >= 5 else 0)

    # Time_Orderd format HH:MM:SS or HH:MM
    def extract_hour(val):
        if pd.isna(val):
            return np.nan
        try:
            parts = str(val).split(':')
            h = int(parts[0])
            if 0 <= h <= 23:
                return h
            return np.nan
        except:
            return np.nan

    df['order_hour'] = df['Time_Orderd'].apply(extract_hour)

    # 7. Calculate Distance (km) using Haversine formula
    # Filter out 0 coordinates or anomalous coords
    valid_coords = (
        (df['Restaurant_latitude'].abs() > 0.1) & 
        (df['Restaurant_longitude'].abs() > 0.1) & 
        (df['Delivery_location_latitude'].abs() > 0.1) & 
        (df['Delivery_location_longitude'].abs() > 0.1)
    )
    df['distance_km'] = np.nan
    df.loc[valid_coords, 'distance_km'] = haversine_np(
        df.loc[valid_coords, 'Restaurant_latitude'],
        df.loc[valid_coords, 'Restaurant_longitude'],
        df.loc[valid_coords, 'Delivery_location_latitude'],
        df.loc[valid_coords, 'Delivery_location_longitude']
    )

    # Cap unrealistic distances (e.g. > 50km for city food delivery) to NaN or reasonable threshold
    df.loc[df['distance_km'] > 50, 'distance_km'] = np.nan

    # 8. Handling Missing Values using DAP Reference Standard:
    # df.fillna(df.mean(numeric_only=True)) for numerical variables
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Mode imputation for key categorical columns
    categorical_cols = ['Weatherconditions', 'Road_traffic_density', 'Type_of_order', 'Type_of_vehicle', 'Festival', 'City']
    for c in categorical_cols:
        if c in df.columns:
            mode_val = df[c].mode()[0] if not df[c].mode().empty else 'Unknown'
            df[c] = df[c].fillna(mode_val)

    # 9. Derive Peak Hour target from actual demand distribution
    # Peak demand hours in food delivery are lunch (12-14) and dinner (18-23)
    # Let's verify by actual hourly frequency
    hourly_counts = df['order_hour'].round().astype(int).value_counts()
    peak_hours = [12, 13, 14, 18, 19, 20, 21, 22, 23]
    df['is_peak_hour'] = df['order_hour'].apply(lambda h: 1 if int(round(h)) in peak_hours else 0)

    # Compute order demand load per hour for demand forecasting
    hourly_demand_map = df['order_hour'].round().astype(int).map(hourly_counts)
    df['hourly_demand_volume'] = hourly_demand_map

    print("Cleaned DataFrame info:")
    print(df.info())
    print("\nSample records:")
    print(df[['order_hour', 'day_of_week', 'distance_km', 'delivery_time_min', 'Road_traffic_density', 'is_peak_hour', 'hourly_demand_volume']].head(5))

    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    df.to_csv(processed_path, index=False)
    print(f"Saved processed dataset to {processed_path}")
    return df

if __name__ == '__main__':
    load_and_clean_data()
