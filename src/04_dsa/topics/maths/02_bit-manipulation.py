"""
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 NUMBER SYSTEM                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                |
| 🟡 Numbers in Computer are presented by bits using "0" and "1", their are operators provided by programming languages called bit manipulation  |
|    to manipulate bits.                                                                                                                         |
|                                                                                                                                                |
| 🔶 How to Convert Decimal to Binary                                                                                                            |
|                                                                                                                                                |
|     🔸 Example for "10":                                                                                                                       |
|                   🔹 10 / 2 = 5, Remainder = 0                                                                                                 |
|                   🔹 5 / 2 = 2, Remainder = 1                                                                                                  |
|                   🔹 2 / 2 = 1, Remainder = 0                                                                                                  |
|                   🔹 1 / 2 = 0, Remainder = 1                                                                                                  |
|                                                                                                                                                |
|     🔹 After this calculation, we can get remainder in a reversed order (bottom to top) "1010"                                                 |
|                                                                                                                                                |
| 🔶 How to Convert Binary to Decimal                                                                                                            |
|                                                                                                                                                |
|    🔸 Example for "10 (1010)":                                                                                                                 |
|                  🔹  1x2³ + 0x2² + 1x2¹ + 0x2⁰                                                                                                 |
|                  🔹  8   +  0   +  2   +  0                                                                                                    |
|                  🔹 = 10                                                                                                                       |
|                                                                                                                                                |
| 🔷 How to Choose Number of Bits                                                                                                                |
|                                                                                                                                                |
|    🔹 bool      -->  1 byte   -->   false/true (0/1)                                                                                           |
|    🔹 int8_t    -->  1 byte   -->   -128        to     127                                                                                     |
|    🔹 uint8_t   -->  1 byte   -->   0           to     255                                                                                     |
|    🔹 int16_t   -->  2 bytes  -->   -32,768     to     32,768                                                                                  |
|    🔹 int       -->  4 bytes  -->   -2.1B       to     2.1B                                                                                    |
|    🔹 int64_t   -->  8 bytes  -->   Very Large                                                                                                 |
|                                                                                                                                                |
| 🔶 1 byte = 8 bits                                                                                                                             |
|                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                             Important Concepts                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                |
| 💠 "SET/UNSET BITS": 0 --> Set Bit, 1 --> Unset Bits                                                                                           |
|                                                                                                                                                |
| 💠 "Power of 2": Power of 2 will always have only "1" in the binary.                                                                           |
|                                                                                                                                                |
| 💠 "Remove Last Set Bit": To remove last set bit we will use "n & (n - 1)"                                                                     |
|                                                                                                                                                |
| 💠 "Extract Last Set Bit": To extract last set bit we will use "n & (-n)", -n means two's compliment.                                          |
|                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                          Bit Manipulation Operators                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                |
| ⭐ "AND (&)":                                                                                                                                  |
|                                                                                                                                                |
|              4 = 0100                                                                                                                          |
|           &  1 = 0001                                                                                                                          |
|                  0001     ==> If corresponding bit are (1 & 1) then it will "1" otherwise "0"                                                  |
|                                                                                                                                                |
| ⭐ "OR (|)":                                                                                                                                   |
|                                                                                                                                                |
|              4 = 0100                                                                                                                          |
|           |  1 = 0001                                                                                                                          |
|                  0101     ==> If one of the corresponding bit "1" then it will "1" otherwise "0"                                               |
|                                                                                                                                                |
| ⭐ "NOT (~)":                                                                                                                                  |
|                                                                                                                                                |
|              4 = 0100                                                                                                                          |
|              ~   1011     ==> Flip all the bits, If it's 0 "flip to 1", 1 "flip to 0"                                                          |
|                                                                                                                                                |
| ⭐ "XOR (^)":                                                                                                                                  |
|                                                                                                                                                |
|              4 = 0100                                                                                                                          |
|           ^  1 = 0001                                                                                                                          |
|                  0101     ==> If corresponding bits are same then "0" otherwise "1".                                                           |
|                                                                                                                                                |
|     🔵 Popular use cases are: "Swapping without temps", "Finding missing numbers"                                                              |
|                                                                                                                                                |
| ⭐ "LEFT-SHIFT (<<)": Shift bits to left                                                                                                       |
|                                                                                                                                                |
|              4 = 0100                                                                                                                          |
|          <<  1                                                                                                                                 |
|              8 = 1000     ==> Used to multiply by power of 2.     a << n = a x 2^n                                                             |
|                                                                                                                                                |
| ⭐ "RIGHT-SHIFT (>>)": Shift bits to right                                                                                                     |
|                                                                                                                                                |
|              4 = 0100                                                                                                                          |
|          >>  1                                                                                                                                 |
|              2 = 0010     ==> Used to divide by power of 2.     a << n = a / 2^n                                                               |
|                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                   FORMULAS                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                |
| 1.  "n & (n-1)"          : Removes the rightmost set bit.                                                                                      |
|                                                                                                                                                |
| 2.  "n & (-n)"           : Isolates the rightmost set bit.                                                                                     |
|                                                                                                                                                |
| 3.  "n | (1 << i)"       : Sets the bit at position i.                                                                                         |
|                                                                                                                                                |
| 4.  "n & ~(1 << i)"      : Clears the bit at position i.                                                                                       |
|                                                                                                                                                |
| 5.  "n ^ (1 << i)"       : Toggles the bit at position i.                                                                                      |
|                                                                                                                                                |
| 6.  "(n >> i) & 1"       : Checks if bit at position i is set.                                                                                 |
|                                                                                                                                                |
| 7.  "n & (1 << i)"       : Checks if bit at position i is set (non-zero = set).                                                                |
|                                                                                                                                                |
| 8.  "n & 1"              : Checks if n is odd (1 = odd, 0 = even).                                                                             |
|                                                                                                                                                |
| 9.  "n << 1"             : Multiplies n by 2.                                                                                                  |
|                                                                                                                                                |
| 10. "n >> 1"             : Divides n by 2.                                                                                                     |
|                                                                                                                                                |
| 11. "n & (n-1) == 0"     : Checks if n is a power of 2.                                                                                        |
|                                                                                                                                                |
| 12. "n ^ n"              : Always gives 0.                                                                                                     |
|                                                                                                                                                |
| 13. "n ^ 0"              : Always gives n.                                                                                                     |
|                                                                                                                                                |
| 14. "a ^= b; b ^= a; a ^= b" : Swaps a and b without a temp variable.                                                                          |
|                                                                                                                                                |
| 15. "(a ^ b) < 0"        : Checks if a and b have opposite signs.                                                                              |
|                                                                                                                                                |
| 16. "n & ((1 << k) - 1)" : Gets the last k bits of n.                                                                                          |
|                                                                                                                                                |
| 17. "n & ~((1 << k) - 1)": Clears the last k bits of n.                                                                                        |
|                                                                                                                                                |
| 18. "n & ~(1<<(len-1))"  : Removes the leftmost set bit.                                                                                       |
|                                                                                                                                                |
| 19. "n | (n-1)"          : Sets all bits after the rightmost set bit.                                                                          |
|                                                                                                                                                |
| 20. "__builtin_popcount(n)"  : Counts total set bits in n (C++ built-in).                                                                      |
|                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                               BINARY NUMBERS                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                |
| 1 = 0001                                                                                                                                       |
| 2 = 0010                                                                                                                                       |
| 3 = 0011                                                                                                                                       |
| 4 = 0100                                                                                                                                       |
| 5 = 0101                                                                                                                                       |
| 6 = 0110                                                                                                                                       |
| 7 = 0111                                                                                                                                       |
| 8 = 1000                                                                                                                                       |
| 9 = 1001                                                                                                                                       |
| 10 = 1010                                                                                                                                      |
| 11 = 1011                                                                                                                                      |
| 12 = 1100                                                                                                                                      |
| 13 = 1101                                                                                                                                      |
| 14 = 1110                                                                                                                                      |
| 15 = 1111                                                                                                                                      |
|                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+
"""

