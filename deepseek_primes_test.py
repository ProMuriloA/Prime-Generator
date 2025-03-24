import numpy as np
import math

sieve_marker = int(input('Enter the upper limit so we can test if the number is a prime: '))


def ultra_fast_sieve(n):
    """Optimized sieve for numbers up to 10^7 using numpy"""
    if n < 2:
        return []
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0:2] = False
    sieve[4::2] = False  # Mark even numbers > 2 as non-prime
    sieve[9::3] = False  # Mark multiples of 3

    # Check numbers congruent to 1 and 5 mod 6
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if sieve[i]:
            sieve[i * i::i] = False
        if sieve[i + 2]:
            sieve[(i + 2) * (i + 2)::i + 2] = False
    return np.nonzero(sieve)[0].tolist()


def segmented_sieve(n):
    """Segmented sieve for large numbers"""
    if n < 2:
        return []

    sqrt_n = math.isqrt(n)
    base_primes = ultra_fast_sieve(sqrt_n)
    primes = base_primes.copy()

    segment_size = 2 ** 18  # 262,144 numbers per segment
    low = max(2, sqrt_n + 1)

    while low <= n:
        high = min(low + segment_size, n)
        sieve = np.ones(high - low + 1, dtype=bool)

        for p in base_primes:
            start = max(p * ((low + p - 1) // p), p * p)
            sieve[start - low::p] = False

        primes.extend((np.nonzero(sieve)[0] + low).tolist())
        low = high + 1

    return primes


# Select appropriate sieve based on input size
if sieve_marker <= 10 ** 7:
    primes = ultra_fast_sieve(sieve_marker)
else:
    primes = segmented_sieve(sieve_marker)

# Directly print all primes without truncation
print(f"Primes up to {sieve_marker}:")
print(primes)

# Check if the upper limit is a prime
if primes and primes[-1] == sieve_marker:
    print(f"The upper limit {sieve_marker} is a prime number.")
else:
    print(f"The upper limit {sieve_marker} is not a prime number.")