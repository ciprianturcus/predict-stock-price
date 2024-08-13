import os
import pandas as pd
import random
from datetime import datetime, timedelta
import warnings
 
warnings.filterwarnings("ignore")
 
def get_random_data_points(file_path):
    # Reading the CSV file and assigning column names
    df = pd.read_csv(file_path, header=None, names=['Stock-ID', 'Timestamp', 'stock price'])
    # Convert the Timestamp to datetime format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d-%m-%Y')
    # Select 10 random consecutive data points
    start_index = random.randint(0, len(df) - 10)
    return df.iloc[start_index:start_index + 10]
 
def predict_next_values(data_points):
    prices = data_points['stock price'].values
    n = prices[-1]
    n1 = sorted(prices)[-2]  # Second highest value
    n2 = n1 + 0.5 * (n1 - n)
    n3 = n2 + 0.25 * (n2 - n1)
    return [n1, n2, n3]
 
def process_files(exchange_folder, num_files):
    files = os.listdir(exchange_folder)
    selected_files = files[:min(num_files, len(files))]
    for file in selected_files:
        file_path = os.path.join(exchange_folder, file)
        data_points = get_random_data_points(file_path)
        predictions = predict_next_values(data_points)
        last_timestamp = data_points.iloc[-1]['Timestamp']
        predicted_timestamps = [last_timestamp + timedelta(days=i) for i in range(1, 4)]
        stock_id = data_points.iloc[0]['Stock-ID']
        output_data = data_points[['Stock-ID', 'Timestamp', 'stock price']].copy()
        prediction_df = pd.DataFrame({
            'Stock-ID': [stock_id] * 3,
            'Timestamp': predicted_timestamps,
            'stock price': predictions
        })
        # Use pd.concat instead of append
        output_data = pd.concat([output_data, prediction_df], ignore_index=True)
        output_file = os.path.join(exchange_folder, f'predicted_{file}')
        output_data.to_csv(output_file, index=False)
 
def main(exchange_folders, num_files):
    for folder in exchange_folders:
        process_files(folder, num_files)
 
# Example usage:
exchange_folders = ['/home/cturcus/test/exchange1']  # Update path as needed
num_files = 2  # Change to 1 if only 1 file should be processed
main(exchange_folders, num_files)
