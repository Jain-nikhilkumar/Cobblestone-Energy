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

# Parameters for the dataset
num_points = 100000
anomaly_probability = 0.02
noise_level = 0.2

# Generate synthetic data
time, data_stream = generate_large_synthetic_data(num_points=num_points, anomaly_probability=anomaly_probability, noise_level=noise_level)

# Save data to a CSV file
data_df = pd.DataFrame({'Time': time, 'Value': data_stream})
data_df.to_csv('large_synthetic_data_stream.csv', index=False)

print(f"Synthetic data with {num_points} points has been saved to 'large_synthetic_data_stream.csv'.")
