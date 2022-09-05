## Overview of the dataframe
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv")

df = pandas.DataFrame(data)

data.head()
data.shape
data.columns

plt.hist(df['Rating'])
plt.show()

## Selecting data from the dataframe
### Select a column
print(data['Rating']) #.mean()
print()

### Select multiple columns
print(data[['Course Name', 'Rating']])
print()

### Selecting a row
print(data.iloc[3])
print()

### Selecting multiple rows
print(data.iloc[1:3])
print()

### Selecting a section
print(data[['Course Name', 'Rating']].iloc[1:3])
print()

### Selecting a cell
print(data['Timestamp'].iloc[2])
print(data.at[2, 'Rating'])
print()