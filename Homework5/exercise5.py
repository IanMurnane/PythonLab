import pandas as pd

df = pd.read_csv('data.csv')

df = df[sorted(df.columns)]

print(df.iloc[0])
