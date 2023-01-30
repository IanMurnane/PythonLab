import pandas as pd

df = pd.read_csv('data.csv')

avg_age = df["Age"].mean()

df["Age"] = df["Age"].fillna(avg_age)

print(df.to_string())
