import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load the synthetic data
data_df = pd.read_csv('large_synthetic_data_stream.csv')

# Set the anomaly probability (this should match the value used in data generation)
anomaly_probability = 0.02

# Train Isolation Forest model
iso_forest = IsolationForest(contamination=anomaly_probability)
data_df['anomaly'] = iso_forest.fit_predict(data_df[['Value']])

# Save model results
data_df.to_csv('anomaly_detection_results.csv', index=False)
print("Anomaly detection results saved to 'anomaly_detection_results.csv'.")

# Plot the synthetic data and detected anomalies
anomalies = data_df[data_df['anomaly'] == -1]
plt.figure(figsize=(15, 7))
plt.plot(data_df['Time'], data_df['Value'], label='Synthetic Data')
plt.scatter(anomalies['Time'], anomalies['Value'], color='red', label='Detected Anomalies', s=10)
plt.title('Anomaly Detection on Synthetic Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
