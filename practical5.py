import pandas as pd

# Series
marks = pd.Series([85, 90, 78, 92, 88])

print("Series:")
print(marks)

# DataFrame
data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Neha"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# First five rows
print("\nHead:")
print(df.head())

# Last five rows
print("\nTail:")
print(df.tail())

# Summary statistics
print("\nDescription:")
print(df.describe())

# Select column
print("\nNames:")
print(df["Name"])

# Select rows
print("\nFirst three rows:")
print(df.iloc[:3])

# Add a column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

print("\nUpdated DataFrame:")
print(df)

# Export CSV
df.to_csv("students.csv", index=False)

print("\nCSV file created successfully.")
