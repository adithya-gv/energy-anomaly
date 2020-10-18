import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

df = np.loadtxt('https://raw.githubusercontent.com/adithya-gv/energy-anomaly/master/station_data/10112.dat', dtype=float)

fdf = np.loadtxt('https://raw.githubusercontent.com/adithya-gv/energy-anomaly/master/final/final10112.dat', dtype=float)

#Histogram of site 10112, timespan (over many days) vs Energy Consumption
fig = px.histogram(df, x=df[:,1], y=df[:,2], log_x=True, log_y=True)

#Labels for above graph^^
fig.update_layout(title_text="Cumulative Energy Consumption Across Days")
fig.update_xaxes(title_text='Day')
fig.update_yaxes(title_text='Cumulative Energy Consumption')

#Single-day histogram graph of energy consumption:
result = np.where(fdf == fdf[:,0].min())
fig2 = px.histogram(fdf, x=fdf[result[0],1], y=fdf[result[0],2])
fig2.update_layout(title_text="Energy Consumption Across a Single Day")
fig2.update_xaxes(title_text='Minutes')
fig2.update_yaxes(title_text='Energy Consumption')

# data frame
df3 = pd.read_csv('https://media.githubusercontent.com/media/adithya-gv/energy-anomaly/master/final/predictSet1.csv')
# scatterplot
# specific colors for non anomaly, anomaly data
fig3 = px.scatter(
    df3, x = "Day", y = "Value", color = "Flag"
)

fig3.update_layout(title_text="Anomalous and Nonanomalous Predictions")

fig3.update_xaxes(tickangle = 45) # set x axis label angle
# fig3.update_xaxes(range = [0, 500])

#HTML visual components, order affects order on webapp
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
        id = 'energy-consump-vs-day',
        figure = fig3
    ),
    dcc.Graph(
        id='graph-with-slider',
        figure=fig2
    ),
    dcc.Slider(
        id='day-slider',
        min=fdf[:,0].min(),
        max=fdf[:,0].max(),
        value=fdf[:,0].min(),
        marks={str(day): str(day) for day in np.unique(fdf[:,0])},
        step=None
    ),
    html.Div(id='my-output'),
])

#Callbacks, inputs such as the slider update the single-day graph and 'Day Chosen' Output
@app.callback(
    Output('graph-with-slider','figure'),
    Output(component_id='my-output', component_property='children'),
    [Input('day-slider','value')],
)
def update_figure(selected_day):
    result = np.where(fdf == selected_day)
    fig2 = px.histogram(fdf, x=fdf[result[0],1], y=fdf[result[0],2])
    fig2.update_layout(transition_duration=10)
    fig2.update_layout(title_text="Energy Consumption Across a Single Day")
    fig2.update_xaxes(title_text='Minutes')
    fig2.update_yaxes(title_text='Energy Consumption')
    return fig2, ('Day Chosen: {}'.format(selected_day))

if __name__ == '__main__':
    app.run_server(debug=True)
