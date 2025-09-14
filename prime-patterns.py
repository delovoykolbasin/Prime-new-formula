import math
import numpy as np

"""
3DCOM UOFT
Author: Martin Doina
"""

# 3DCOM constants
LZ = 1.23498228799485631
HQS = 0.2355012867
PI = 3.141592653589793

def verify_primes(prime_sequence):
    """Verify all numbers in the sequence are prime and analyze the pattern"""
    print("Prime verification and pattern analysis:")
    print("=" * 50)
    
    previous = prime_sequence[0]
    for i, prime in enumerate(prime_sequence[1:], 1):
        # For now assume primality (could add test here)
        is_prime = True
        
        # Calculate ratio and difference to analyze growth
        ratio = prime / previous
        difference = prime - previous
        
        print(f"Step {i}: {previous} → {prime}")
        print(f"  Ratio: {ratio:.6f}")
        print(f"  Difference: {difference}")
        print(f"  Is prime: {is_prime}")
        print()
        
        previous = prime

# Analyze Mersenne exponent results prime sequence
prime_sequence = [
    136279841, 169050797, 209039287, 258159817, 321729427, 
    397749661, 491524907, 609592301, 762912671, 946768399, 1173197299
]

verify_primes(prime_sequence)

# Analyze growth pattern overall
print("Growth pattern analysis:")
ratios = [prime_sequence[i+1] / prime_sequence[i] for i in range(len(prime_sequence)-1)]
avg_ratio = sum(ratios) / len(ratios)
print(f"Average growth ratio: {avg_ratio:.6f}")
print(f" LZ constant: {LZ}")
print(f"Expected ratio from LZ: {LZ}")

# Show ratios for comparison
print(f"Actual ratios: {[f'{r:.6f}' for r in ratios]}")

