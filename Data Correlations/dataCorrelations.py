# Finding Relationships
# A great aspect of the Pandas module is the corr() method.
# The corr() method calculates the relationship between each column in your data set.

import pandas as pd

df = pd.read_csv(r"C:\Users\User\Downloads\data.csv")
# print(df)

# Show the relationship between the columns:
print(df.corr())
# Note: The corr() method ignores "not numeric" columns.




























