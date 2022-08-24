# Making a basic Bokeh circle graph

# Importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Prepare some data
x=[3, 7.5, 10]
y=[3, 6, 9]

# Prepare the output file
output_file("Circle.html")

# Create a figure object
f=figure()

# Create circle
f.circle(x,y)

show(f)