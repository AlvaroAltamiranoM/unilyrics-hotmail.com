# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 20:38:30 2020

@author: unily
"""

#           http://127.0.0.1:8050/

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
from plotly.offline import plot
import random

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#server = app.server
#import vacantes_series
#Data
#data = pd.read_csv(r'combined_ready.csv', encoding='utf-8')


app.layout = html.Div(children=[
    html.H1(children='América Latina',
    style={'textAlign': 'center'
            }
    ),
    html.Div([
        dcc.Dropdown(
            id='xaxis-column',
            options=[{'label': i, 'value': i} for i in table3.pais.unique()],
            placeholder='Seleccione un País',
            value = 'Ecuador'),
            ],
            style={'width': '48%', 'display': 'inline',
                    'marginTop': '1em','marginBottom': '1em'}),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Log',
                labelStyle={'display': 'inline-block'}
            ),

    html.Div([
    dcc.Graph(id='graph1',
              style={'width': '48%', 'display': 'inline'}),
        
        ]),
    html.H3(children='*No todos los países cuentan con la variable de no. de vacantes por aviso. Aquí sólo se grafican el no. de avisos',
        style={'textAlign': 'center'
                },
),

    ])

@app.callback(
    Output('graph1', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-type', 'value')])

def update_graph(xaxis_column_name, yaxis_type):
    table_g = table3.loc[table3['pais']==xaxis_column_name]
    return {
            'data': [dict(
            x=table_g['semana'],
            y=table_g['conteo'],
            type='line',
        )],
        'layout': dict(
            xaxis={
                'title': 'País',
                'yanchor': 'top'},
            yaxis={
                'title': 'Número de postings*',
                'type': 'linear' if yaxis_type == 'Linear' else 'log'},
            title={
                'text': 'Vacantes en: <br>{}'.format(xaxis_column_name),
                'xanchor': 'auto',
                'y': 0.9})
        }

if __name__ == '__main__':
    app.run_server(debug=False)
