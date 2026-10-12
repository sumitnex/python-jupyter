import numpy as np

# 1D array
arr1 = np.array([10, 20, 30, 40, 50])
#printing
print("1D Array:")
print(arr1)

# Indexing
print("First element:", arr1[0])
print("Third element:", arr1[2])

# Slicing
print("First three elements:", arr1[:3])
print("Elements from index 2:", arr1[2:])

# arange
arr2 = np.arange(1, 11)
print("\nArray using arange:")
print(arr2)

# linspace
arr3 = np.linspace(0, 10, 5)
print("\nArray using linspace:")
print(arr3)

# 2D array
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n2D Array:")
print(arr2d)

# Indexing
print("Element at row 1, column 2:", arr2d[1, 2])

# Slicing
print("First two rows:")
print(arr2d[:2])

print("First two columns:")
print(arr2d[:, :2])

# Reshaping
arr4 = np.arange(1, 13)
reshaped = np.reshape(arr4, (3, 4))

print("\nReshaped Array:")
print(reshaped)

# Mathematical operations
print("\nSum:", np.sum(arr2d))
print("Mean:", np.mean(arr2d))
print("Maximum:", np.max(arr2d))
print("Minimum:", np.min(arr2d))