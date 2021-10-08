# dash imports
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
# from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# data wrangling imports
import pandas as pd
from numpy import nan, linspace
from datetime import datetime
from math import floor

# local imports
# used for callbacks
from app import app


# function definitions
def get_date_duration(df: pd.DataFrame, pre: str, post: str):
    """
    calculate total duration from earliest date to latest date

    :param df:
    :param pre:
    :param post:
    :return:
    """

    return (df[post] - df[pre]).dt.days


def add_today_line(fig: go.Figure, orientation: str) -> go.Figure:
    """
    add line denoting today's date

    :param fig:
    :param orientation:
    :return:
    """

    # todo: change 'today' to datetime.date.today()
    today = '2009-04-20'
    fig.update_layout(shapes=[
        dict(
          type='line',
          yref='paper', y0=0, y1=1,
          xref='x', x0=today, x1=today
        )
    ])
    return fig


def visit_count_cumsum(df: pd.DataFrame, visit: str) -> pd.DataFrame:
    """
    Calculate the cumulative visits that occurred by a given date

    :param df: dataframe with visit dates
    :type df: pd.Dataframe
    :param visit: visit name corresponding to column name in df
    :type visit: str
    :return: dataframe with column of cumulative summation for visit occurrences
    :rtype: pd.Dataframe
    """

    # sort the df based on the target visit column
    df = df.sort_values(by=visit)

    # assign a value of '1' for any start visit that had occurred
    # todo: do this for every visit
    mask = pd.isnull(df[visit])

    # inverting the mask as it flags 'NaN' as 'True'
    mask = mask.replace({True: 0, False: 1})
    df[f'{visit}_Count_Bool'] = mask

    # do a cumulative summation of events
    df[f'{visit}_Count'] = df[f'{visit}_Count_Bool'].cumsum()

    return df


def create_gantt(df: pd.DataFrame, x_start: str, x_end: str, y: str) -> go.Figure:
    """

    :param df:
    :param x_start:
    :param x_end:
    :param y:
    :return:
    """
    # make base gantt chart
    gantt = px.timeline(df,
                        x_start=x_start,
                        x_end=x_end,
                        y=y,
                        color_discrete_sequence=['black'],
                        hover_data={'Start': False, 'Finish': False, 'Task': False, 'Duration': True})

    # change bar width
    # change tooltip for bar
    gantt.update_traces(
        width=0.025,
        hovertemplate="Duration: %{text} days",
        text=df['Duration']
    )

    # put gantt chart into figure object which will be used for adding traces
    fig = go.Figure(data=gantt.data, layout=gantt.layout)

    return fig


def add_visit_trace_gantt(fig: go.Figure, df: pd.DataFrame, x_name: str, y_name: str, trace_name: str = None,
                          symbol_icon: str = 'circle', symbol_color: str = 'black', symbol_size: int = 10) -> go.Figure:
    # marker documentation
    # https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.html#plotly.graph_objects.scatter.Marker

    # note: <extra></extra> tag removes the part of the hover where the trace name is usually displayed in a contrasting
    # color
    # source: https://plotly.com/python/hover-text-and-formatting/

    if trace_name is None:
        trace_name = x_name

    fig.add_trace(
        go.Scatter(
            x=df[x_name],
            y=df[y_name],
            marker={
                'symbol': symbol_icon,
                'size': symbol_size,
                'color': symbol_color
            },
            mode='markers',
            hovertemplate="{trace_name}: %{{x}}<extra></extra>".format(trace_name=trace_name, x=''),
            name=trace_name
        )
    )
    return fig


def add_visit_trace_identity(fig: go.Figure, df: pd.DataFrame, visit: str, trace_name: str = None,
                             color: str = None) -> tuple:
    # calculate cumulative sum of visit as a fcn of date
    df = visit_count_cumsum(df, visit)

    # add plot of visit occurrences
    identity_plot.add_trace(
        go.Scatter(
            x=df[visit],
            y=df[f'{visit}_Count'],
            mode='lines',
            line={
                'shape': 'hv'
            },
            name=visit
        )
    )

    return df, identity_plot


