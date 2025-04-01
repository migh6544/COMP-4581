##
# Michael Ghattas
# COMP 4581 - Lab 3
# Jan/27/2025
##


import random
import time
import math
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

# Function to check if a number is prime
def isPrime(p):
    if p < 2:
        return False
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

# Function to generate a random n-bit prime number
def nBitPrime(n):
    while True:
        candidate = int(random.random() * (2 ** n))
        if candidate >= 2 and isPrime(candidate):
            return candidate

# Function to factorize PQ into its prime factors P and Q
def factor(pq):
    for i in range(2, int(math.sqrt(pq)) + 1):
        if pq % i == 0:
            return i, pq // i
    return None, None  # Should not happen if PQ is valid

# Timing the factorization process
def timeFactorization(bit_length):
    P = nBitPrime(bit_length)
    Q = nBitPrime(bit_length)
    PQ = P * Q

    start_time = time.time()
    factor(PQ)
    end_time = time.time()

    return (end_time - start_time) * 1000  # Time in milliseconds

# Collecting timing data
results = []
for bit_length in range(15, 21):  # Adjust the range based on runtime feasibility
    crack_time = timeFactorization(bit_length)
    results.append((bit_length, crack_time))
    print(f"Bit Length: {bit_length}, Time: {crack_time:.2f} ms")

# Save the results for analysis
df_results = pd.DataFrame(results, columns = ["Bit Length", "Cracking Time (ms)"])
df_results.to_csv("Michael_Ghattas_Lab3_Data.csv", index = False)

# Define exponential function
def exponential(x, a, b):
    return a * np.exp(b * x)

# Fit the collected data
bit_lengths = df_results["Bit Length"].values
cracking_times = df_results["Cracking Time (ms)"].values

params, _ = curve_fit(exponential, bit_lengths, cracking_times)
a, b = params

# Predict time for a 1024-bit key
bit_length_1024 = 1024
crack_time_1024_ms = exponential(bit_length_1024, a, b)
crack_time_1024_years = crack_time_1024_ms / 1000 / 60 / 60 / 24 / 365

# Plot the collected data and the fitted curve
x_fit = np.linspace(min(bit_lengths), max(bit_lengths), 500)
y_fit = exponential(x_fit, a, b)

plt.figure(figsize=(12, 8))
plt.scatter(bit_lengths, cracking_times, label = "Measured Data", color = "blue")
plt.plot(x_fit, y_fit, label = f"Exponential Fit: y = {a:.2e} * exp({b:.2e} * x)", color = "red")

plt.title("RSA Cracking Times vs. Bit Lengths", fontsize = 16)
plt.xlabel("Bit Length", fontsize = 14)
plt.ylabel("Cracking Time (ms)", fontsize = 14)
plt.legend(fontsize = 12)
plt.grid(True)
plt.savefig("Michael_Ghattas_Lab3_Plot.jpeg", format = "jpeg")
plt.show()

# Comments for 1024-bit estimation
print(f"Estimated Cracking Time for 1024-bit Key: {crack_time_1024_ms} ms")
print(f"Estimated Cracking Time for 1024-bit Key: {crack_time_1024_years} years")


##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##