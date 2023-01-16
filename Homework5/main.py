import pandas as pd

df = pd.read_csv('data.csv')

corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)
