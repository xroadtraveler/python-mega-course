import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv")

df = pandas.DataFrame(data)

data.head()
data.shape
data.columns

plt.hist(df['Rating'])
plt.show()