import numpy as np
import math

# 3DCOM constants
LZ = 1.23498228799485631
HQS = 0.2355012867
PI = 3.141592653589793 

def is_prime(num):
    """Check if a number is prime"""
    if num <= 1 or not float(num).is_integer():
        return False
    num = int(num)
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def predict_next_prime_from_base(base_prime, n_neptune=7):
    """Predict the next prime using a given base prime and your exact formula"""
    predicted_orbits = []
    
    # Use the given base prime as a0
    a0 = base_prime
    
    # Your exact scanning code
    for n in np.arange(n_neptune + 1, 15, 0.001):
        orbit = a0 * (LZ ** (n - n_neptune))  # Your exact formula
        resonance = HQS * np.sin(0.3 * PI * n)  # Your exact resonance pattern
        
        if abs(resonance) > 0.06:  # Your exact threshold
            rounded_orbit = int(round(orbit))
            if is_prime(rounded_orbit) and rounded_orbit > base_prime:
                predicted_orbits.append(rounded_orbit)
    
    if predicted_orbits:
        return min(predicted_orbits)  # Return the smallest predicted prime
    else:
        return None

# Start from the Mersenne prime (2^136279841)-1
p = 136279841
mersenne_prime = pow(2, p) - 1
current_prime = mersenne_prime
prime_sequence = [current_prime]

print(f"Starting from Mersenne prime: 2^{p}-1")
print(f"Prime length: {len(str(current_prime))} digits")

# We can't work with such a large number directly in the formula due to overflow
# So we'll use the exponent as a proxy for the first prediction
print("Using exponent as proxy for first prediction due to numerical limitations...")

# Use the exponent for the first prediction
current_prime = p  # Use the exponent instead of the massive prime
prime_sequence = [current_prime]

print(f"Starting from exponent: {current_prime}")

# Predict the next primes recursively using your exact formula
for i in range(20):  # Predict 20 more primes
    next_prime = predict_next_prime_from_base(current_prime)
    
    if next_prime:
        prime_sequence.append(next_prime)
        current_prime = next_prime
        print(f"Prediction {i+1}: Found prime {next_prime} (using base {prime_sequence[-2]})")
    else:
        print(f"Prediction {i+1}: No prime found using base {current_prime}")
        break

print(f"\nFinal prime sequence: {prime_sequence}")

# Verify the predictions are actual primes
print("\nVerification - all numbers are primes:")
for prime in prime_sequence:
    print(f"{prime} is prime: {is_prime(prime)}")