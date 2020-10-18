import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# data frame
df = pd.read_csv('https://media.githubusercontent.com/media/adithya-gv/energy-anomaly/master/final/predictSet1.csv')
# scatterplot
# specific colors for non anomaly, anomaly data
fig = px.scatter(
    df, x = "Day", y = "Value", color = "Flag"
)

fig.update_xaxes(tickangle = 45) # set x axis label angle
# fig.update_xaxes(range = [0, 500])

app.layout = html.Div(children=[
    html.H1 (
        children = 'Energy Consumption Analysis',
        style = {
            'textAlign': 'center'
        }
    ),

    html.Div(children = 'Anomalous and Nonanomalous Predictions', style = {
        'textAlign': 'center'
    }),

    dcc.Graph(
        id = 'energy-consump-vs-day',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(debug = True)
