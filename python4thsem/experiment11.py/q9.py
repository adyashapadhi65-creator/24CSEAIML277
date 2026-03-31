# Q9. WAP to calculate correlation between columns in pandas DataFrame
import pandas as pd

data = {
    "Math": [90,85,86,95],
    "Science": [88,82,85,90],
    "English": [78,75,80,85]
}

df = pd.DataFrame(data)
print(df.corr())