##
# Michael Ghattas
# COMP 4581 - Lab 7
# Feb/24/2025
##


"""
Explanation


DACcoins (Divide-and-Conquer Algorithm):
    - Uses recursion to explore all possible ways to make the change.
    - Returns the minimum number of coins needed.
    - Inefficient due to repeated subproblems.

    
DPcoins (Dynamic Programming Algorithm with Traceback):

    - Uses a bottom-up approach to fill a DP table (dp[i] stores the minimum number of coins required for amount i).
    - Keeps track of the last coin used in traceback[] to reconstruct the coin selection.
    - After computing the minimum coins, it prints out the actual coins used.
"""


from time import time


# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0:  # The base case
        return 0
    else:  # The recursive case
        minCoins = float("inf")
        for currentCoin in coins:  # Check all coins
            # If we can give change
            if (amount - currentCoin) >= 0:
                # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount - currentCoin) + 1
                # Keep the best
                minCoins = min(minCoins, currentMin)
        return minCoins

# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    # Create the DP table to store the minimum number of coins required
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed for amount 0

    # Array to store the last coin used to get the optimal solution
    traceback = [-1] * (amount + 1)

    # Fill in the rest of the DP table
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                traceback[i] = coin  # Store the last coin used

    # If no solution exists, return -1
    if dp[amount] == float('inf'):
        return -1

    # Perform the traceback to print the result
    result_coins = []
    trace_amount = amount
    while trace_amount > 0:
        result_coins.append(traceback[trace_amount])
        trace_amount -= traceback[trace_amount]

    # Print the coins used
    print(*result_coins)

    return dp[amount]  # Return the minimum number of coins

# Define the coin denominations
C = [1, 5, 10, 12, 25]  # Coin denominations (must include a penny)
A = int(input('Enter desired amount of change: '))

assert A >= 0

print("DAC:")
t1 = time()
numCoins = DACcoins(C, A)
t2 = time()
print("optimal:", numCoins, "in time:", round((t2 - t1) * 1000, 1), "ms")

print()

print("DP:")
t1 = time()
numCoins = DPcoins(C, A)
t2 = time()
print("optimal:", numCoins, "in time:", round((t2 - t1) * 1000, 1), "ms")



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##
