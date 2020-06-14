#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly
import plotly.graph_objs as go
import random
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
#import vacantes_series
#Data
table1 = pd.read_csv(r'table1.csv', encoding='utf-8')
table3 = pd.read_csv(r'table3.csv', encoding='utf-8')
table4 = pd.read_csv(r'table4.csv', encoding='utf-8')
ramas = pd.read_csv(r'ramas.csv', encoding='utf-8')
salarios = pd.read_csv(r'salarios.csv', encoding='utf-8')
google = pd.read_csv(r'google.csv', encoding='utf-8')
anuncios_empresa = pd.read_csv(r'empresa.csv', encoding='utf-8')

app.title = 'Observatorio de vacantes'



app.layout = html.Div(children=[
    html.H1(children='América Latina',
    style={'textAlign': 'center', 'marginTop': '2em',
                                'marginBottom': '1em','display': 'block',
                                'borderTop': '1px solid #d6d6d6',
                                'borderBottom': '1px solid #d6d6d6',
                                'backgroundColor': '#1f77a1',
                                'color': 'white',
                                'padding': '10px'}
    ),
    html.H3(children='Observatorio de vacantes de empleo *',
        style={'textAlign': 'center'
                },
),
    
    html.Div([
            dcc.Graph(id='graphregional',
              style={'width': '48%', 'display': 'inline',
                     },
              config = {'displaylogo': False}),
        ]),

html.P(['Fuente: con base en datos descargados de Computrabajo e Infojobs.',
                ' Cada punto de datos corresponde al número de nuevos anuncios publicados por los portales de empleo en la semana particular.'],
                style={'color': 'black', 'fontSize': 10, 'marginBottom': 25, 'marginTop': 15, 'marginLeft': 65}),
        
    html.Div([
            html.Div([html.P("La siguiente sección presenta indicadores de vacantes para 17 países de América Latina",
                         style={'marginTop': '2em',
                                'marginBottom': '1em','display': 'block',
                                'borderTop': '1px solid #d6d6d6',
                                'borderBottom': '1px solid #d6d6d6',
                                'backgroundColor': '#1f77a1',
                                'color': 'white',
                                'padding': '10px'})]),
                      
            html.Div([html.P("Seleccione un país:",
                         style={'marginTop': '1em','marginBottom': '1em',
                                'display': 'inline-block'})]),
    html.Div([
        dcc.Dropdown(
            id='xaxis-column',
            options=[{'label': i, 'value': i} for i in table3.pais.unique()],
            placeholder='Seleccione un País',
            value = 'Argentina'),
            ],
            style={'width': '20%', 'display': 'inline',
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
        html.P(['Fuente: con base en datos descargados de Computrabajo e Infojobs.',' †No todos los países cuentan con la variable de no. de vacantes por aviso.',
                ' Cada punto de datos corresponde al número de nuevos anuncios (y/o vacantes) publicadas por los portales de empleo en la semana particular.',
                ' El número de plazas de empleo (vacantes) por anuncio individual se limita a un techo de 300.'],
                style={'color': 'black', 'fontSize': 10, 'marginBottom': 25, 'marginTop': 15, 'marginLeft': 65}),

        dcc.Graph(id='graph2',
            style={'width': '48%', 'display': 'inline-block', 'marginBottom': 0.01},
            config = {'displaylogo': False}),      
        dcc.Graph(id='graph4',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),
                   html.P(['Fuente: con base en datos descargados de Computrabajo e Infojobs.', html.Br(),'‡Para cada país, se calcula la mediana al interior de cada mes'],
                style={'width': '48%', 'display': 'inline-block', 'fontSize': 10, 'marginLeft': 35}),
                html.P(['Fuente: Google. ‡La línea base es el valor medio, para el día correspondiente de la semana, durante el período del 3 de enero al 6 de febrero de 2020.',\
                       ' Para más información, consultar: https://www.google.com/covid19/mobility/'],
                            style={'width': '48%', 'display': 'inline-block', 'fontSize': 10,  'marginBottom': 25, 'marginLeft': 5}),        
        
        html.Div([html.P("Seleccione un mes o grupo de meses:",
                         style={'marginTop': '2em','marginBottom': '1em',
                                'display': 'inline-block'})]),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in ramas.fecha_online.unique()],
                placeholder='Seleccione un mes',
                value = ['Enero', 'Febrero', 'Marzo','Abril','Mayo', 'Junio'],
                multi =True),
                ],
                 style={'width': '48%', 'display': 'inline',
                        'marginTop': '1em','marginBottom': '1em'}),
            html.Div([           
            dcc.Graph(id='graph3',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),
            dcc.Graph(id='graph5',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),
                     html.P(['Fuente: con base en datos descargados de Computrabajo e Infojobs. ‡Distribución de nuevas vacantes durante el mes(es) y país seleccionado.',' Clasificación de ramas provista por el portal (no es CIIU). Solo ARG, CHL, y COL tienen info para esta variable.'],
                style={'width': '48%', 'display': 'inline-block', 'fontSize': 10, 'marginLeft': 35}),
                     html.P(['Fuente: con base en datos descargados de Computrabajo e Infojobs. ‡Durante el mes(es) y país seleccionado.'],
                            style={'width': '48%', 'display': 'inline-block', 'fontSize': 10, 'marginBottom': 25, 'marginLeft': 13}),
            ]),

            html.Div(["* Desarrollado en Python por: ",html.A("Alvaro Altamirano Montoya", href='https://www.linkedin.com/in/%C3%A1lvaro-altamirano-montoya-b3857659/?locale=en_US', target="_blank"),
                ' con base en datos descargados por ',
                html.A("Alvaro Altamirano Montoya", href='https://www.linkedin.com/in/%C3%A1lvaro-altamirano-montoya-b3857659/', target="_blank"),
                       ' y ', html.A("Roberto Sánchez Ávalos", href='https://www.linkedin.com/in/rsanchezavalos/', target="_blank"), '. Las vacantes son\
                       descargadas continuamente mediante la librería BeautifulSoup, y posteriormente ordenadas en bases de datos relacionales de texto plano (csv).\
                       Estas bases de datos permiten la creación de los indicadores presentados en esta página.'
            ], style={'marginTop': '2em',
                                'marginBottom': '1em','display': 'block',
                                'borderTop': '1px solid #d6d6d6',
                                'borderBottom': '1px solid #d6d6d6',
                                'backgroundColor': '#1f77a1',
                                'color': 'white',
                                'padding': '10px'}),

], style={'marginTop': '2em','marginBottom': '1em','marginLeft': 5, 'marginRight': 5
                                })
])


