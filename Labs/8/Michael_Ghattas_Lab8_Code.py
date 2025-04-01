##
# Michael Ghattas
# COMP 4581 - Lab 8
# Mar/3/2025
##



def printMatrix(m):
    """Helper function to print matrices in a readable format"""
    for row in m:
        print(row)
    print()

def chainMatrix(dims):
    """Computes the optimal matrix multiplication order using DP.

    Args:
        dims (list): List of matrix dimensions.
    
    Returns:
        tuple: (minimum cost, optimal parenthesization string)
    """
    n = len(dims) - 1  # Number of matrices
    m = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
    s = [[None for _ in range(n)] for _ in range(n)]  # Table to store split points

    # Fill the DP table
    for chain_length in range(2, n + 1):  # Chain length increases
        for i in range(n + 1 - chain_length):
            j = i + chain_length - 1
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k  # Store the best split point

    print("Optimal Cost Matrix:")
    printMatrix(m)

    print("Traceback Table:")
    printMatrix(s)

    # Generate the optimal parenthesization
    optimal_parens = parenStr(s, 0, n - 1)
    
    return m[0][n - 1], optimal_parens

def parenStr(s, i, j):
    """Recursive function to generate the optimal parenthesization.

    Args:
        s (list): The traceback table storing split indices.
        i (int): Start index of the matrix chain.
        j (int): End index of the matrix chain.

    Returns:
        str: Parenthesized string representation.
    """
    if i == j:
        return f"A{i}"
    else:
        k = s[i][j]
        left = parenStr(s, i, k)
        right = parenStr(s, k + 1, j)
        return f"({left}{right})"

# Example input
dims = [30, 35, 15, 5, 10, 20, 25]
optimal_cost, optimal_parenthesization = chainMatrix(dims)

print(f"Optimal multiplication cost: {optimal_cost}")
print(f"Optimal parenthesization: {optimal_parenthesization}")



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##