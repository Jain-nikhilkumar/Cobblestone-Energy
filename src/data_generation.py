import numpy as np
import pandas as pd
import random

# Function to generate large synthetic data
def generate_large_synthetic_data(num_points=100000, anomaly_probability=0.01, noise_level=0.1):
    time = np.arange(0, num_points)
    data_stream = np.sin(0.02 * time) + noise_level * np.random.randn(num_points)
    for i in range(num_points):
        if random.random() < anomaly_probability:
            data_stream[i] += np.random.normal(5, 2)
    return time, data_stream

# Function to save the data to a CSV file
def save_data_to_csv(time, data_stream, filename='large_synthetic_data_stream.csv'):
    # Create a DataFrame
    data_df = pd.DataFrame({'Time': time, 'Value': data_stream})
    
    # Save the DataFrame to a CSV file
    data_df.to_csv(filename, index=False)
    print(f"Synthetic data with {len(data_stream)} points has been saved to '{filename}'.")
