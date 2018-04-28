# default setup for dashapp
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# datareader
import pandas_datareader.data as web
import datetime

app = dash.Dash()

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()

stock = 'TSLA'
df = web.DataReader(stock, 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

# print(df.index, df.Close)



app.layout = html.Div(children=[

    html.H1(children='Dash Tutorial pt.3'),

    html.Div(children='''
        Plots by input!
    '''),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')

    # dcc.Graph(
    #     id='example-graph',
    #     figure={
    #         'data': [
    #             {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
    #         ],
    #         'layout': {
    #             'title': stock
    #         }
    #     }
    # )
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
    )
def update_graph(input_data):

    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'morningstar', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df = df.drop("Symbol", axis=1)

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df['Close'], 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)