"""
+-----------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                       🟡 BASIC                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------+
"""

# EASY PROBLEMS

# GETTING LAST BIT

# CHECKING K-TH BIT IS SET OR NOT

# TOGGLING K-TH BIT TO SET

# FLIPPING K-TH BIT

# COUNTING NUMBER OF SET BITS - In Binary decimal number are sum of power of 2 So (13 = 2³ + 2² + 2⁰ = 13 So in binary there wil be "3 set bits")

# To count number of set bits -> Will use a format that remove the set bit from right hand side, if we keep removing set bits from right hand side at the end we got total count.

# CHECKING WHETHER IT'S POWER OF 2 OR NOT

# Step 1.

# Main function

# EVEN ODD

# GETTING LAST BIT

# CHECKING K-TH BIT IS SET OR NOT

# TOGGLING K-TH BIT TO SET

# FLIPPING K-TH BIT

# COUNTING NUMBER OF SET BITS

# CHECKING IF THE NUMBER IF POWER OF 2 OF NOT

# namespace basic

"""
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                    🟡 DSA Problems                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
"""

# Reversing the binary value

# Step 1. Using XOR Operation We'll get "unique" and "duplicate" at end, All number will be canceled only remaining will be ("unique" ^ "duplicate").

# Step 2. Here we are calculating the different set bit from right side on ("unique" ^ "duplicate"), So that we can easily find it.

# Step 3. Grouping: Right most set bit tells, which bit from right is different in both of them. To find "unique" and "duplicate".

# Step 4. Getting "missing", "duplicate" number by checking every number if num matches with "bucket1" mean number is already there in "numbers" mean it's duplicate.

# Step 1. Performing "XOR" on the numbers so that, at the end we'll get ("unique" ^ "unique").

# Step 2. Finding rightmost set bit, because "rightmost" set bit will tell which bit is different.

# Step 3. Grouping both two "uniques" value into two variables.

# Looping through all subset masks

# Checking the set bit

# This map stores:

# prefixXOR value -> how many times it appeared

# Important: prefix before array starts is 0

# Build running prefix XOR

# Check if there exists a prefix such that:

# prefixXOR ^ previousPrefix = k

# So previousPrefix = prefixXOR ^ k

# Store current prefix

# Main function

# Find all subsets

# Reversing bits

# Finding one unique from three

# Count XOR Subarray

# namespace dsa_problems


def to_binary(number):
    return bin(number)[2:]


def is_bit_set(number, position):
    return (number & (1 << position)) != 0


def set_bit(number, position):
    return number | (1 << position)


def clear_bit(number, position):
    return number & ~(1 << position)


def toggle_bit(number, position):
    return number ^ (1 << position)
