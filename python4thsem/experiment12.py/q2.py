# Q2. WAP to draw scatter and bar plot using matplotlib.pyplot as plt
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 7]

plt.scatter(x, y, color='b', label='Scatter')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

plt.bar(x, y, color='g')
plt.title("Bar Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()