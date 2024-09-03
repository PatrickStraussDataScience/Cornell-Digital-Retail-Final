import pandas as pd

# Read the data into a DataFrame
df = pd.read_csv(r"C:\Users\Patrick\Downloads\BIKEDATASET3.csv")  # Replace 'your_data.csv' with the path to your CSV file

# Convert 'starttime' column to datetime objects
df['starttime'] = pd.to_datetime(df['starttime'])

# Filter the data to only include the time period from June 1st, 2019, to August 31st, 2019
start_date = pd.Timestamp(2019, 6, 1)
end_date = pd.Timestamp(2019, 8, 31)
filtered_data = df[(df['starttime'] >= start_date) & (df['starttime'] <= end_date)]

# Convert 'starttime' and 'stoptime' columns to datetime objects
filtered_data['starttime'] = pd.to_datetime(filtered_data['starttime'])
filtered_data['stoptime'] = pd.to_datetime(filtered_data['stoptime'])

# Group the data by day and calculate inflow, outflow, and net demand for each day
filtered_data['date'] = filtered_data['starttime'].dt.date
daily_data = filtered_data.groupby('date').agg({
    'end station id': lambda x: (x == 67).sum(),  # Count of trips ending at station id 67 as inflow
    'start station id': lambda x: (x == 67).sum(),  # Count of trips starting from station id 67 as outflow
}).rename(columns={'end station id': 'inflow', 'start station id': 'outflow'})
daily_data['net_demand'] = daily_data['inflow'] - daily_data['outflow']

# Calculate mean and standard deviation of inflow, outflow, and net demand per day
mean_inflow = daily_data['inflow'].mean()
std_inflow = daily_data['inflow'].std()
mean_outflow = daily_data['outflow'].mean()
std_outflow = daily_data['outflow'].std()
mean_net_demand = daily_data['net_demand'].mean()
std_net_demand = daily_data['net_demand'].std()

print("Mean Inflow per day:", mean_inflow)
print("Standard Deviation of Inflow per day:", std_inflow)
print("Mean Outflow per day:", mean_outflow)
print("Standard Deviation of Outflow per day:", std_outflow)
print("Mean Net Demand per day:", mean_net_demand)
print("Standard Deviation of Net Demand per day:", std_net_demand)