@app.callback(
    Output('graphregional', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-type', 'value')])

def update_graph0(data1, data2):

        data1 = go.Scatter(x=table1['semana'], y=table1['conteo'], name='Vacantes por semana',
                                 line=dict(color='royalblue', width=3), mode='lines')
        data2 =go.Scatter(x=table1['semana'], y=table1['conteo_MA'], name = 'Media móvil (3 semanas)',
                                 line=dict(color='black', width=2, dash='dot'), mode='lines')
        
        return {
        'data':  [data1, data2],
        'layout': dict(
        xaxis={
            'title': 'Semana (ISO 8601)',
            'yanchor': 'bottom', 'showline':True,'showgrid':False,'zeroline': False,
            'linewidth':1.5, 'linecolor':'black', 'showspikes':True},  
        yaxis={
            'title': 'Número†',
            'showline':True, 'showgrid':True,'zeroline': False,
            'linewidth':1.5, 'linecolor':'black', 'showspikes':True},
        title={
            'text': 'Nuevas vacantes publicadas en 17 países de América Latina',
            'xanchor': 'auto',
            'y': 0.9, 'x':0.01}) }

        
@app.callback(
    Output('graph1', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-type', 'value')])

def update_graph(xaxis_column_name, yaxis_type):
    table_g = table3.loc[table3['pais']==xaxis_column_name]
    #table_g['conteo_MA']= table_g['conteo'].rolling(window=3).mean()
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
            'title': 'Número†',
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
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value')])
        
def update_graph3(xaxis_column_name, year_value):
    if xaxis_column_name == 'Argentina' or xaxis_column_name == 'Chile' or xaxis_column_name == 'Colombia':
        table_rama = ramas.loc[(ramas['pais']==xaxis_column_name) & ramas['fecha_online'].
                        isin(year_value)].sort_values(by='conteo', ascending=False)
    else:
        table_rama=[]

    fig = px.treemap(table_rama, path=['rama_de_actividad'], values='conteo',
                  color='conteo', hover_data=['rama_de_actividad'],
                  color_continuous_scale='Greens',
                  title = {'text':'Distribución de ramas de actividad‡', 'x':0.5})
    
    fig.update_layout(margin=dict(b=5, l=30), height=430)
    
    return  fig


@app.callback(
    Output('graph2', 'figure'),
    [Input('xaxis-column', 'value')])

def update_graph2(xaxis_column_name):
    table_g = salarios.loc[salarios['pais']==xaxis_column_name]
    fig = px.bar(table_g, x='fecha_online', y='url_oferta', 
                    color="median",
                         title={'text': "Nuevos anuncios según categoría salarial‡", 'x':0.5})

    fig.update_xaxes(showline=True, linewidth=1, linecolor='black', showspikes=True)
    fig.update_yaxes(showspikes=True, showline=True, linewidth=1, linecolor='black')

    fig.update_layout(
    xaxis_title="",
    yaxis_title="Número de anuncios",
    plot_bgcolor='rgba(0,0,0,0)',
    legend_title_text='',
    margin=dict(b=0.1),
    barmode='group',
    legend_orientation="h", 
       legend=dict(
       font=dict(
            family="sans-serif",
            size=11,
            color="black"
        )))

    return  fig

@app.callback(
    Output('graph4', 'figure'),
    [Input('xaxis-column', 'value')])

def update_graph4(xaxis_column_name):
    google2 = google.loc[google['pais']==xaxis_column_name]
    area = px.area(google2, x="semana", y="workplaces_percent_change_from_baseline",
	       title={'text': "Tendencias de movilidad hacia lugares de trabajo", 'x':0.5},
           color="workplaces_percent_change_from_baseline",
           color_discrete_sequence= px.colors.sequential.thermal)
    area.layout.showlegend = False
    area.update_layout(template="simple_white", 
                      xaxis_title="Semana (ISO 8601)",
                      yaxis_title="Cambio en relación con línea base (%)‡",
                      margin=dict(b=1, l=25))

    return area

@app.callback(
    Output('graph5', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value')])
        
def update_graph5(xaxis_column_name, year_value):
    table3 = anuncios_empresa.loc[(anuncios_empresa['pais']==xaxis_column_name) & anuncios_empresa['fecha_online'].\
                                  isin(year_value)].sort_values(by='conteo', ascending=False)
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
                                                title={'text': "15 empresas con más anuncios‡",'y':0.9,'x':0.5, 'xanchor': 'center','yanchor': 'top'},
                                                height=425, width=650,
                                                margin=dict(b=5, l=80))
            }



if __name__ == '__main__':
    app.run_server(debug=False)




