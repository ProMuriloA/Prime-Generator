import numpy as np
import math

sieve_marker = int(input('Enter the upper limit: '))


def ultra_fast_sieve(n):
    """Optimized sieve for numbers up to 10^7 using numpy"""
    if n < 2:
        return []
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0:2] = False
    sieve[4::2] = False
    sieve[9::3] = False
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if sieve[i]:
            sieve[i * i::i] = False
        if sieve[i + 2]:
            sieve[(i + 2) * (i + 2)::i + 2] = False
    return np.nonzero(sieve)[0].tolist()


def segmented_sieve(n):
    """Segmented sieve for numbers above 10^7"""
    if n < 2:
        return []

    # Calculate base primes up to sqrt(n)
    base_primes = ultra_fast_sieve(math.isqrt(n))
    primes = base_primes.copy()

    segment_size = 2 ** 18  # Optimal for modern CPU cache (256KB)
    low = max(2, base_primes[-1] + 1) if base_primes else 2

    while low <= n:
        high = min(low + segment_size, n)
        sieve = np.ones(high - low + 1, dtype=bool)

        for p in base_primes:
            start = max(p * p, ((low + p - 1) // p) * p)
            sieve[start - low::p] = False

        # Add new primes found in this segment
        primes.extend(np.nonzero(sieve)[0] + low)
        low = high + 1

    return primes


# Choose the appropriate sieve based on input size
if sieve_marker <= 10 ** 7:  # ~1MB memory usage
    primes = ultra_fast_sieve(sieve_marker)
else:
    primes = segmented_sieve(sieve_marker)

print(f"Found {len(primes)} primes up to {sieve_marker}")