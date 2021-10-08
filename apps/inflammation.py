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
    html.H1('Inflammation Data'),

    html.Br(),

    # CBC Table
    html.H2('CBC Data'),
    dash_table.DataTable(
        id='inflammation-cbc-table'
    ),

    html.Br(),

    # CBC graph
    dcc.Graph(
        id='inflammation-cbc-graph'
    ),

    html.Br(),

    # cytokines table
    html.H2('Cytokine Data'),
    dash_table.DataTable(
        id='inflammation-cytokine-table'
    ),

    html.Br(),

    # cytokine graph
    dcc.Graph(
        id='inflammation-cytokine-graph'
    ),

    html.Br(),

    # FACS Table?
    html.H2('FACS Data'),
    dash_table.DataTable(
        id='inflammation-facs-table'
    ),

    html.Br(),

    # FACS graph
    dcc.Graph(
        id='inflammation-facs-graph'
    ),

])