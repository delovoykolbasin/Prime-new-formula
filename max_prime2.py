import gmpy2
import time

# Constants
LZ = gmpy2.mpfr('1.23498228799485631')
LZ_cubed = LZ ** 3
current_prime = gmpy2.mpz('7854626881233389')  # Starting number

max_digits = 100000000000       # Maximum digits limit
progress_interval = 50   # Steps between progress prints
step_limit = 50000000000       # Max iteration safety cap

print("Starting large prime growth prediction loop...")

for step in range(1, step_limit + 1):
    start_time = time.time()
    
    next_prime = gmpy2.mpz(gmpy2.mul(current_prime, LZ_cubed))
    digits = next_prime.num_digits(10)
    runtime = time.time() - start_time
    
    if step % progress_interval == 0:
        print(f"Step {step:5d}: digits={digits:5d}, time={runtime:.6f}s")
    
    if digits >= max_digits:
        print(f"Reached max digit length {max_digits} at step {step}, stopping.")
        break
    
    current_prime = next_prime

print("Completed large prime growth prediction.")

