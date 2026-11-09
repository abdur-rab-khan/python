"""
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                       FACTORS                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                   |
| 🟡 Factor mean a number who completely divides without any remainder, example 2 is the factor of 4 because 2 divides 4 without any remainder      |
|                                                                                                                                                   |
| 🔶 Every number have at-least two factors:                                                                                                        |
|    🔸 By Itself                                                                                                                                   |
|    🔸 By 1                                                                                                                                        |
|                                                                                                                                                   |
| ⭐ KEY TAKEAWAY                                                                                                                                   |
|                                                                                                                                                   |
|    🔸 If 2 is the factor of 6, mean 100% (6 / 2 = 3) is also be a factor of 6                                                                     |
|                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# Brute force -- method

# 1 will be the factor of all number.

# If number is equal to n.

# If it's completely divisible by n -- it's factor.

# Looping through all founded factors

# Using square root method

# If n is competently divisible by i -- it's a factor and n / i will also

# be a factor.

# Looping through all founded factors

# Calling all factors

# Using brute force method

# Using efficient method

# namespace factor

# Calling factor

def factors(number):
    if number <= 0:
        return []
    result = []
    for value in range(1, int(number ** 0.5) + 1):
        if number % value == 0:
            result.append(value)
            if value != number // value:
                result.append(number // value)
    return sorted(result)
