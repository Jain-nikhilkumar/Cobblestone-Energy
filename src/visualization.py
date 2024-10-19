# src/visualization.py
import matplotlib.pyplot as plt

def c(df, anomalies):
    """Plots the data stream and marks the detected anomalies."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df['value'], label='Data Stream')
    plt.scatter(df['time'].iloc[anomalies], df['value'].iloc[anomalies], color='red', label='Anomalies', marker='x')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Data Stream with Anomalies')
    plt.legend()
    plt.show()
