import pandas as pd
from datetime import datetime, timedelta

# Load the dataset
df = pd.read_csv(r"C:\Users\Patrick\Downloads\CombinedTripsDataCLEANED.csv")

# Convert start time and stop time to datetime objects
df['starttime'] = pd.to_datetime(df['starttime'])
df['stoptime'] = pd.to_datetime(df['stoptime'])

# Define a function to round time to the next 5-minute interval
def round_to_nearest_5_minutes(time):
    minute_rounded = int(time.minute / 5) * 5
    return time.replace(minute=minute_rounded, second=0, microsecond=0)

# Add discrete_start_time column in military time format
df['discrete_start_time'] = df['starttime'].apply(round_to_nearest_5_minutes).dt.strftime('%H:%M')

# Add discrete_stop_time column in military time format with rounding
df['discrete_stop_time'] = df['stoptime'].apply(round_to_nearest_5_minutes).dt.strftime('%H:%M')

# Add season column
def get_season(month):
    if 3 <= month <= 5:
        return 'spring'
    elif 6 <= month <= 8:
        return 'summer'
    elif 9 <= month <= 11:
        return 'autumn'
    else:
        return 'winter'

df['season'] = df['month'].apply(get_season)

# Add day_of_week column
df['day_of_week'] = df['starttime'].dt.dayofweek

# Export the modified dataset to a new CSV file
export_path = r"C:\Users\Patrick\Downloads\BIKEDATASET4.csv"
df.to_csv(export_path, index=False)

print(f"Dataset exported to {export_path}")
