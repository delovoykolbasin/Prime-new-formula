import numpy as np

LZ = 1.23498228
HQS = 0.235
PI = np.pi

def is_prime(num):
    if num <= 1 or not float(num).is_integer():
        return False
    num = int(num)
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def predict_planet_nine_prime_filter():
    a0 = 30.06
    n_neptune = 7
    predicted_orbits = []
    for n in np.arange(n_neptune + 1, 15, 0.001):
        orbit = a0 * (LZ ** (n - n_neptune))
        resonance = HQS * np.sin(0.3 * PI * n)
        if abs(resonance) > 0.06:
            # Check if rounded orbit is prime
            rounded_orbit = round(orbit, 0)
            if is_prime(rounded_orbit):
                predicted_orbits.append(rounded_orbit)
    return sorted(set(predicted_orbits))

planet_nine_primes = predict_planet_nine_prime_filter()
print(f"Predicted Planet Nine prime orbits: {planet_nine_primes}")

