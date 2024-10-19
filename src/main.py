from data_generation import *
from anomaly_detection import detect_anomalies, plot_results

def main():
    # Parameters for the dataset
    num_points = 100000
    anomaly_probability = 0.02
    noise_level = 0.2

    # Generate synthetic data
    time, data_stream = generate_large_synthetic_data(num_points=num_points, 
                                                      anomaly_probability=anomaly_probability, 
                                                      noise_level=noise_level)

    # Save data to CSV
    save_data_to_csv(time, data_stream)

    # Perform anomaly detection
    data_df = detect_anomalies()

    # Plot the results
    plot_results(data_df)

# Entry point of the script
if __name__ == '__main__':
    main()
