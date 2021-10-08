# import dash_core_components as dcc
import dash_html_components as html
# from dash.dependencies import Input, Output

# from app import app


def get_study_synopsis():
    return '[synopsis]'


def get_inclusion_criteria():
    lst = html.Ul([])
    criteria = [
        'Item 1',
        'Item 2'
    ]

    for item in criteria:
        lst.children.append(html.Li(item))
    return lst


def get_exclusion_criteria():
    lst = html.Ul([])
    criteria = [
        'Item 1',
        'Item 2'
    ]

    for item in criteria:
        lst.children.append(html.Li(item))
    return lst


def get_aims():
    lst = html.Ol([])
    aims = [
        'Aim 1',
        'Aim 2',
        'Aim 3',
        'Aim 4'
    ]

    for item in aims:
        lst.children.append(html.Li(item))
    return lst


def get_analysis_statistics_plan():
    lst = html.Ol([])
    plan = [
        'Aim 1',
        'Aim 2',
        'Aim 3',
        'Aim 4'
    ]

    for item in plan:
        lst.children.append(html.Li(item))
    return lst


layout = html.Div([

    # study synopsis
    html.Div(
        children=[
            html.H2('Synopsis'),
            html.P(get_study_synopsis())
        ]
    ),

    # aims
    html.Div(
        children=[
            html.H2('Aims'),
            get_aims()
        ]
    ),

    # eligibility criteria
    html.Div(
        children=[

            # main section header
            html.H2('Eligibility Criteria'),

            # inclusion criteria section
            html.H3('Inclusion Criteria'),
            get_inclusion_criteria(),

            # exclusion criteria section
            html.H3('Exclusion Criteria'),
            get_exclusion_criteria()
        ]
    ),

    # stats overview
    html.Div(
        children=[
            html.H2('Data Analysis and Statistics'),
            get_analysis_statistics_plan()
        ]
    )
])


# callbacks
# no callbacks for this app/page
# TODO: add links to detailed analysis pipelines, MOP, etc.?
