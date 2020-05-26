#!/usr/bin/env python
# -*- coding: utf-8 -*-


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
import random
import plotly.express as px
from plotly.subplots import make_subplots


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
#import vacantes_series
#Data
table3 = pd.read_csv(r'table3.csv', encoding='utf-8')
table4 = pd.read_csv(r'table4.csv', encoding='utf-8')
ramas = pd.read_csv(r'ramas.csv', encoding='utf-8')
salarios = pd.read_csv(r'salarios.csv', encoding='utf-8')
google = pd.read_csv(r'google.csv', encoding='utf-8')
anuncios_empresa = pd.read_csv(r'empresa.csv', encoding='utf-8')

app.title = 'Observatorio de vacantes'


app.layout = html.Div(children=[
    html.H1(children='América Latina',
    style={'textAlign': 'center', 
            }
    ),
    html.H3(children='Observatorio de vacantes de empleo',
        style={'textAlign': 'center'
                },
),
    html.Div([
        dcc.Dropdown(
            id='xaxis-column',
            options=[{'label': i, 'value': i} for i in table3.pais.unique()],
            placeholder='Seleccione un País',
            value = 'Argentina'),
            ],
            style={'width': '48%', 'display': 'inline',
                    'marginTop': '1em','marginBottom': '1em'}),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Lineal', 'Log']],
                value='Lineal',
                labelStyle={'display': 'inline-block'}
            ),

    html.Div([
            dcc.Graph(id='graph1',
              style={'width': '48%', 'display': 'inline'},
              config = {'displaylogo': False}),
        
        ]),
        html.P(['*No todos los países cuentan con la variable de no. de vacantes por aviso.' , html.Br(),'Fuente: con base en datos descargados de Computrabajo e Infojobs.'],
                style={'color': 'black', 'fontSize': 10, 'marginBottom': 25, 'marginTop': 15, 'marginLeft': 65}),

         dcc.Graph(id='graph2',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),          
        dcc.Graph(id='graph3',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),
                   html.P(['**Acumulado del año. Se limitan salarios con distancia menor a 2.2 desviaciones estándar de la media.', html.Br(),'Fuente: con base en datos descargados de Computrabajo e Infojobs.'],
                style={'width': '48%', 'display': 'inline-block', 'fontSize': 10, 'marginTop': 10, 'marginBottom': 25, 'marginLeft': 35}),
                  html.P(['**Acumulado del año. Clasificación de ramas provista por el portal (not CIIU). Solo ARG, CHL, y COL tienen info para esta variable.', html.Br(),'Fuente: con base en datos descargados de Computrabajo e Infojobs.'],
                style={'width': '48%', 'display': 'inline-block', 'fontSize': 10}),
        
        html.Div([
            dcc.Graph(id='graph4',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),
            dcc.Graph(id='graph5',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),
                     html.P('Fuente: https://www.google.com/covid19/mobility/',
                            style={'width': '48%', 'display': 'inline-block', 'fontSize': 10,  'marginBottom': 25, 'marginLeft': 35}),
                     html.P(['**Acumulado del año.', html.Br(), 'Fuente: con base en datos descargados de Computrabajo e Infojobs.'],
                            style={'width': '48%', 'display': 'inline-block', 'fontSize': 10}),
            ]),

            html.Div([
                html.P("Desarrollado en Python por:"),
                html.A("Alvaro Altamirano Montoya", href='https://www.linkedin.com/in/%C3%A1lvaro-altamirano-montoya-b3857659/?locale=en_US', target="_blank"),
                html.Br(),
                html.A("@ALVARODW", href='https://twitter.com/ALVARODW', target="_blank")
            ])
])


