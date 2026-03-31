# Q. WAP to create pandas DataFrame and perform basic operations
import pandas as pd

data = {
    "Name": ["Alice","Bob","Charlie"],
    "Age": [25,30,35],
    "City": ["NY","LA","SF"]
}

df = pd.DataFrame(data)
print(df)

print(df["Name"])
print(df.iloc[0])