import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')

df.hist(column=["Age", "Sex", "Survived"])

plt.show()