def create_visit_symbol_map() -> tuple:
    # map visits to symbol icons and colors
    visits = ['Start', 'Finish', 'Midpoint', 'Early']
    symbol_icons = ['circle', 'star-square', 'triangle-up', 'hexagram']
    symbol_colors = ['black', 'darkviolet', 'pink', 'lightslategrey']

    return visits, symbol_icons, symbol_colors


# import data into df
df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Midpoint="2009-01-31", Early="2009-01-15"),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Midpoint="2009-03-31", Early="2009-03-06"),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Midpoint="2009-04-20", Early=nan)
])

# convert date columns to datetime
for col in df.columns:
    if col == "Task":
        continue
    df[col] = pd.to_datetime(df[col])

df['Duration'] = get_date_duration(df, 'Start', 'Finish')

gantt = create_gantt(df, 'Start', 'Finish', 'Task')

visits, symbol_icons, symbol_colors = create_visit_symbol_map()

# add traces to gantt plot
for idx, visit in enumerate(visits):
    gantt = add_visit_trace_gantt(gantt, df, visit, 'Task', symbol_icon=symbol_icons[idx],
                                  symbol_color=symbol_colors[idx])

# list tasks from top --> bottom
# show y grid lines
gantt.update_yaxes(
    autorange="reversed",
    showgrid=True
)

# hide x grid line
gantt.update_xaxes(
    showgrid=False
)

# add title, axis titles, legend title
gantt.update_layout(
    title={
        'text': 'Suject Enrollment Timeline',
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top'
      },
    xaxis_title={
        'text': 'Date',
        # 'font': '',
        # 'standoff': ''
            },
    yaxis_title={
        'text': 'Task',
        # 'font': '',
        # 'standoff': ''
            },
    legend={
        'title': {
            'text': 'Visits'
        }
    },
    showlegend=True
)

# gantt.update_layout(hovermode='x unified')


# make predicted vs. real enrollment graph

# calculate the duration of the trial and determine the days per new subject enrollment
# todo: set trial start and end dates
start = pd.Timestamp('2009-01-01')
end = pd.Timestamp('2009-12-31')
delta = (end - start).days
sample_size = 55
days_between_new_subject_enrollment = floor(delta / sample_size)
day_array = linspace(start.value, end.value, floor(delta/days_between_new_subject_enrollment) + 1)
day_array = pd.to_datetime(day_array).date

# make identity plot
identity_plot = go.Figure(
    data=go.Scatter(
        x=day_array,
        y=[n for n in range(1, len(day_array) + 1)],
        mode='lines+markers',
        line={
            'color': 'black',
            'shape': 'hv'
        },
        marker={
            'color': 'black',
            'size': 1.0
        }
        ,
        name='Predicted Progress'
    )
)

identity_plot.update_layout(
    title={
        'text': 'Visit Progress Timeline',
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title={
        'text': 'Date',
        # 'font': '',
        # 'standoff': ''
    },
    yaxis_title={
        'text': 'Number of Subjects',
        # 'font': '',
        # 'standoff': ''
    },
    legend={
        'title': {
            'text': 'Visits'
        }
    },
    showlegend=True
)

identity_plot.update_xaxes(
    showgrid=False,
    showspikes=True
    )

identity_plot.update_yaxes(
    showgrid=False,
    showspikes=True
    )

# add traces for each visit
for visit in visits:
    df, identity_plot = add_visit_trace_identity(identity_plot, df, visit)

# add a line to denote today's date
identity_plot = add_today_line(identity_plot, 'vertical')

# layout dash page
layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id='visit-progress-timeline',
                        figure=identity_plot
                    )
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id='subject-enrollment-timeline',
                        figure=gantt
                    )
                )
            ]
        )
    ]
)
