import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "ggplot2"

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = np.loadtxt('https://raw.githubusercontent.com/adithya-gv/energy-anomaly/master/dataset/10112.dat', dtype=float)


#Decent Histogram
fig = px.histogram(df, x=df[:,1], y=df[:,2], log_x=True, log_y=True)
#Single-day graph:
fig.update_layout(title_text="Cumulative Energy Consumption Across Days")
fig.update_xaxes(title_text='Day')
fig.update_yaxes(title_text='Cumulative Energy Consumption')

result = np.where(df == 112.0)
fig2 = px.line(df, x=df[result[0],1], y=df[result[0],2])
fig2.update_layout(title_text="Energy Consumption Across a Single Day")
fig2.update_xaxes(title_text='Day')
fig2.update_yaxes(title_text='Energy Consumption')

#fig2 = px.line(df, x=df[:,1], y=df[:,2])

#fig = px.scatter(df, x=df[:,1], y=df[:,2], color=df[:,2],
                 #log_x=True, size_max=20)

'''fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)
fig2 = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="population", hover_name="country",
                 log_x=True, size_max=60)'''

app.layout = html.Div([
    html.H1(children='Energy Consumption Analysis',
    style = {
        'textAlign': 'center'
    }
    ),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    ),
    dcc.Graph(
        id='life-exp-vs-gdp2',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)