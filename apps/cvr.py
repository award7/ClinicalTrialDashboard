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
    html.H1('Cerebrovascular Reactivity Data'),

    html.Br(),

    # CVR data vs. HOMA-IR
    html.H2('Data'),
    dash_table.DataTable(
        id='cvr-table'
    ),

    html.Br(),

    # graphs
    dcc.Graph(
        id='cvr-graph'
    ),

])