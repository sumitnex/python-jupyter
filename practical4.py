import numpy as np

# Random numbers between 0 and 1
random_numbers = np.random.rand(10)

print("Random numbers:")
print(random_numbers)

normal_numbers = np.random.randn(10)

print("\nStandard normal random numbers:")
print(normal_numbers)

# Random integers
integers = np.random.randint(1, 101, 10)

print("\nRandom integers:")
print(integers)

# Normal distribution
normal_distribution = np.random.normal(
    loc=50,
    scale=10,
    size=1000
)

print("\nNormal distribution:")
print(normal_distribution[:10])

# Statistics
print("Mean:", np.mean(normal_distribution))
print("Median:", np.median(normal_distribution))
print("Standard deviation:", np.std(normal_distribution))
print("Variance:", np.var(normal_distribution))
print("Minimum:", np.min(normal_distribution))
print("Maximum:", np.max(normal_distribution))