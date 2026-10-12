import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load real-world dataset
df = sns.load_dataset("iris")

print("First five rows:")
print(df.head())

print("\nLast five rows:")
print(df.tail())

# Dataset information
print("\nDataset information:")
print(df.info())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate values
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Species count
print("\nSpecies count:")
print(df["species"].value_counts())