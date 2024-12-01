# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

import pandas as pd 

data = { "player": ['Rohit','Virat','KL','Tilak'],
        "Number": [45,18,100,39]}

#load data into a DataFrame object:
cricket = pd.DataFrame(data)

print(cricket)

# What is a DataFrame?
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

# Locate Row
# Pandas use the loc attribute to return one or more specified row(s)
# Return row 0:

# print(cricket.loc[0]) ##refer to the row index:

# Return row 0 and 1:

# print(cricket.loc[0,1]) #use a list of indexes


# Named Indexes
# With the index argument, you can name your own indexes.
# Add a list of names to give each row a name:
cricket = pd.DataFrame(data, index = [1,2,3,4])
print(cricket)

# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).

print(cricket.loc[1])







