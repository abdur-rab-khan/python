from decimal import Decimal
x = 5
y = 8
z = 20

n_t = x, y, z  # Tuple of numbers

x, y, z = n_t  # Unpacking the tuple  >> 5 8 20

# We can directly calculate the power of any number without any other method
x = x ** 2  # 25
x = x ** 3  # 125

# How can we handle larger numbers in python.
l = 100000000000000000000000000 * 0.5  # ❌ >> 5e+25
lc = Decimal('100000000000000000000000') * Decimal('0.5')
large = Decimal('50000000000000000000000.0')
l_to_i = int(Decimal('100000000000000000000000') *
             Decimal('0.5'))  # ✅ >> 50000000000000000000000
