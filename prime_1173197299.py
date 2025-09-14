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

def predict_prime_sequence():
    """Predict primes using 3DCOM recursive framework with last prime as base"""
    # Start from your initial prime
    current_prime = 136279841
    prime_sequence = [current_prime]
    n_neptune = 7
    
    for i in range(10):  # Predict 10 primes
        predicted_orbits = []
        
        # Use the last found prime as the base (a0)
        a0 = current_prime
        
        # Your exact scanning code
        for n in np.arange(n_neptune + 1, 15, 0.001):
            orbit = a0 * (LZ ** (n - n_neptune))  # Continue the recursive sequence
            resonance = HQS * np.sin(0.3 * PI * n)  # resonance pattern
            
            # Strong resonance points are where prime can exist
            if abs(resonance) > 0.06:  # Tuned for prime system
                rounded_orbit = round(orbit, 0)
                if is_prime(rounded_orbit) and rounded_orbit > current_prime:
                    predicted_orbits.append(rounded_orbit)
        
        # Find the next prime (smallest predicted prime greater than current)
        if predicted_orbits:
            next_prime = min(predicted_orbits)
            prime_sequence.append(int(next_prime))
            current_prime = int(next_prime)  # Set as base for next iteration
            print(f"Predicted prime {i+1}: {current_prime}")
        else:
            print(f"No prime found in iteration {i+1}")
            break
    
    return prime_sequence

# Run the prediction
print("Starting prime sequence prediction...")
primes = predict_prime_sequence()
print(f"Final prime sequence: {primes}")