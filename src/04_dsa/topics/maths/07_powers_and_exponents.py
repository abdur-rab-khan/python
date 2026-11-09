"""
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 POWERS AND EXPONENTS                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                   |
| 🟡 Power mean how many times a number multiply by itself.                                                                                         |
|                                                                                                                                                   |
| 🔶 Example:                                                                                                                                       |
|                                                                                                                                                   |
|    => 2³  MEANS 2 x 2 x 2 = 8                                                                                                                     |
|                                                                                                                                                   |
|    2 ==> BASE                                                                                                                                     |
|    3 ==> EXPONENTS                                                                                                                                |
|                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# Brute force to find power and exponents

# Optimized solution

def power(base, exponent):
    if exponent < 0:
        return 1 / power(base, -exponent)
    result = 1
    while exponent:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result
