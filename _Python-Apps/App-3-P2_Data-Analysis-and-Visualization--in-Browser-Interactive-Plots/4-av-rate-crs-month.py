import justpy as jp
from calendar import month
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name'])['Rating'].mean().unstack() # plots rating mean
# month_average_crs = data.groupby(['Month', 'Course Name'])['Rating'].count().unstack() # plots rating count
month_average = data.groupby(['Month']).mean()
print(month_average_crs) # to see what DataFrame looks like

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Analysis of Course Reviews'
    },
    subtitle: {
        align: 'center',
        text: 'Average Rating by Month by Course'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        title: {
            enabled: true,
            text: 'Date'
        },
        accessibility: {
            rangeDescription: 'Range: 2018-01 to 2021-04.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: 'Average Rating'
    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048
            ]
    }]
}
"""


def app():
    wp = jp.QuasarPage() # wp stands for webpage
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(month_average.index)

    # creates list comprehension of Course Names, average ratings column
    hc_data = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

    hc.options.series = hc_data

    return wp

jp.justpy(app)