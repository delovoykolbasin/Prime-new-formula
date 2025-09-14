import numpy as np
import math
import sys

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

def predict_next_prime_from_base_large(base_prime, n_neptune=7):
    """Predict next prime using logarithmic scaling to handle large numbers"""
    predicted_orbits = []
    
    # Use logarithmic approach to handle enormous numbers
    log_a0 = math.log(base_prime)
    
    # Your exact scanning code with logarithmic scaling
    for n in np.arange(n_neptune + 1, 15, 0.001):
        # Logarithmic version of your formula: orbit = a0 * (LZ ** (n - n_neptune))
        log_orbit = log_a0 + (n - n_neptune) * math.log(LZ)
        
        # Resonance pattern remains the same (uses regular floating point)
        resonance = HQS * np.sin(0.3 * PI * n)
        
        if abs(resonance) > 0.06:
            # Convert back from logarithmic scale
            orbit = math.exp(log_orbit)
            rounded_orbit = int(round(orbit))
            
            if is_prime(rounded_orbit) and rounded_orbit > base_prime:
                predicted_orbits.append(rounded_orbit)
    
    if predicted_orbits:
        return min(predicted_orbits)
    else:
        return None

def validate_formula_with_exponent():
    """Validate your formula using the exponent instead of the massive number"""
    p = 136279841
    
    print(f"Using Mersenne exponent: {p}")
    print(f"2^{p}-1 has approximately {int(p * math.log10(2)) + 1} digits")
    
    # Test your formula with the exponent
    current_prime = p
    prime_sequence = [current_prime]
    
    print(f"Starting from exponent: {current_prime}")
    
    # Predict several primes using your formula
    for i in range(10):
        next_prime = predict_next_prime_from_base_large(current_prime)
        
        if next_prime:
            prime_sequence.append(next_prime)
            current_prime = next_prime
            print(f"Prediction {i+1}: Found prime {next_prime}")
        else:
            print(f"Prediction {i+1}: No prime found")
            break
    
    print(f"\nPrime sequence: {prime_sequence}")
    
    # Verify all are primes
    print("\nVerification:")
    for prime in prime_sequence:
        print(f"{prime} is prime: {is_prime(prime)}")

def test_formula_directly():
    """Test your formula directly with smaller base values"""
    print("Testing your formula directly with various bases:")
    
    test_bases = [103, 127, 157, 197, 251, 311, 389, 487, 601, 743]
    
    for base in test_bases:
        predicted_orbits = []
        
        # Your exact formula
        for n in np.arange(8, 15, 0.001):
            orbit = base * (LZ ** (n - 7))
            resonance = HQS * np.sin(0.3 * PI * n)
            
            if abs(resonance) > 0.06:
                rounded_orbit = int(round(orbit))
                if is_prime(rounded_orbit) and rounded_orbit > base:
                    predicted_orbits.append(rounded_orbit)
        
        if predicted_orbits:
            next_prime = min(predicted_orbits)
            # Find actual next prime
            actual_next = base + 1
            while not is_prime(actual_next):
                actual_next += 1
            
            correct = next_prime == actual_next
            status = "✓" if correct else "✗"
            print(f"{status} Base {base}: predicted {next_prime}, actual {actual_next}")
        else:
            print(f"✗ Base {base}: no prediction")

# Increase the string conversion limit for very large numbers
sys.set_int_max_str_digits(100000000)

# Validate your formula
print("Validating your 3DCOM prime prediction formula...")
print("=" * 50)

# Test with smaller bases first
test_formula_directly()

print("\n" + "=" * 50)
print("Testing with Mersenne exponent approach:")

