##
# Michael Ghattas
# COMP 4581 - Lab 2
# Jan/21/2025
##


import random
from time import time
import pandas as pd
import matplotlib.pyplot as plt


# Define sorting algorithms

def mergeSort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i =  j =  0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=  1
        else:
            result.append(right[j])
            j +=  1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertionSort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i - 1
        while j >=  0 and key < L[j]:
            L[j + 1]  =  L[j]
            j -=  1
        L[j + 1] = key
    return L

def bubbleSort(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L

# Perform timing tests
def timing_test():
    results = []
    for n in range(100, 5100, 100):
        A  =  [i for i in range(n)]
        random.shuffle(A)

        # Timing mergeSort
        t1 = time()
        mergeSort(A[:])  # Use a copy of A to avoid mutation
        t2 = time()
        merge_time = (t2 - t1) * 1000

        # Timing insertionSort
        t1 = time()
        insertionSort(A[:])  # Use a copy of A to avoid mutation
        t2 = time()
        insert_time = (t2 - t1) * 1000

        # Timing bubbleSort
        t1 = time()
        bubbleSort(A[:])  # Use a copy of A to avoid mutation
        t2 = time()
        bubble_time = (t2 - t1) * 1000

        results.append((n, round(merge_time, 2), round(insert_time, 2), round(bubble_time, 2)))

    return results

# Run the timing tests
timing_results = timing_test()

# Convert results to a DataFrame for display
df_results = pd.DataFrame(timing_results, columns = ["N", "Merge (ms)", "Insert (ms)", "Bubble (ms)"])

# Save results to a CSV file
df_results.to_csv("Michael_Ghattas_Lab2_Data.csv", index = False)
print("Results saved to sort_running_times_lab2.csv")

# Plotting the timing results without annotation
plt.figure(figsize = (12, 8))
plt.plot(df_results["N"], df_results["Merge (ms)"], label = "Merge Sort", marker = 'o', linestyle = '-', color = 'blue')
plt.plot(df_results["N"], df_results["Insert (ms)"], label = "Insertion Sort", marker = 's', linestyle = '--', color = 'green')
plt.plot(df_results["N"], df_results["Bubble (ms)"], label = "Bubble Sort", marker = '^', linestyle = '-.', color = 'red')

# Adding labels, title, legend, and grid
plt.title("Sorting Algorithm Running Times (Lab 2)", fontsize = 16)
plt.xlabel("Number of Elements (N)", fontsize = 14)
plt.ylabel("Time (ms)", fontsize = 14)
plt.legend(fontsize = 12, loc = 'upper left')
plt.grid(True, linestyle = '--', alpha = 0.7)

# Save the updated plot as a JPEG file without annotation
plt.savefig("Michael_Ghattas_Lab2_Plot.jpeg", format = "jpeg")
print("Updated plot saved to sort_running_times_plot_no_annotation.jpeg")


##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##