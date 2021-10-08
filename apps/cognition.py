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


def get_data():
    beta_unicode = '\u03B2'
    df = pd.DataFrame({
        beta_unicode: {
            'test1': 1,
            'test2': 2,
            'test3': 3
        },
        'y-Intercept': {
            'test1': 0.1,
            'test2': 0.2,
            'test3': 0.3
        },
        'error': {
            'test1': 0.01,
            'test2': 0.02,
            'test3': 0.03
        }
    }).to_dict('records')
    return df


def get_predictors():
    return ['var1', 'var2', 'var3']


def get_covariates():
    return ['cov1', 'cov2', 'cov3']


def get_cognitive_tests():
    return ['test1', 'test2', 'test3']


layout = html.Div([

    # main header
    html.H1('Cognitive Data'),

    html.Br(),

    # dropdown for predictor variable
    dcc.Dropdown(
        id='cognition-predictor-dropdown',
        options=[{'label': i, 'value': i} for i in get_predictors()]
    ),

    # dropdown for covariates
    dcc.Dropdown(
        id='cognition-covariate-dropdown',
        options=[{'label': i, 'value': i} for i in get_covariates()]
    ),

    # summary table of lm coefficients by test vs. HOMA-IR
    dash_table.DataTable(
        id='cognition-table',
        columns=[{'name': i, 'id': i} for i in ['Test', '\u03B2', 'y-Intercept', 'Error', 'R2']],
        data=get_data()
    ),

    html.Br(),

    dcc.Dropdown(
        id='cognition-test-dropdown',
        options=[{'label': i, 'value': i} for i in get_cognitive_tests()]
    ),

    # graphs of lm by test vs. HOMA-IR
    dcc.Graph(
        id='cognition-graph'
    )

])