# Q5. WAP to draw the 3D plot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]
z = [2, 3, 3, 3, 2]

ax.scatter(x, y, z, color='r', label='3D Points')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.title("3D Plot")
plt.show()