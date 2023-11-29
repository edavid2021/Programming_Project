import matplotlib.pyplot as plt

# Data
n_values = [10000, 20000, 30000, 40000,
            50000, 60000, 70000, 80000, 90000, 100000]
empirical_rt = [15.25, 31.89, 47.83, 64.83,
                82.81, 99.71, 118.14, 136.33, 156.75, 174.48]
predicted_rt = [15.56, 34.13, 48.92, 66.15,
                84.98, 100.41, 118.76, 137.47, 158.71, 177.76]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, empirical_rt, label='EmpiricalRT (ms)', marker='o')
plt.plot(n_values, predicted_rt, label='PredictedRT', marker='o')

# Adding labels and title
plt.xlabel('n')
plt.ylabel('Running Time')
plt.title('Alg2 Running Time Comparison')
plt.legend()

# Show the plot
plt.show()
