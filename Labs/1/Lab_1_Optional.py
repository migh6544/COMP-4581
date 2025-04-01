import numpy as np
import time
import random

def generate_matrix(n):
    return [[random.randint(0, 10) for _ in range(n)] for _ in range(n)]

def manual_matrix_mult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return None

    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Test with increasing matrix sizes
for n in [100, 200, 300, 400, 500]:
    A = generate_matrix(n)
    B = generate_matrix(n)
    A_np = np.array(A)
    B_np = np.array(B)

    # Time manual implementation
    start = time.time()
    manual_matrix_mult(A, B)
    end = time.time()
    manual_time = end - start

    # Time NumPy implementation
    start = time.time()
    np.dot(A_np, B_np)
    end = time.time()
    numpy_time = end - start

    print(f"n={n}: Manual Time = {manual_time:.6f} s, NumPy Time = {numpy_time:.6f} s")
