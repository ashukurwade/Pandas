# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type

# Create a simple Pandas Series from a list
import pandas as pd
h = [45,18,9,39]
myseries = pd.Series(h)
print(myseries)

# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.
print(myseries[0])

# Create Labels
# With the index argument, you can name your own labels.
# Create your own labels
myseries = pd.Series(h, index = ["Rohit", "Virat", "Ishan", "Tilak"])
print(myseries)

# When you have created labels, you can access an item by referring to the label.
print(myseries["Rohit"])

