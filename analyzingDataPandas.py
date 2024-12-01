# Pandas - Analyzing DataFrames

# Viewing the Data
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# The head() method returns the headers and a specified number of rows, starting from the top.

# Get a quick overview by printing the first 10 rows of the DataFrame

# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

import pandas as pd
df = pd.read_csv(r"C:\Users\User\Desktop\Ashu\gender_submission.csv")
print(df)
print("-----------------------------------------------")

print(df.head(10))
# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
print("-----------------------------------------------")

# Print the first 5 rows of the DataFrame
print(df.head())
print("-----------------------------------------------")

# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
# Print the last 5 rows of the DataFrame
print(df.tail())
print("-----------------------------------------------")
### Info About the Data ###
# The DataFrames object has a method called info(), that gives you more information about the data set.
print(df.info())
print("-----------------------------------------------")

## Null Values ##
# The info() method also tells us how many Non-Null values there are present in each column, and in our data set
# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data

