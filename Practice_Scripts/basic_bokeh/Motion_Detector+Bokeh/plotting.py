from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

# Changes df times into formatted datetimes
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

# Passes DataFrame data to ColumnDataSource object
cds=ColumnDataSource(df)

# Creates a Figure "p" as our "Motion Graph"
p=figure(x_axis_type='datetime', height=100, width=500, sizing_mode="scale_both", title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.yaxis[0].ticker.desired_num_ticks=1

# Creates a tooltip hover function
hover=HoverTool(tooltips=[("Start: ","@Start_string"), ("End: ","@End_string")])
p.add_tools(hover)

# Formats our graph
q=p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

output_file("Graph.html")
show(p)