@app.callback(
    Output('graph1', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-type', 'value')])

def update_graph(xaxis_column_name, yaxis_type):
    table_g = table3.loc[table3['pais']==xaxis_column_name]
    table_g['conteo_MA']= table_g['conteo'].rolling(window=3).mean()
    table_g2 = table4.loc[table4['pais']==xaxis_column_name]
    
    if xaxis_column_name == 'Argentina' or xaxis_column_name == 'Chile' or xaxis_column_name == 'Colombia':
        data1 = go.Scatter(x=table_g['semana'], y=table_g['conteo'], name='Vacantes por semana',
                                 line=dict(color='royalblue', width=3), mode='lines')
        data2 =go.Scatter(x=table_g['semana'], y=table_g['conteo_MA'], name = 'Media móvil (3 semanas)',
                                 line=dict(color='black', width=2, dash='dot'), mode='lines')
        
        return {
        'data':  [data1, data2],
        'layout': dict(
        xaxis={
            'title': 'Semana (ISO 8601)',
            'yanchor': 'bottom', 'showline':True,'showgrid':False,'zeroline': False,
            'linewidth':1.5, 'linecolor':'black', 'showspikes':True},  
        yaxis={
            'title': 'Número*',
            'type': 'linear' if yaxis_type == 'Lineal' else 'log',
            'showline':True, 'showgrid':True,'zeroline': False,
            'linewidth':1.5, 'linecolor':'black', 'showspikes':True},
        title={
            'text': 'Nuevas vacantes en: <br>{}'.format(xaxis_column_name),
            'xanchor': 'auto',
            'y': 0.9}) }

        
    else:
        # Create and style traces
        data1 = go.Scatter(x=table_g['semana'], y=table_g['conteo'], name='Vacantes por semana',
                                 line=dict(color='royalblue', width=3), mode='lines')
        data2 =go.Scatter(x=table_g['semana'], y=table_g['conteo_MA'], name = 'Media móvil (3 semanas)',
                                 line=dict(color='black', width=2, dash='dot'), mode='lines')
        data3 =go.Scatter(x=table_g2['semana'], y=table_g2['conteo'], name = 'Anuncios por semana',
                                 line=dict(color='green', width=3, dash='dot'), mode='lines')
    
        return {
                'data':  [data1, data2, data3],
            'layout': dict(
                xaxis={
                    'title': 'Semana (ISO 8601)',
                    'yanchor': 'bottom', 'showline':True,'showgrid':False,'zeroline': False,
                    'linewidth':1.5, 'linecolor':'black', 'showspikes':True},  
                yaxis={
                    'title': 'Número*',
                    'type': 'linear' if yaxis_type == 'Lineal' else 'log',
                    'showline':True, 'showgrid':True,'zeroline': False,
                    'linewidth':1.5, 'linecolor':'black', 'showspikes':True},
                title={
                    'text': 'Nuevas vacantes en: <br>{}'.format(xaxis_column_name),
                    'xanchor': 'auto',
                    'y': 0.9}) }
        
@app.callback(
    Output('graph3', 'figure'),
    [Input('xaxis-column', 'value')])

def update_graph3(xaxis_column_name):
    if xaxis_column_name == 'Argentina' or xaxis_column_name == 'Chile' or xaxis_column_name == 'Colombia':
        table_rama = ramas.loc[ramas['pais']==xaxis_column_name]
    else:
        table_rama=[]

    return px.treemap(table_rama, path=['rama_de_actividad'], values='conteo',
                  color='conteo', hover_data=['rama_de_actividad'],
                  color_continuous_scale='Greens',
                  title = {'text':'Distribución de ramas de actividad**', 'x':0.5}
                  )

@app.callback(
    Output('graph2', 'figure'),
    [Input('xaxis-column', 'value')])

def update_graph2(xaxis_column_name):
    table_salarios = salarios.loc[salarios['pais']==xaxis_column_name]
    table_salarios = table_salarios[~(np.abs(table_salarios.salario-table_salarios.salario.mean()) > (2.2*table_salarios.salario.std()))]
    if xaxis_column_name=='Colombia':
        table_salarios = table_salarios[table_salarios['salario']>600000]
    if xaxis_column_name=='Chile':
        table_salarios = table_salarios[table_salarios['salario']>100000]
    
    
    fig = px.histogram(table_salarios, x="salario",marginal='box',nbins=20,
                         title={'text': "Histograma y Boxplot de la distribución salarial**", 'x':0.5},
                         color_discrete_sequence=px.colors.qualitative.Safe,
                         template="simple_white",
                         )

    fig.update_layout(template="simple_white", 
                      xaxis_title="Salario mensual en moneda local nominal",
                      yaxis_title="Densidad"
                      )
    return fig  


@app.callback(
    Output('graph4', 'figure'),
    [Input('xaxis-column', 'value')])

def update_graph4(xaxis_column_name):
    google2 = google.loc[google['pais']==xaxis_column_name]
    area = px.area(google2, x="semana", y="workplaces_percent_change_from_baseline",
	       title={'text': "Google's 'Tendencias de movilidad hacia lugares de trabajo'", 'x':0.5},
           color="workplaces_percent_change_from_baseline",
           color_discrete_sequence= px.colors.sequential.thermal)
    area.layout.showlegend = False
    area.update_layout(template="simple_white", 
                      xaxis_title="Semana (ISO 8601)",
                      yaxis_title="Cambio en relación con línea base (%)"
                      )

    return area

@app.callback(
    Output('graph5', 'figure'),
    [Input('xaxis-column', 'value')])
        
def update_graph5(xaxis_column_name):
    table3 = anuncios_empresa.loc[anuncios_empresa['pais']==xaxis_column_name].sort_values(by='conteo', ascending=False)
    table3.loc[table3['conteo']>20,'conteo']=20
    colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(30)]

    data = go.Scatter(
    x=[random.random() for i in range(30)],
    y=random.choices(range(30), k=15),
    mode='text',
    text=table3['empresa'][~(table3['empresa'].str.len() <4)].unique(),
    marker={'opacity': 0.3},
    textfont={'size': table3['conteo'],
   'color': colors})

    return {'data': [data],'layout' : go.Layout(xaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False, 'showline':True, 'mirror':True},
                                                yaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False, 'showline':True, 'mirror':True},
                                                title={'text': "15 empresas con más anuncios**",'y':0.9,'x':0.5, 'xanchor': 'center','yanchor': 'top'})
            }

    table3 = anuncios_empresa.loc[anuncios_empresa['pais']=='Colombia'].sort_values(by='conteo', ascending=False)



if __name__ == '__main__':
    app.run_server(debug=False)



