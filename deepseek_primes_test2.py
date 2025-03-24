import secrets
import math

def is_prime(n, rounds=40):
    """Miller-Rabin primality test for cryptographic use."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    # Write n-1 as d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # Test for 'rounds' iterations
    for _ in range(rounds):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_rsa_prime(bit_length):
    """Generate a prime of specified bit length using Miller-Rabin."""
    while True:
        candidate = secrets.randbits(bit_length)
        # Ensure the number is odd and has the correct bit length
        candidate |= (1 << (bit_length - 1)) | 1
        if is_prime(candidate):
            return candidate

# User input for bit length (e.g., 1024, 2048)
bit_length = int(input("Enter the bit length for RSA primes (e.g., 1024): "))

# Generate two distinct primes
p = generate_rsa_prime(bit_length)
q = generate_rsa_prime(bit_length)
while p == q:
    q = generate_rsa_prime(bit_length)

# Verify primes
print(f"Generated primes (p, q):")
print(f"p = {p}\n\nq = {q}")
print(f"p is prime: {is_prime(p)}")
print(f"q is prime: {is_prime(q)}")