import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Neha"],
    "Department": ["Computer", "IT", "Computer", "IT", "Computer"],
    "Marks": [85, np.nan, 78, 92, np.nan],
    "Age": [20, 21, np.nan, 22, 21]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Detect missing values
print("\nMissing values:")
print(df.isnull())

print("\nNumber of missing values:")
print(df.isnull().sum())

# Fill missing values
df_filled = df.fillna({
    "Marks": df["Marks"].mean(),
    "Age": df["Age"].mean()
})

print("\nAfter filling missing values:")
print(df_filled)

# Drop rows containing missing values
df_dropped = df.dropna()

print("\nAfter dropping missing rows:")
print(df_dropped)

# Filtering
print("\nStudents with marks > 80:")
print(df_filled[df_filled["Marks"] > 80])

# Select columns
print("\nName and Marks:")
print(df_filled[["Name", "Marks"]])

# Sorting
print("\nSorted by Marks:")
print(df_filled.sort_values("Marks", ascending=False))

# Grouping
print("\nDepartment-wise average marks:")
print(
    df_filled.groupby("Department")["Marks"].mean()
)