# dash imports
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
# from dash.dependencies import Input, Output

# data wrangling imports
import pandas as pd

# local imports
# from app import app

layout = html.Div([
    html.H1('Structural MRI Data'),

    html.Br(),

    # MRI Table
    html.H2('Structural MRI Data'),
    dash_table.DataTable(
        id='mri-table'
    ),

    html.Br(),

    # MRI graph
    dcc.Graph(
        id='mri-graph'
    ),

    html.Br()
])