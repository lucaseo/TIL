import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go

# keeps maximum length
from collections import deque


X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=100 # millisecond 단위
            )
        ]
    )

@app.callback(Output('live-graph', 'figure'),
              events = [Event('graph-update', 'interval')]) # we want to update figure

def update_graph():
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(Y[-1]+(Y[-1]*random.uniform(-0.1, 0.1)))

    data = go.Scatter(
        x = list(X),
        y = list(Y),
        name = 'Scatter',
        mode = 'lines+markers'     #scatter에 선을 추가해서 line graph를 만들어줌 (plotly style)
        )

    return {'data'  : [data],
            'layout': go.Layout(xaxis = dict(range=[min(X), max(X)]),
                                yaxis = dict(range=[min(Y), max(Y)]),
                                )}


if __name__ == '__main__':
    app.run_server(debug=True)
