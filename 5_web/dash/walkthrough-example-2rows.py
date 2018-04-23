import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# initialize app
app = dash.Dash()

app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})  # noqa: E501
# try enter the cdn link above ; and check configuration
# this layout can take up to total of 12columns (important !!)


# declare layout
app.layout = html.Div(
    html.Div([                  # seperate division on each elements

            html.Div([
                html.H1(children = 'Hello World'),

                html.Div(children = '''
                    Dash : A web application framework for Python.
                '''),
            ], className='row'),  #className : setting header as a row of CSS division

        html.Div([
            html.Div([    # add another nested div on each graph
                dcc.Graph(
                    # graph 1
                    id='example-graph-1',
                    figure={
                        'data': [
                            {'x' : [1, 2, 3], 'y' : [4, 1, 2], 'type':'bar', 'name':'SF'},
                            {'x' : [1, 2, 3], 'y' : [2, 4, 5], 'type':'bar', 'name':u'Montréal'},
                        ],
                        'layout' : {

                            # label axis
                            'title' : 'Dash Data Visualization',
                            'xaxis' : dict(
                                title='x Axis',
                                titlefront=dict(
                                family = 'Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='y Axis',
                                titlefront=dict(
                                family= 'Helectiva, monospace',
                                size=30,
                                color='#7f7f7f'
                            ))
                        }
                        }
                )], className='eight columns'  # vertical seperation !
                ),                           # six columns ... sort of like the size of the width
                                             # we can also try eight / and set the second one as four
                                             # total 12 :)

            # graph 2 (now we have two grapsh here !)
            html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x' : [1, 2, 3], 'y' : [4, 1, 2], 'type':'line', 'name':'SF'},
                            {'x' : [1, 2, 3], 'y' : [2, 4, 5], 'type':'line', 'name':u'Montréal'},
                        ],
                        'layout' : {

                            # label axis
                            'title' : 'Dash Data Visualization',
                            'xaxis' : dict(
                                title='x Axis',
                                titlefront=dict(
                                family = 'Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='y Axis',
                                titlefront=dict(
                                family= 'Helectiva, monospace',
                                size=30,
                                color='#7f7f7f'
                            ))
                        }

                    }
                )
            ], className='four columns'),
        ], className='row',), # setting graphs as second row of CSS division

        # second row
        html.Div([
            html.Div([    # add another nested div on each graph
                dcc.Graph(
                    # graph 1
                    id='example-graph-3',
                    figure={
                        'data': [
                            {'x' : [1, 2, 3], 'y' : [4, 1, 2], 'type':'bar', 'name':'SF'},
                            {'x' : [1, 2, 3], 'y' : [2, 4, 5], 'type':'bar', 'name':u'Montréal'},
                        ],
                        'layout' : {

                            # label axis
                            'title' : 'Dash Data Visualization',
                            'xaxis' : dict(
                                title='x Axis',
                                titlefront=dict(
                                family = 'Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='y Axis',
                                titlefront=dict(
                                family= 'Helectiva, monospace',
                                size=30,
                                color='#7f7f7f'
                            ))
                        }
                        }
                )], className='four columns'  # vertical seperation !
                ),                           # six columns ... sort of like the size of the width
                                             # we can also try eight / and set the second one as four
                                             # total 12 :)

            # graph 2 (now we have two grapsh here !)
            html.Div([
                dcc.Graph(
                    id='example-graph-4',
                    figure={
                        'data': [
                            {'x' : [1, 2, 3], 'y' : [4, 1, 2], 'type':'line', 'name':'SF'},
                            {'x' : [1, 2, 3], 'y' : [2, 4, 5], 'type':'line', 'name':u'Montréal'},
                        ],
                        'layout' : {

                            # label axis
                            'title' : 'Dash Data Visualization',
                            'xaxis' : dict(
                                title='x Axis',
                                titlefront=dict(
                                family = 'Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='y Axis',
                                titlefront=dict(
                                family= 'Helectiva, monospace',
                                size=30,
                                color='#7f7f7f'
                            ))
                        }

                    }
                )
            ], className='eight columns'),
        ], className='row',)
    ])
    )



if __name__ == '__main__':
    app.run_server(debug=True)
