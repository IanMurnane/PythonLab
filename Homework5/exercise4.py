import pandas as pd

df = pd.read_csv('data.csv')

df.set_index('PassengerId', inplace=True)

df.loc[df["Sex"] == "male", "Sex"] = "M"
df.loc[df["Sex"] == "female", "Sex"] = "F"

df['Sum'] = df.iloc[:, [0, 1]].sum(axis=1)

print(df.iloc[1])
