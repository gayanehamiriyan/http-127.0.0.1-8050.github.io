import dash
import dash_core_components as dcc
import dash_html_components as html
from graphs import f1
from graphs import f2
from graphs import f3
from graphs import f4
from graphs import f5


app=dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div([

#Row 1 heading

        html.Div([
          html.H1("", className='four columns'),
          html.H2("Homework 3",style={'color': 'red', 'fontSize': 30}, className='four columns'),
          html.H1("", className='four columns')
          ], className="row"),
#Row 2 First grapf (barplot)
        html.Div([
          html.Div("Homework 3 assumes the development of this web application using Dash and Plotly in Python. You are required to develop 6 plots (including one table) with the given layout. Subtle differences related to styling (colors etc) are allowed, yet the general layout must be kept to perceive same information as this website does.", className='four columns'),
          html.Div(html.Div([html.H5(dcc.Markdown("**Graph 1**")),html.Div(["The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected."])]), className='four columns'),
          html.Div([
              (dcc.Graph(id="figure_1", figure= f1,className='four columns'))
            ])
         ], className= "row"),
#Row 3  Second grapf (Line graph)
        html.Div([
          html.Div(html.Div([html.H5(dcc.Markdown("**Graph 2**")),html.Div(["One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph."])]), className='four columns'),
          html.Div([
              (dcc.Graph(id="figure_2", figure= f2,className='six columns'))
            ]),
          html.Div("", className='two columns'),
          
         ], className= "row"),

#Row 4  Third and Fourt Graph (Box Plot and Table)
        html.Div([
          html.Div(html.Div([html.H5(dcc.Markdown("**Graph 3 and 4**")),html.Div(["One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph."])]), className='four columns'),
          html.Div([
              (dcc.Graph(id="figure_3", figure= f3,className='four columns'))
            ]),
          html.Div([
              (dcc.Graph(id="figure_4", figure= f4,className='four columns'))
            ]),
         ], className= "row"),

#Row 5  Fifth Graph (Box Plot and Table)
        html.Div([
          html.Div(html.Div([html.H5(dcc.Markdown("**Graph 5**")),html.Div(["Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap"])]), className='four columns'),
          html.Div([
              (dcc.Graph(id="figure_5", figure= f5,className='six columns'))
            ]),
          html.Div("", className='two columns'),
         ], className= "row"),

    ])

if __name__ == '__main__':
  app.run_server(debug=True)
