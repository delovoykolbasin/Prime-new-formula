import time
import math
"""
3DCOM UOFT
Author: Martin Doina
"""

try:
    import gmpy2
    use_gmpy2 = True
except ImportError:
    use_gmpy2 = False
import gmpy2

LZ = gmpy2.mpfr('1.23498228799485631')
LZ_cubed = LZ ** 3   # use the ** operator

current_prime = gmpy2.mpz('7854626881233389')
next_prime = gmpy2.mpz(current_prime * LZ_cubed)


if use_gmpy2:
    print("Using gmpy2 for fast big integer calculations")
else:
    print("gmpy2 not found, using built-in int")

LZ = 1.23498228799485631
current_prime = 7854626881233389  # Starting large prime
max_digits = 1000  # How many digits to go up to
progress_interval = 10  # Display progress every 10 steps

step = 363000
while True:
    step += 1
    start_time = time.time()
    
    if use_gmpy2:
        current_prime = gmpy2.mpz(current_prime)
        next_prime = gmpy2.mpz(current_prime * LZ**3)
    else:
        next_prime = int(current_prime * LZ**3)
    
    digits = len(str(next_prime))
    runtime = time.time() - start_time
    
    if step % progress_interval == 0 or digits >= max_digits:
        print(f"Step {step}: digits={digits}, time={runtime:.6f}s")
    
    if digits >= max_digits:
        print(f"Reached max digit length {max_digits}, stopping.")
        break
    
    current_prime = next_prime

