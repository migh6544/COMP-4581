##
# Michael Ghattas
# COMP 4581 - Lab 2
# Jan/21/2025
##


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Load data (assuming 'df_results' has already been created from the uploaded CSV)
import pandas as pd
df_results = pd.read_csv("Michael_Ghattas_Lab2_Data.csv")

# Define potential fitting functions
def linear(x, a, b):
    return a * x + b

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def logarithmic(x, a, b):
    return a * np.log(x) + b

def power(x, a, b):
    return a * x**b

# Extract X (N values) and Y (time for each algorithm)
x_data = df_results["N"]
merge_y = df_results["Merge (ms)"]
insert_y = df_results["Insert (ms)"]
bubble_y = df_results["Bubble (ms)"]

# Fit curves for each algorithm
merge_params, _ = curve_fit(linear, x_data, merge_y)
insert_params, _ = curve_fit(quadratic, x_data, insert_y)
bubble_params, _ = curve_fit(quadratic, x_data, bubble_y)

# Generate predictions for n=1,000,000
n_large = 1_000_000
merge_time_large = linear(n_large, *merge_params)
insert_time_large = quadratic(n_large, *insert_params)
bubble_time_large = quadratic(n_large, *bubble_params)

# Define formulas as strings for the legend with rounded coefficients and descriptions
merge_formula = f"T_merge(n) = {merge_params[0]:.2f} * n + {merge_params[1]:.2f} (Linear)"
insert_formula = f"T_insert(n) = {insert_params[0]:.2e} * n^2 + {insert_params[1]:.2f} * n + {insert_params[2]:.2f} (Quadratic)"
bubble_formula = f"T_bubble(n) = {bubble_params[0]:.2e} * n^2 + {bubble_params[1]:.2f} * n + {bubble_params[2]:.2f} (Quadratic)"

# Plot results and fits
plt.figure(figsize=(12, 8))
plt.scatter(x_data, merge_y, label="Merge Sort Data", color="blue")
plt.scatter(x_data, insert_y, label="Insertion Sort Data", color="green")
plt.scatter(x_data, bubble_y, label="Bubble Sort Data", color="red")

x_fit = np.linspace(min(x_data), max(x_data), 500)

plt.plot(x_fit, linear(x_fit, *merge_params), label=f"Merge Sort Fit: {merge_formula}", color="blue", linestyle="--")
plt.plot(x_fit, quadratic(x_fit, *insert_params), label=f"Insertion Sort Fit: {insert_formula}", color="green", linestyle="--")
plt.plot(x_fit, quadratic(x_fit, *bubble_params), label=f"Bubble Sort Fit: {bubble_formula}", color="red", linestyle="--")

# Plot annotations
plt.title("Sorting Algorithm Running Times with Best Fit Lines", fontsize=16)
plt.xlabel("Number of Elements (N)", fontsize=14)
plt.ylabel("Time (ms)", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

# Save plot with updated legend
plt.savefig("Michael_Ghattas_Lab2_Optional.jpeg", format="jpeg")
plt.show()

# Output predictions for n=1,000,000
print(f"Merge Sort Time for n=1,000,000: {merge_time_large:.2f} ms")
print(f"Insertion Sort Time for n=1,000,000: {insert_time_large:.2f} ms")
print(f"Bubble Sort Time for n=1,000,000: {bubble_time_large:.2f} ms")


##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##