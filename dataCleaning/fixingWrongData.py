# Wrong Data
#"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong

# Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

# Replacing Values
# One way to fix wrong values is to replace them with something else.

import pandas as pd

df = pd.read_csv(r"C:\Users\User\Downloads\data.csv")
print(df)

# Set "Duration" = 45 in row 7
df.loc[7, 'Duration'] = 45

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

# If the value is higher than 120, set it to 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

# Removing Rows
# Another way of handling wrong data is to remove the rows that contains wrong data.
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
