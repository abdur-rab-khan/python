"""
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                            GCD or HCF (GREATEST COMMON DIVISOR)                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                   |
| 🟡 GCD (Greatest Common Divisor), it's the biggest number that divides both number without any remainders.                                        |
|                                                                                                                                                   |
|      🔹 Factor of 12 ("a") -> 1, 2, 3, 4, [6], 12                                                                                                 |
|      🔹 Factor of 18 ("b") -> 1, 2, 3, [6], 9, 18                                                                                                 |
|                                                                                                                                                   |
| 🔶 Euclidean Algorithm gcd(b, a % b)                                                                                                              |
|      🔸 It's the algorithm that provides efficient way to find the "gcd"                                                                          |
|                                                                                                                                                   |
| 🟡 Euclidean algorithm finds GCD by repeating a % b until the remainder becomes 0. The last non-zero value of b is the GCD.                       |
|                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                              LCM (LEAST COMMON MULTIPLE)                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                   |
| 🟡 LCM (Least Common Multiple), it's the smallest number that both number can divide them without getting any remainders.                         |
|                                                                                                                                                   |
|      🔹 Multiple of 4 ("a") -> 4, 18, [12], 16, 20 ....                                                                                           |
|      🔹 Multiple of 6 ("b") -> 6, [12], 18 ...                                                                                                    |
|                                                                                                                                                   |
| 👉 [12] is the LCM for (4, 6), because 12 is divide by 4 and 6 completely without giving any remainder                                            |
|                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# namespace gcd

# Formula is a * b = lcm(a, b) / gcd(a, b)

# lcm(a, b) = a * b / gcd(a, b);

# Or we can also write like this lcm(a, b) = (a / gcd(a, b)) * b;

# namespace lcm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return 0 if not a or not b else abs(a * b) // gcd(a, b)
