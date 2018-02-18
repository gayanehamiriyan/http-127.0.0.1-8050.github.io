#Graph 1
from plotly.offline import iplot,plot
import pandas as pd
import numpy as np
import plotly.graph_objs as go
trace1=go.Bar(x=[15,50,15,20],y=["x8","x7","x6","x5"],orientation = 'h',marker=dict(color="purple"),name="Negative")
trace2=go.Bar(x=[-15,-45,-5,-35],y=["x4","x3","x2","x1"],orientation = 'h',marker=dict(color="pink"),name="Positive")
layout  = dict(title="Correlation with employees probability of churn",yaxis=dict(title="Variable"),showlegend=True)
f1=dict(data=[trace1,trace2],layout=layout)



#Graph 2
import quandl
quandl.ApiConfig.api_key = "mDPLGDvKMjWBm84nRxaT"
data = quandl.get("FRED/GDP")

from plotly.offline import plot, iplot
import plotly.graph_objs as go

import pandas as pd

x_values = pd.to_datetime(data.index.values)



y_values = data["Value"]
trace = go.Scatter(x=x_values,y=y_values,mode="lines",fill='tozeroy')
       
layout = go.Layout(title='US GDP over time')
data = [trace]
f2 = dict(data=data,layout=layout)


#Graph3
from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

import numpy as np

import quandl
quandl.ApiConfig.api_key = "mDPLGDvKMjWBm84nRxaT"
mydata1 = quandl.get("WIKI/GOOGL")

mydata2=quandl.get("BCHARTS/ABUCOINSUSD")


trace_1 = go.Box(x=mydata1.Open.pct_change(),name="Google")
trace_2 = go.Box(x=mydata2.Open.pct_change(),name="Bitcoin")
layout=dict(title="Distribution of Price Change")
data = [trace_2,trace_1]
f3 = dict(data=data,layout=layout)



#Graph3
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np

import quandl
quandl.ApiConfig.api_key = "mDPLGDvKMjWBm84nRxaT"
mydata1 = quandl.get("WIKI/GOOGL")

mydata2=quandl.get("BCHARTS/ABUCOINSUSD")


trace_1 = go.Box(x=mydata1.Open.pct_change(),name="Google")
trace_2 = go.Box(x=mydata2.Open.pct_change(),name="Bitcoin")
layout=dict(title="Distribution of Price Change")
data = [trace_2,trace_1]
f3 = dict(data=data,layout=layout)


#Graph 4
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np

import quandl
quandl.ApiConfig.api_key = "mDPLGDvKMjWBm84nRxaT"
mydata1 = quandl.get("WIKI/GOOGL")

mydata2=quandl.get("BCHARTS/ABUCOINSUSD")


#Google first four rows
goog=mydata1.Open.pct_change()
goog=goog.to_frame()
goog.reset_index(level=0, inplace=True)
goog_4=goog.loc[1:4]
goog_1pc=round(goog_4["Open"][1],3) #first percentage change wiki/google
goog_2pc=round(goog_4["Open"][2],3) #second percentage change wiki/google
goog_3pc=round(goog_4["Open"][3],3) #third percentage change wiki/google
goog_4pc=round(goog_4["Open"][4],3) #fourth percentage change wiki/google

#Bitcoin first four rows

bit=mydata2.Open.pct_change()
bit=bit.to_frame()

bit.reset_index(level=0, inplace=True)
bit_4=bit.loc[1:4]
bit_1pc=round(bit_4["Open"][1],3) #first percentage change bitcoin
bit_2pc=round(bit_4["Open"][2],3) #second percentage change bitcoin
bit_3pc=round(bit_4["Open"][3],3) #third percentage change bitcoin
bit_4pc=round(bit_4["Open"][4],3) #fourth percentage change bitcoin

from plotly.offline import plot, iplot
import plotly.graph_objs as go

header = dict(values=['Google','Bitcoin'],
              align = ['left','center'],
              font = dict(color = 'white', size = 12),
              fill = dict(color='#119DFF')
             )
cells = dict(values=[[goog_1pc,goog_2pc,goog_3pc,goog_4pc],
                     [bit_1pc,bit_2pc,bit_3pc,bit_4pc]],
             align = ['left','center'],
             fill = dict(color=["yellow","white"])
            )
trace = go.Table(header=header, cells=cells)

data = [trace]
layout = dict(width=500, height=300)
f4 = dict(data=data, layout=layout)



#Graph5
import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Task 1", Start='2018-01-01', Finish='2018-01-31',Resource='Idea Validation'),
      dict(Task="Task 2", Start='2018-03-01', Finish='2018-04-15', Resource='Team Formation'),
      dict(Task="Task 3", Start='2018-04-15', Finish='2018-09-30', Resource='Prototyping')]

colors = ['#7a0509', (0.1, 0.8, 0.1), 'rgb(254,224,144)']

f5 = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True, show_colorbar=True,title="Startup Roadmap")