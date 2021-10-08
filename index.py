# dash imports
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# other imports
# from threading import Timer

# local imports
from app import app
from apps import (home,
                  enrollment,
                  demographics,
                  cognition,
                  ogtt_mri,
                  cvr,
                  inflammation,
                  mri,
                  test_retest,
                  compliance)


# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("Enrollment Data", href="/enrollment"),
        dbc.DropdownMenuItem("Demographic Data", href="/demographics"),
        dbc.DropdownMenuItem("Cognition Data", href="/cognition"),
        dbc.DropdownMenuItem("OGTT-MRI Data", href="/ogtt_mri"),
        dbc.DropdownMenuItem("Cerebrovascular Reactivity Data", href="/cvr"),
        dbc.DropdownMenuItem("Inflammatory Data", href="/inflammation"),
        dbc.DropdownMenuItem("Structural MRI Data", href="/mri"),
        dbc.DropdownMenuItem("Test-Retest Data", href="/test_retest"),
        dbc.DropdownMenuItem("Compliance Data", href="/compliance"),
    ],
    nav=True,
    in_navbar=True,
    label="Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo/brand
                dbc.Row(
                    [
                        # dbc.Col(html.Img(src="/assets/virus.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("IRB 2019-0361 Clinical Trial Dashboard", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content'),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/enrollment':
        return enrollment.layout
    elif pathname == '/demographics':
        return demographics.layout
    elif pathname == '/cognition':
        return cognition.layout
    elif pathname == '/ogtt_mri':
        return ogtt_mri.layout
    elif pathname == '/cvr':
        return cvr.layout
    elif pathname == '/inflammation':
        return inflammation.layout
    elif pathname == '/mri':
        return mri.layout
    elif pathname == '/test_retest':
        return test_retest.layout
    elif pathname == '/compliance':
        return compliance.layout
    else:
        return home.layout


# def open_browser():
#     webbrowser.open_new(f"http://localhost:{port}")


if __name__ == '__main__':
    # Timer(1, open_browser).start()
    app.run_server(host='127.0.0.1', port=8080, debug=True)
