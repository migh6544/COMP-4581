##
# Michael Ghattas
# COMP 4581 - Lab 4
# Feb/03/2025
##



import math
import random


# Function to compute the absolute difference between two points (distance)
def distance(p1, p2):
    """
    Computes the absolute difference (distance) between two 1D points.

    Parameters:
    p1 (int): First point
    p2 (int): Second point

    Returns:
    int: Absolute difference |p1 - p2|
    """

    return abs(p1 - p2)


# Recursive function for closest pair distance
def recCPairDist(points):
    """
    Recursively finds the closest pair distance using Divide and Conquer.

    Parameters:
    points (list): A sorted list of 1D points (integers)

    Returns:
    int: Minimum distance between the closest pair of points
    """

    # Base Case: If only two points remain, return their distance
    if len(points) == 2:
        return distance(points[0], points[1])

    # Base Case: If only one point remains, return infinity (no valid pair)
    if len(points) < 2:
        return math.inf

    # Divide: Split the points into two halves
    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]

    # Conquer: Recursively find minimum distance in both halves
    left_min = recCPairDist(left_half)
    right_min = recCPairDist(right_half)

    # Combine: Find the smallest distance across the split boundary
    cross_min = distance(points[mid - 1], points[mid])

    # Return the smallest of the three distances
    return min(left_min, right_min, cross_min)


# Wrapper function: Sorts the input before calling recursive function
def cPairDist(points):
    """
    Finds the closest pair distance in a list of 1D points.

    Parameters:
    points (list): A list of 1D points (integers)

    Returns:
    int: Minimum distance between the closest pair of points
    """

    # Sort the points before applying the recursive function
    points.sort()

    return recCPairDist(points)


def run_tests():
    """
    Runs test cases on the closest pair distance function.
    """
    test_cases = [
        [7, 4, 12, 14, 2, 10, 16, 6],
        [7, 4, 12, 14, 2, 10, 16, 5],
        [14, 8, 2, 6, 3, 10, 12]
    ]

    for i, test in enumerate(test_cases, 1):
        result = cPairDist(test)
        print(f"Test Case {i}: Closest Pair Distance = {result}")


# Execute the script
def main():
    """
    Main function to execute the closest pair algorithm.
    """
    print("Running Closest Pair Distance Algorithm...\n")
    run_tests()


if __name__ == "__main__":
    main()



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##