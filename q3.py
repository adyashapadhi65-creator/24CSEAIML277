# Q3. WAP to draw histogram and box plot using matplotlib.pyplot as plt
import matplotlib.pyplot as plt

data = [22, 87, 5, 43, 56, 13, 55, 54, 11, 20, 51, 5]

plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Frequency")
plt.ylabel("Data")
plt.show()

plt.boxplot(data)
plt.title("Box Plot")
plt.show()