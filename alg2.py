import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def alg2(arr, i):
    merge_sort(arr)
    return arr[i - 1]

def generate_random_array(n):
    return [random.randint(1, 1000) for _ in range(n)]

def measure_running_time(algorithm, arr, i):
    start_time = time.time()
    result = algorithm(arr.copy(), i)
    end_time = time.time()
    running_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, running_time

# Experiment parameters
input_sizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
iterations = 5
i_value = int(2 * len(input_sizes) / 3)

# Results table header
print("n\tTheoreticalRT\tEmpiricalRT (ms)\tRatio\tPredictedRT")

for n in input_sizes:
    theoretical_running_time = n * (n-1) / 2  # O(n log(n))

    # Run the algorithm multiple times and calculate average running time
    total_empirical_running_time = 0
    for _ in range(iterations):
        input_array = generate_random_array(n)
        _, empirical_running_time = measure_running_time(alg2, input_array, i_value)
        total_empirical_running_time += empirical_running_time

    average_empirical_running_time = total_empirical_running_time / iterations
    ratio = average_empirical_running_time / theoretical_running_time

    # Format the output for better readability
    print(f"{n}\t{theoretical_running_time:.2f}\t\t{average_empirical_running_time:.2f}\t\t{ratio:.8f}\t{ratio * theoretical_running_time:.2f}")
