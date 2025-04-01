def printMatrix(m):
    """Helper function to print a matrix in a formatted way."""
    for row in m:
        print(row)

def matrixMult(A, B):
    """Performs matrix multiplication of A and B."""
    # Get dimensions of matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        print("Matrix multiplication not possible. Dimensions do not match.")
        return None

    # Initialize result matrix with dimensions rows_A x cols_B
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B since cols_A == rows_B
                C[i][j] += A[i][k] * B[k][j]

    return C

# Testing code

# Test 1: Square 3x3 matrices
print("Test 1:")
A = [[2, -3, 3], [-2, 6, 5], [4, 7, 8]]
B = [[-1, 9, 1], [0, 6, 5], [3, 4, 7]]
C = matrixMult(A, B)
if C is not None:
    printMatrix(C)

# Test 2: Incompatible dimensions
print("\nTest 2:")
A = [[2, -3, 3, 0], [-2, 6, 5, 1], [4, 7, 8, 2]]
B = [[-1, 9, 1], [0, 6, 5], [3, 4, 7]]
C = matrixMult(A, B)
if C is not None:
    printMatrix(C)

# Test 3: Non-square matrices
print("\nTest 3:")
A = [[2, -3, 3, 5], [-2, 6, 5, -2]]
B = [[-1, 9, 1], [0, 6, 5], [3, 4, 7], [1, 2, 3]]
C = matrixMult(A, B)
if C is not None:
    printMatrix(C)
