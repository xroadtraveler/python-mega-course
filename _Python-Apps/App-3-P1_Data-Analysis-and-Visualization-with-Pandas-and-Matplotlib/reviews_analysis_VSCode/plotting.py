import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

# Process data to group by date
data['Day'] = data['Timestamp'].dt.date
# data.head()

# Group by day
day_average = data.groupby(['Day']).mean() # plot mean
# day_average = data.groupby(['Day']).count() # plot count

# Plot
plt.figure(figsize=(25, 3))
plt.plot(day_average.index, day_average['Rating'])
plt.show()