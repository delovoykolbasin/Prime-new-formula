import numpy as np
"""
3DCOM UOFT
Author: Martin Doina 
"""

# 3DCOM constants
LZ = 1.23498228799485631
HQS = 0.2355012867
PI = 3.141592653589793 

def is_prime(num):
    if num <= 1 or not float(num).is_integer():
        return False
    num = int(num)
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def predict_prime_sequence(start_prime, num_predictions=10):
    """Predict prime sequence using last found prime as base"""
    primes_found = [start_prime]
    current_prime = start_prime
    n_neptune = 7
    
    for i in range(num_predictions):
        predicted_orbits = []
        
        # Use the last found prime as the base (a0)
        a0 = current_prime
        
        # Your exact scanning code
        for n in np.arange(n_neptune + 1, 15, 0.001):
            orbit = a0 * (LZ ** (n - n_neptune))
            resonance = HQS * np.sin(0.3 * PI * n)
            
            if abs(resonance) > 0.06:
                rounded_orbit = int(round(orbit, 0))
                if is_prime(rounded_orbit) and rounded_orbit > current_prime:
                    predicted_orbits.append(rounded_orbit)
        
        if predicted_orbits:
            # Find the next prime (smallest predicted prime)
            next_prime = min(predicted_orbits)
            primes_found.append(next_prime)
            current_prime = next_prime  # Set as base for next iteration
            print(f"Prediction {i+1}: Found prime {next_prime} (using base {a0})")
        else:
            print(f"Prediction {i+1}: No prime found (using base {a0})")
            break
    
    return primes_found

def predict_planet_nine_prime_filter():
    """Your original function - unchanged"""
    a0 = 103
    n_neptune = 7
    predicted_orbits = []
    for n in np.arange(n_neptune + 1, 15, 0.001):
        orbit = a0 * (LZ ** (n - n_neptune))
        resonance = HQS * np.sin(0.3 * PI * n)
        if abs(resonance) > 0.06:
            rounded_orbit = int(round(orbit, 0))
            if is_prime(rounded_orbit):
                predicted_orbits.append(rounded_orbit)
    return sorted(set(predicted_orbits))

# Run your original function first
planet_nine_primes = predict_planet_nine_prime_filter()
print(f"Predicted Planet Nine prime orbits: {planet_nine_primes}")

# Now use the largest found prime as starting point for recursive prediction
if planet_nine_primes:
    last_prime = planet_nine_primes[-1]  # Use the last prime found (557)
    print(f"\nStarting recursive prediction from last prime: {last_prime}")
    
    # Predict the next 10 primes using recursive base
    prime_sequence = predict_prime_sequence(last_prime, num_predictions=10)
    print(f"\nFinal prime sequence: {prime_sequence}")
else:
    print("No primes found to start recursive prediction")