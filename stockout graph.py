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

# Calculate start counts for each station and each 30-minute interval
start_counts = rides_data.groupby(['start_time_rounded', 'start station id']).size().reset_index(name='start_count')

# Calculate end counts for each station and each 30-minute interval
end_counts = rides_data.groupby(['end_time_rounded', 'end station id']).size().reset_index(name='end_count')

# Merge start and end counts
net_change_by_interval = pd.merge(end_counts, start_counts, left_on=['end_time_rounded', 'end station id'],
                                  right_on=['start_time_rounded', 'start station id'], how='outer')

# Calculate the net change
net_change_by_interval['net_change'] = net_change_by_interval['end_count'].fillna(0) - net_change_by_interval['start_count'].fillna(0)

# Select relevant columns
net_change_by_interval = net_change_by_interval[['start station id', 'start_time_rounded','end station id', 'end_time_rounded', 'net_change']]

# Merge net change by interval with station capacity data
station_data = pd.merge(net_change_by_interval, station_capacity, left_on='end station id', right_on='ID')

# Calculate available bikes at each station for each time
station_data['available_bikes'] = station_data.groupby('end station id')['net_change'].cumsum()

# Calculate depletion status
station_data['depletion_status'] = station_data['available_bikes'] / station_data['CAPACITY']


# Save results to CSV
station_data.to_csv(r"C:\Users\Patrick\Downloads\stockout_risk5.csv", index=False)



# Plotting
# plt.figure(figsize=(10, 6))
# plt.plot(net_change_by_interval['end_time_rounded'], net_change_by_interval['net_change'], label='Net Change')
#plt.plot(net_change_by_interval['time_rounded'], net_change_by_interval['start_count'], label='Start Counts')
#plt.plot(net_change_by_interval['end_time_rounded'], net_change_by_interval['end_count'], label='End Counts')
#plt.xlabel('Time Interval')
#plt.ylabel('Net Change in Bikes')
#plt.title('Net Change of Bikes Over Time')
#plt.legend()
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()
