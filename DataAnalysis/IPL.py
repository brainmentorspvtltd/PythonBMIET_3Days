import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('matches.csv')
#print(df.shape)

#print(df.head())

print(df.describe())
