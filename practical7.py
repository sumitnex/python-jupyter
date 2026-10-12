import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# Line plot
plt.plot(x, y, marker="o")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Plot")
plt.show()

# Bar plot
names = ["A", "B", "C", "D"]
marks = [80, 90, 70, 85]

plt.bar(names, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Bar Chart")
plt.show()

# Scatter plot
plt.scatter(x, y, color="red")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot")
plt.show()

# Histogram
data = [10, 20, 20, 30, 30, 30, 40, 40, 50, 50]

plt.hist(data, bins=5, color="green", edgecolor="black")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()