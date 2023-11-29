import matplotlib.pyplot as plt

# Data
n_values = [10000, 20000, 30000, 40000,
            50000, 60000, 70000, 80000, 90000, 100000]
empirical_rt = [0.69, 1.88, 1.82, 1.78, 3.36, 4.38, 6.26, 5.51, 8.47, 10.41]
predicted_rt = [0.97, 2.90, 2.66, 2.83, 6.15, 6.28, 7.87, 7.95, 16.36, 15.55]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, empirical_rt, label='EmpiricalRT (ms)', marker='o')
plt.plot(n_values, predicted_rt, label='PredictedRT', marker='o')

# Adding labels and title
plt.xlabel('n')
plt.ylabel('Running Time')
plt.title('Alg3 Running Time Comparison')
plt.legend()

# Show the plot
plt.show()
