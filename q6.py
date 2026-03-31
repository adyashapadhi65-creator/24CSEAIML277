# Q. WAP to create and work with pandas Series

import pandas as pd

data = [10, 20, 30, 40]
s = pd.Series(data)

print("Series:")
print(s)

print("First element:", s[0])
print("Last element:", s[3])

print("Sum:", s.sum())
print("Mean:", s.mean())

s2 = pd.Series(data, index=["a", "b", "c", "d"])
print("Series with custom index:")
print(s2)

print("Access using label:", s2["b"])