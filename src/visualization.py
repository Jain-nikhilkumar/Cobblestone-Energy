import matplotlib.pyplot as plt

def plot_anomalies(data_df):
    """Plot the synthetic data and detected anomalies."""
    anomalies = data_df[data_df['anomaly'] == -1]
    
    plt.figure(figsize=(15, 7))
    plt.plot(data_df['Time'], data_df['Value'], label='Synthetic Data')
    plt.scatter(anomalies['Time'], anomalies['Value'], color='red', label='Detected Anomalies', s=10)
    plt.title('Anomaly Detection on Synthetic Data')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
