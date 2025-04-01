##
# Michael Ghattas
# COMP 4581 - Lab 3
# Jan/27/2025
##


def sieve_of_eratosthenes(limit):
    """
    The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a given integer n.
    It works by iteratively marking the multiples of each prime starting from 2.
    
    This function finds all prime numbers up to the specified limit using the Sieve of Eratosthenes.

    Parameters:
        limit (int): The upper bound to find prime numbers.

    Returns:
        list: A list of prime numbers up to the given limit.
    """
    if limit < 2:
        return []

    # Initialize a boolean array where True indicates a number is prime
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False

    # Extract the prime numbers
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

# Example Usage
n = 100
print(f"Primes up to {n}: {sieve_of_eratosthenes(n)}")


##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##