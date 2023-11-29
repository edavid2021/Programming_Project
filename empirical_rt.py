import matplotlib.pyplot as plt

# Data
n_values = [10000, 20000, 30000, 40000,
            50000, 60000, 70000, 80000, 90000, 100000]
alg1_empirical_rt = [1087.16, 4342.79, 9718.87, 17455.38,
                     27138.01, 38996.45, 52767.96, 69090.38, 87302.45, 108332.12]
alg2_empirical_rt = [15.25, 31.89, 47.83, 64.83,
                     82.81, 99.71, 118.14, 136.33, 156.75, 174.48]
alg3_empirical_rt = [0.69, 1.88, 1.82, 1.78,
                     3.36, 4.38, 6.26, 5.51, 8.47, 10.41]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, alg1_empirical_rt, label='ALG1: EmpiricalRT', marker='o')
plt.plot(n_values, alg2_empirical_rt, label='ALG2: EmpiricalRT', marker='o')
plt.plot(n_values, alg3_empirical_rt, label='ALG3: EmpiricalRT', marker='o')

# Adding labels and title
plt.xlabel('n')
plt.ylabel('Empirical Running Time (ms)')
plt.title('Empirical Running Time Comparison')
plt.legend()

# Show the plot
plt.show()
