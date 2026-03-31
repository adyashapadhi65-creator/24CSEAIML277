# Q5. WAP for saving and loading numpy arrays
import numpy as np

arr = np.array([1,2,3,4])
np.save("myarray.npy", arr)

loaded = np.load("myarray.npy")
print(loaded)