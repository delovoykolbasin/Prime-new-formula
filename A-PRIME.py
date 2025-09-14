import numpy as np
"""
3DCOM UOFT
Author: Martin Doina 
"""

# 3DCOM constants
LZ = 1.23498228799485631
HQS = 0.2355012867
PI = 3.141592653589793 

def predict_prime():
    """Predict prime's using 3DCOM recursive framework"""
    # Start from 2^136279841−1 (keep exactly as is)
    a0 = 136279841; mersenne_prime = pow(2, a0) - 1

    # luke (keep exactly as is)
    n_prime = large_number = 10 ** 100000000

    n_neptune = 7  # Assuming this is needed for the formula
    
    # Calculate next prime (keep exactly as is)
    predicted_orbits = []
    for n in np.arange(n_prime + 1, 15, 0.001):  # Scan beyond prime
        orbit = a0 * (LZ ** (n - n_neptune))  # Continue the recursive sequence
        resonance = HQS * np.sin(0.3 * PI * n)  # resonance pattern
        
        # Strong resonance points are where prime can exist
        if abs(resonance) > 0.06:  # Tuned for prime system
            predicted_orbits.append(orbit)
    
    # Return integers only - this is the only change
    return sorted(set(int(round(orbit)) for orbit in predicted_orbits))

def is_prime(num):
    if num <= 1 or not float(num).is_integer():
        return False
    num = int(num)
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def predict_planet_nine_prime_filter():
    a0 = 136279841; mersenne_prime = pow(2, a0) - 1
    n_neptune = 7  # Keep exactly as is
    predicted_orbits = []
    for n in np.arange(n_neptune + 1, 15, 0.001):  # Keep exactly as is
        orbit = a0 * (LZ ** (n - n_neptune))  # Keep exactly as is
        resonance = HQS * np.sin(0.3 * PI * n)  # Keep exactly as is
        if abs(resonance) > 0.06:  # Keep exactly as is
            # Only change: convert to integer
            rounded_orbit = int(round(orbit))
            if is_prime(rounded_orbit):
                predicted_orbits.append(rounded_orbit)
    return sorted(set(predicted_orbits))

# Run predictions (keep exactly as is)
planet_nine_primes = predict_planet_nine_prime_filter()
print(f"Predicted Planet Nine prime orbits: {planet_nine_primes}")

# Predict! (keep exactly as is)
prime = predict_prime()
print(f"Predicted prime: {prime}")
