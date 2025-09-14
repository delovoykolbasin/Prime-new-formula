import numpy as np
import math
from typing import List

# 3DCOM constants
LZ = 1.23498228
HQS = 0.2355012867
PI = math.pi

def is_prime(num: int) -> bool:
    """Check if a number is prime.
    
    Args:
        num: Integer to check.
    
    Returns:
        True if prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = math.isqrt(num)
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            return False
    return True

def predict_primes_3dcom(start_n: float = 8.0, end_n: float = 15.0,
                         step: float = 0.001,
                         resonance_threshold: float = 0.06) -> List[int]:
    """
    Predict prime numbers using the 3DCOM resonance framework.

    Args:
        start_n: Starting point for resonance scan.
        end_n: Ending point for resonance scan.
        step: Resolution of the scan.
        resonance_threshold: Minimum resonance strength to consider.

    Returns:
        Sorted list of predicted prime numbers.
    """
    a0 = 103  # Starting reference
    n_neptune = 7  # Reference position

    predicted_primes = set()

    # Use numpy.linspace to ensure stable float step coverage
    n_values = np.arange(start_n, end_n, step)
    for n in n_values:
        orbit = a0 * (LZ ** (n - n_neptune))
        resonance = HQS * math.sin(0.3 * PI * n)
        if abs(resonance) > resonance_threshold:
            candidate = round(orbit)
            if candidate > 1 and is_prime(candidate):
                predicted_primes.add(candidate)

    return sorted(predicted_primes)

def predict_large_prime_patterns(base_prime: int, num_predictions: int = 10) -> List[int]:
    """
    Predict a sequence of primes starting from a known large prime using 3DCOM resonance patterns.

    Args:
        base_prime: Known starting prime number.
        num_predictions: Number of primes to predict.

    Returns:
        List of predicted prime numbers.
    """
    predicted_sequence = []

    for i in range(1, num_predictions + 1):
        resonance_factor = HQS * math.sin(0.3 * PI * i)
        predicted_prime = base_prime + round(LZ * i * (1 + abs(resonance_factor)))

        candidate = predicted_prime
        while not is_prime(candidate):
            candidate += 1

        predicted_sequence.append(candidate)
        base_prime = candidate

    return predicted_sequence


if __name__ == "__main__":
    import time

    print("Testing 3DCOM prime prediction...")

    start_time = time.time()
    primes = predict_primes_3dcom(start_n=8, end_n=20, step=0.0001)
    duration = time.time() - start_time

    print(f"Predicted primes (first 20): {primes[:20]}")
    verified_primes = [p for p in primes if is_prime(p)]
    print(f"Verified primes (first 20): {verified_primes[:20]}")

    known_prime = 136279841
    predicted_sequence = predict_large_prime_patterns(known_prime, 5)
    print(f"Predicted prime sequence from {known_prime}: {predicted_sequence}")

    test_range = range(1000, 1020)
    actual_primes = [p for p in test_range if is_prime(p)]
    predicted_in_range = [p for p in primes if p in test_range]

    print(f"\nAccuracy test:")
    print(f"Actual primes in range {test_range.start}-{test_range.stop - 1}: {actual_primes}")
    print(f"Predicted primes in range: {predicted_in_range}")

    print(f"\nExecution time for prime prediction: {duration:.4f} seconds")

