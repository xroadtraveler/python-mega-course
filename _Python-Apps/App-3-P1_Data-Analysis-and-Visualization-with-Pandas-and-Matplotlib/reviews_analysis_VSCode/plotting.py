import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])



### Rating average/count by day
# Process data to group by date
"""
data['Day'] = data['Timestamp'].dt.date
# data.head()
"""

# Group by day
"""
day_average = data.groupby(['Day']).mean() # plot mean
# day_average = data.groupby(['Day']).count() # plot count
"""

# Plot day graph
"""
plt.figure(figsize=(25, 3))
plt.plot(day_average.index, day_average['Rating'])
plt.show()
"""



### Rating average by week
# Process data to group by week
"""
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
# print(data['Week']) # Check
"""

# Group by week
"""
week_average = data.groupby(['Week']).mean()
print(week_average)
"""

# Plot week graph
"""
plt.figure(figsize=(25, 3))
plt.plot(week_average.index, week_average['Rating'])
plt.show()
"""



### Rating average by month
# Process data to group by month
"""
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
print(data['Month']) # Check
"""

# Group by month
"""
month_average = data.groupby(['Month']).mean()
print(month_average)
"""

# Plot month graph
"""
plt.figure(figsize=(25, 3))
plt.plot(month_average.index, month_average['Rating'])
plt.show()
"""



### Average rating by month by course
# Process data to group by month AND course name
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name']).mean().unstack() # to graph mean
# month_average_crs = data.groupby(['Month', 'Course Name'])['Rating'].count().unstack() # to graph count
# print(month_average_crs[-20:]) # Check
# print(month_average_crs.index) # Check
# print(month_average_crs.columns) # Check

# Plot the average per month per course
month_average_crs.plot(figsize=(25, 8))
plt.show()