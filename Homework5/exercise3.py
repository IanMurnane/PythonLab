import pandas as pd

df = pd.read_csv('data.csv')

df.set_index('PassengerId', inplace=True)

df.loc[df["Sex"] == "male", "Sex"] = "M"
df.loc[df["Sex"] == "female", "Sex"] = "F"

print(df.iloc[1])
