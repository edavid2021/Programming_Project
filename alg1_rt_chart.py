import matplotlib.pyplot as plt

# Data
n_values = [10000, 20000, 30000, 40000,
            50000, 60000, 70000, 80000, 90000, 100000]
empirical_rt = [1087.16, 4342.79, 9718.87, 17455.38, 27138.01,
                38996.45, 52767.96, 69090.38, 87302.45, 108332.12]
predicted_rt = [1158.09, 4436.27, 9904.61, 17915.17, 27350.21,
                39494.05, 53059.20, 69533.18, 87629.50, 108774.10]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, empirical_rt, label='EmpiricalRT (ms)', marker='o')
plt.plot(n_values, predicted_rt, label='PredictedRT', marker='o')

# Adding labels and title
plt.xlabel('n')
plt.ylabel('Running Time')
plt.title('Alg1 Running Time Comparison')
plt.legend()

# Show the plot
plt.show()
