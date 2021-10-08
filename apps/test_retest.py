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
    html.H1('Test-Retest Data'),

    html.Br(),

    # table
    dash_table.DataTable(
        id='test-retest-table'
    ),

    html.Br(),

    # graphs
    dcc.Graph(
        id='test-retest-graph'
    ),

])