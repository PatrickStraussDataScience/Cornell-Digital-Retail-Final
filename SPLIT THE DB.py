import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\Patrick\Downloads\BIKEDATASET4.csv")

# Convert starttime and stoptime to datetime objects
df['starttime'] = pd.to_datetime(df['starttime'])
df['stoptime'] = pd.to_datetime(df['stoptime'])

# Extract date and discrete time
df['date'] = df['starttime'].dt.date
df['discrete_start_time'] = df['discrete_start_time'].astype('str')

# Group by start station, date, and discrete start time for outgoing rides
outgoing_rides = df.groupby(['start station id', 'date', 'discrete_start_time']).agg({
    'start station name': 'first',
    'start station latitude': 'first',
    'start station longitude': 'first',
    'day_of_week': 'first',
    'month': 'first',
    'year': 'first',
    'season': 'first',
    'tripduration': 'sum'
}).reset_index()

# Save outgoing rides to CSV
outgoing_rides.to_csv(r"C:\Users\Patrick\Downloads\outgoing_rides.csv", index=False)

# Extract date and discrete stop time
df['date2'] = df['stoptime'].dt.date
df['discrete_stop_time'] = df['discrete_stop_time'].astype('str')

# Group by end station, date, and discrete stop time for incoming rides
incoming_rides = df.groupby(['end station id', 'date2', 'discrete_stop_time']).agg({
    'end station name': 'first',
    'end station latitude': 'first',
    'end station longitude': 'first',
    'day_of_week': 'first',
    'month': 'first',
    'year': 'first',
    'season': 'first',
    'tripduration': 'sum'
}).reset_index()

# Save incoming rides to CSV
incoming_rides.to_csv(r"C:\Users\Patrick\Downloads\incoming_rides.csv", index=False)
