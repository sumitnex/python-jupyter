import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Vectorized operations
print("Addition:")
print(np.add(a, b))

print("\nSubtraction:")
print(b - a)

print("\nMultiplication:")
print(a * b)

print("\nDivision:")
print(b / a)

# Universal functions
print("\nSquare root:")
print(np.sqrt(a))

print("\nExponential:")
print(np.exp(a))

# Broadcasting
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

value = 10

print("\nOriginal array:")
print(arr)

print("\nBroadcasting 10:")
print(arr + value)


row = np.array([10, 20, 30])

print("\nBroadcasting with row:")
print(arr + row)