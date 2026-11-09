# Traversing using for loop

# Traversing using for each loop;

# XOR FOR SWAPPING

# Finding min value

# Finding max value

# Counting element frequency

# Printing all the frequency

# Initializing vector

# Traversing Techniques

# Revering an array

# Find min, max

# Count element frequency

def traverse(values):
    for value in values:
        print(value, end=" ")
    print()

def reverse_array(values):
    values = values[:]
    left, right = 0, len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
    return values

def find_min_max(values):
    if not values:
        return None, None
    return min(values), max(values)

def count_frequency(values):
    frequency = {}
    for value in values:
        frequency[value] = frequency.get(value, 0) + 1
    return frequency
