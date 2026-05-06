import pandas as pd

df = pd.read_csv("data.csv")

name = input("Enter name: ")
result = df[df["Name"].str.contains(name, na=False)]

print(result)
