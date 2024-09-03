import pandas as pd
import matplotlib.pyplot as plt

# Load data
rides_data = pd.read_csv(r"C:\Users\Patrick\Downloads\BIKEDATASET4.csv")
station_capacity = pd.read_csv(r"C:\Users\Patrick\Downloads\capacity3.csv")

# Convert date to datetime
rides_data['date'] = pd.to_datetime(rides_data['starttime'])

# Round start time to nearest 30 minutes
rides_data['start_time_rounded'] = rides_data['date'].dt.round('30min')

# Round end time to nearest 30 minutes
rides_data['end_time_rounded'] = rides_data['date'].dt.round('30min')

# Calculate net change in bikes for each 30-minute interval
start_counts = rides_data.groupby(['start station id', 'start_time_rounded']).size().reset_index(name='start_count')
end_counts = rides_data.groupby(['end station id', 'end_time_rounded']).size().reset_index(name='end_count')

# Merge start and end counts
net_change_by_interval = pd.merge(end_counts, start_counts, left_on=['end station id', 'end_time_rounded'],
                                  right_on=['start station id', 'start_time_rounded'], how='outer')

# Calculate the net change
net_change_by_interval['net_change'] = (net_change_by_interval['end_count'].fillna(0) -
                                        net_change_by_interval['start_count'].fillna(0))

# Select relevant columns
net_change_by_interval = net_change_by_interval[['start station id', 'start_time_rounded','end station id', 'end_time_rounded', 'net_change']]

# Merge net change by interval with station capacity data
station_data = pd.merge(net_change_by_interval, station_capacity, left_on='end station id', right_on='ID')

# Calculate available bikes at each station for each time
station_data['available_bikes'] = station_data.groupby('end station id')['net_change'].cumsum()

# Calculate depletion status
station_data['depletion_status'] = station_data['available_bikes'] / station_data['CAPACITY']


# Save results to CSV
station_data.to_csv(r"C:\Users\Patrick\Downloads\stockout_risk4.csv", index=False)

# Display first few rows of results
print(station_data.head())
