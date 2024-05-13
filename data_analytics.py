import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns

#loading data
titan=pd.read_csv("titanic.csv")
print(titan.head(5))
#print(titan.tail())
print(titan.sample())