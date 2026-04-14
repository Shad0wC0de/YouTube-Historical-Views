import pandas as pd
import os
from datetime import timedelta

# Folder containing your CSV files
input_folder = "/Users/lancelotdatuin/Documents/GitHub/YouTube-Historical-Views/source_data"
output_folder = "/Users/lancelotdatuin/Documents/GitHub/YouTube-Historical-Views/new_data"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all CSV files
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)

        # Read CSV
        df = pd.read_csv(file_path)

        # Convert Timestamp to datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        # 1. Hours (round UP to next hour)
        df['Hours'] = df['Timestamp'].dt.ceil('h')

        # 2. Date
        df['Date'] = df['Timestamp'].dt.date

        # 3. Day (day of week)
        df['Day'] = df['Timestamp'].dt.day_name()

        # 4. Month (first day of month)
        df['Month'] = df['Timestamp'].values.astype('datetime64[M]')

        # Reorder columns
        df = df[['Timestamp', 'Hours', 'Date', 'Day', 'Month', 'Title', 'URL', 'Views']]

        # Save to new file
        output_file = os.path.join(output_folder, f"updated_{filename}")
        df.to_csv(output_file, index=False)

        print(f"Processed: {filename} -> {output_file}")