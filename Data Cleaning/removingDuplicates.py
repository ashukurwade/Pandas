# Discovering Duplicates
# Duplicate rows are rows that have been registered more than one time.

import pandas as pd

df = pd.read_csv(r"C:\Users\User\Downloads\data.csv")
print(df)
print(df.info())

# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:

# Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())

# Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.
# Remove all duplicates:
df.drop_duplicates(inplace=True)
print(df)

# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.
