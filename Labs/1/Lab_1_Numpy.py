import numpy as np
import time

# Define the matrices
A1 = np.array([[2, -3, 3], [-2, 6, 5], [4, 7, 8]])
B1 = np.array([[-1, 9, 1], [0, 6, 5], [3, 4, 7]])

A2 = np.array([[2, -3, 3, 0], [-2, 6, 5, 1], [4, 7, 8, 2]])
B2 = np.array([[-1, 9, 1], [0, 6, 5], [3, 4, 7]])

A3 = np.array([[2, -3, 3, 5], [-2, 6, 5, -2]])
B3 = np.array([[-1, 9, 1], [0, 6, 5], [3, 4, 7], [1, 2, 3]])

# Time the multiplication for Test 1
start = time.time()
C1 = np.dot(A1, B1)
end = time.time()

print("Test 1 (NumPy):")
print(C1)
print(f"Time taken: {end - start:.6f} seconds")

# Time the multiplication for Test 3
start = time.time()
C3 = np.dot(A3, B3)
end = time.time()

print("\nTest 3 (NumPy):")
print(C3)
print(f"Time taken: {end - start:.6f} seconds")