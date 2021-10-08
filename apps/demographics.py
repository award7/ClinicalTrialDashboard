# dash imports
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output

# data wrangling imports
import pandas as pd

# local imports
from app import app


def get_subjects(df):
    return df['State'].tolist()


def get_stats_data(df):
    return pd.DataFrame({
        'Variable': df.columns,
        'Skewness': df.skew,
        'Kurtosis': df.kurt
    }).to_dict('records')


# TODO: change to fetch data from preproc util/object
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

layout = html.Div([

    # header
    html.H1("Demographics"),

    html.Div(
        children=[
            # subject picker
            dcc.Dropdown(
                id='enrollment-dropdown',
                options=[
                    {'label': f'PID{i}', 'value': i} for i in get_subjects(df)
                ],
                multi=True
            ),

            # table
            dash_table.DataTable(
                id='demographics-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
            ),

            # histographs?

            # lower-level stats tables and graphs
            dash_table.DataTable(
                id='demographics-stats-table',
                columns=[{"name": i, "id": i} for i in ["Variable", "Skewnness", "Kurtosis"]],
                data=df.to_dict('records')
            )
        ]
    )
])

# @app.callback(
#     Output('enrollment-graph', 'figure'),
#     Input('enrollment-dropdown', 'value')
# )
# def update_graph(value):
#     # if value == '':
#     #     pass
#     # else:
#     #     mask = (df['State'] == value[0])
#     #
#     # fig = px.scatter(
#     #     df[mask],
#     #     x='Number of Solar Plants',
#     #     y='Installed Capacity (MW)',
#     # )
#     # return fig
#     pass