import time
import math
"""
3DCOM UOFT
Author: Martin Doina
"""

# Constants from  3DCOM model
LZ = 1.23498228799485631
HQS = 0.2355012867

# Starting prime from your list (largest known computed)
current_prime = 7854626881233389  # ~7.85e15, 16 digits

max_digits = 50  # Stop if predicted prime grows beyond this digit length
step_limit = 100  # Limit number of prediction steps to avoid infinite loop

print("Pushing Google Colab for large prime growth predictions...\n")

for step in range(1, step_limit+1):
    start_time = time.time()
    
    # Predict next prime by multiplying with LZ^3 to fit resonance model spacing
    next_prime = int(current_prime * LZ**3)
    digits = len(str(next_prime))
    runtime = time.time() - start_time
    
    print(f"Step {step}:")
    print(f"  Current prime: {current_prime}")
    print(f"  Predicted next prime: {next_prime}")
    print(f"  Digits: {digits}")
    print(f"  Computation time: {runtime:.6f} s\n")
    
    if digits > max_digits:
        print(f"Reached digit limit ({max_digits}), stopping prediction loop.")
        break
    
    current_prime = next_prime

print("Finished pushing Colab limits on prime growth predictions.")

