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
"""
print(data[(data['Timestamp'] >= datetime(2020, 7, 1, tzinfo=utc)) & (data['Timestamp'] < datetime(2020, 12, 31, tzinfo=utc))])
"""


## 5. From data to information

### Average rating
"""
print(data['Rating'].mean())
print()
"""

### Average rating for a particular course
"""
print(data[data['Course Name']=='The Python Mega Course: Build 10 Real World Applications']['Rating'].mean())
print()
"""

### Average rating for a particular period
"""
print(data[(data['Timestamp'] > datetime(2020, 1, 1, tzinfo=utc)) &
     (data['Timestamp'] < datetime(2020, 12, 31, tzinfo=utc))]['Rating'].mean())
print()
"""

### Average rating for a particular period for a particular course
"""
print(data[(data['Timestamp'] > datetime(2020, 1, 1, tzinfo=utc)) &
     (data['Timestamp'] < datetime(2020, 12, 31, tzinfo=utc)) &
    (data['Course Name']=='The Python Mega Course: Build 10 Real World Applications')
    ]['Rating'].mean())
print()
    """

### Average of uncommented ratings
"""
print(data[data['Comment'].isnull()]['Rating'].mean())
print()
"""

### Average of commented ratings
"""
print(data[data['Comment'].notnull()]['Rating'].mean())
print()
"""

### Number of uncommented ratings
"""
print(data[data['Comment'].isnull()]['Rating'].count())
print()
"""

### Number of commented ratings
"""
print(data[data['Comment'].notnull()]['Rating'].count())
print()
"""

### Number of comments containing a certain word
print(data[data['Comment'].str.contains('accent', na=False)])
print()
print(data[data['Comment'].str.contains('accent', na=False)]['Comment'].count())
print()

### Average of commented ratings with “accent” in the comment
print(data[data['Comment'].str.contains('accent', na=False)]['Rating'].mean())
print()

