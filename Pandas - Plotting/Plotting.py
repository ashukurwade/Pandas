# Plotting
# Pandas uses the plot() method to create diagrams.
# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.

# Import pyplot from Matplotlib and visualize our DataFrame:
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv(r"C:\Users\User\Downloads\data.csv")
print(df)
df.plot()
plt.show()

# Scatter Plot
# Specify that you want a scatter plot with the kind argument:
# kind = 'scatter'
# A scatter plot needs an x- and a y-axis.
# In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.
# Include the x and y arguments like this:
# x = 'Duration', y = 'Calories'

df.plot(kind='scatter', x ='Duration', y ='Calories')
plt.show()

# A scatterplot where there are no relationship between the columns:
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()

# Histogram
# Use the kind argument to specify that you want a histogram:
# kind = 'hist'
# A histogram needs only one column.
# A histogram shows us the frequency of each interval

df["Duration"].plot(kind = 'hist')

