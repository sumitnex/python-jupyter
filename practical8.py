import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.figure(figsize=(10, 8))

# Subplot 1
plt.subplot(2, 2, 1)
plt.plot(x, y1, color="blue", marker="o", label="Data 1")
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

# Subplot 2
plt.subplot(2, 2, 2)
plt.bar(x, y1, color="green", label="Data 1")
plt.title("Bar Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

# Subplot 3
plt.subplot(2, 2, 3)
plt.scatter(x, y2, color="red", label="Data 2")
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

# Subplot 4
plt.subplot(2, 2, 4)
plt.plot(x, y2, color="purple", marker="*", label="Data 2")
plt.title("Second Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()