"""
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                     PRIME NUMBERS                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                   |
| 🟡 Prime number is a number, who only divide by "1" or "itself", a number can't be a prime if they have more than "two" factors.                  |
|                                                                                                                                                   |
| 🔶 Example:                                                                                                                                       |
|           🔸 2, 3, 5, 7, 11 (PRIME NUMBERS)                                                                                                       |
|           🔸 1, 2, 4, 6, ... (NON PRIME NUMBERS)                                                                                                  |
|                                                                                                                                                   |
| 🔷 Key Takeaway                                                                                                                                   |
|                                                                                                                                                   |
|    🔹All the multiples of a prime number will be non-prime numbers, So 2 is prime all the multiple e.g 4, 6, 8, 16 these will not be a prime.     |
|                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# 🟡 Sieve of Eratosthenes

# Number smaller than 1 will not a prime number.

# If it's divisible by any number it can't be a prime

def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def sieve(limit):
    if limit < 2:
        return []
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for value in range(2, int(limit ** 0.5) + 1):
        if prime[value]:
            for multiple in range(value * value, limit + 1, value):
                prime[multiple] = False
    return [i for i, flag in enumerate(prime) if flag]
