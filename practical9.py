import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Marks": [75, 85, 90, 65, 80, 95],
    "Hours": [2, 4, 5, 1, 3, 6],
    "Department": [
        "Computer",
        "IT",
        "Computer",
        "IT",
        "Computer",
        "IT"
    ]
}

df = pd.DataFrame(data)

# Line plot
sns.lineplot(data=df, x="Hours", y="Marks", marker="o")
plt.title("Hours vs Marks")
plt.show()

# Bar plot
sns.barplot(data=df, x="Department", y="Marks")
plt.title("Department vs Marks")
plt.show()

# Histogram
sns.histplot(data=df, x="Marks", bins=5, kde=True)
plt.title("Distribution of Marks")
plt.show()

# Box plot
sns.boxplot(data=df, x="Department", y="Marks")
plt.title("Marks by Department")
plt.show()

# Scatter plot
sns.scatterplot(
    data=df,
    x="Hours",
    y="Marks",
    hue="Department"
)

plt.title("Study Hours vs Marks")
plt.show()