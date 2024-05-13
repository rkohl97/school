# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
titanic = pd.read_csv("titanic.csv")
# Change code to *read_excel* for excel file

print(titanic.head(5))  # Print first five rows of data
print(titanic.tail(5))  # Gives last five rows of data
print(titanic.sample(10))  # Gives random 10 rows

# Identify variable types
print(titanic.dtypes)  # What datatypes we have in the columns of our data
print(titanic.describe())  # Gives count, mean, std dev, and other info

# Get count of values in a categorical variable
print(titanic['survived'].value_counts())

# Mean, median, mode, max, min
print(titanic['age'].median())

# Scatter plot
x = titanic['age']
y = titanic['fare']
plt.xlabel('age')
plt.ylabel('fare')
plt.scatter(x, y)
plt.show()

# Histogram
x = titanic['age']
plt.xlabel('age')
plt.ylabel('frequency')
plt.hist(x)  # For more bins: plt.hist(x, bins=15)
plt.show()

# Plot wouldn’t make sense; works best for time series plot
# Histogram
x = titanic['fare']
y = titanic['age']
plt.plot(x, y)
plt.show()

# Bar diagram
x = titanic['sex']
y = titanic['age']
plt.bar(x, y)  # plt.bar(x, y, color = "red", width=0.1) #plt.barh(x, y, color = "red", height = 0.1)
plt.show()
