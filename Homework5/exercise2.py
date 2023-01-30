import pandas as pd

df = pd.read_csv('data.csv')

df.set_index('PassengerId', inplace=True)

print(df.iloc[0])
