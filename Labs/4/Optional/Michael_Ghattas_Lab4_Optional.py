##
# Michael Ghattas
# COMP 4581 - Lab 4
# Feb/03/2025
##



import math
import random


def arc_distance(p1, p2, circle_size = 360):
    """
    Computes the shortest arc distance between two points on a circle.
    
    Parameters:
    p1 (int or float): First point on the circle (in degrees).
    p2 (int or float): Second point on the circle (in degrees).
    circle_size (int): Full circle size (default 360 degrees).

    Returns:
    float: Shortest arc distance between p1 and p2.
    """

    diff = abs(p1 - p2)

    return min(diff, circle_size - diff)


def closest_pair_circle(points, circle_size = 360):
    """
    Finds the closest pair distance on a circle using modular arithmetic.

    Parameters:
    points (list): List of points (angles in degrees).
    circle_size (int): The full size of the circle (default 360 degrees).

    Returns:
    float: The shortest arc distance between the closest pair.
    """

    # Sort points in increasing order for easier comparisons
    points.sort()

    # Compute distances between consecutive points
    min_distance = math.inf
    for i in range(len(points)):
        d = arc_distance(points[i], points[(i + 1) % len(points)], circle_size)
        min_distance = min(min_distance, d)

    return min_distance


def main():
    """
    Main function to run the closest pair distance on a circle.
    """

    test_cases = [
        [7, 4, 12, 14, 2, 10, 16, 6],
        [7, 4, 12, 14, 2, 10, 16, 5],
        [14, 8, 2, 6, 3, 10, 12]
    ] 

    for i, test in enumerate(test_cases, 1):
        result = closest_pair_circle(test)
        print(f"Test Case {i}: Closest Pair Arc Distance = {result:.2f}")


if __name__ == "__main__":
    main()



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##