## 1. Overview of the dataframe
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

df = pandas.DataFrame(data)

"""
data.head()
data.shape
data.columns

plt.hist(df['Rating'])
plt.show()
"""


## 2. Selecting data from the dataframe
### Select a column
"""
print(data['Rating']) #.mean()
print()
"""

### Select multiple columns
"""
print(data[['Course Name', 'Rating']])
print()
"""

### Selecting a row
"""
print(data.iloc[3])
print()
"""

### Selecting multiple rows
"""
print(data.iloc[1:3])
print()
"""

### Selecting a section
"""
print(data[['Course Name', 'Rating']].iloc[1:3])
print()
"""

### Selecting a cell
"""
print(data['Timestamp'].iloc[2])
print(data.at[2, 'Rating'])
print()
"""

## 3. Filtering data based on conditions
### One condition
"""
d2 = data[data['Rating'] > 4]
print(d2['Rating'])
print()
print(d2['Rating'].mean())
print()
"""

### Multiple conditions
"""
print(data[(data['Rating'] > 4) & (data['Course Name'] == 'The Complete Python Course: Build 10 Professional OOP Apps')]['Rating'].mean())
print()
"""

## 4. Time-based filtering
print(data[(data['Timestamp'] >= datetime(2020, 7, 1, tzinfo=utc)) & (data['Timestamp'] < datetime(2020, 12, 31, tzinfo=utc))])