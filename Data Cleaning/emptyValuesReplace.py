# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# Calculate the MEAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv(r"C:\Users\User\Downloads\data.csv")

# Calculate the MEAN, and replace any empty values with it:
x = df["Calories"].mean()

df["Calories"].fillna(x)

# Mean = the average value (the sum of all values divided by number of values).

# Calculate the MEDIAN, and replace any empty values with it:
y = df["Calories"].median()

df["Calories"].fillna(y)
# Median = the value in the middle, after you have sorted all values ascending.

# Calculate the MODE, and replace any empty values with it:
z = df["Calories"].mode()[0]

df["Calories"].fillna(z)
# Mode = the value that appears most frequently.

