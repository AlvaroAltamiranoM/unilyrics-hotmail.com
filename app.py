#!/usr/bin/env python
# -*- coding: utf-8 -*-


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
#import vacantes_series
#Data
table3 = pd.read_csv(r'table3.csv', encoding='utf-8')
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
            
            dcc.Graph(id='graphregional2',
              style={'width': '48%', 'display': 'inline',
                     },
              config = {'displaylogo': False}),

        ]),

html.P(['Fuente: con base en datos descargados de Computrabajo e Infojobs.',
                ' Cada punto de datos corresponde al número de nuevos anuncios publicados por los portales de empleo en la semana particular. La lista desplegable de la próxima sección enumera los países incluidos.'],
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
                ' El número de plazas de empleo (vacantes) por anuncio individual se limita a un techo de 200.'],
                style={'color': 'black', 'fontSize': 10, 'marginBottom': 25, 'marginTop': 15, 'marginLeft': 65}),

        dcc.Graph(id='graph2',
            style={'width': '48%', 'display': 'inline-block', 'marginBottom': 0.01},
            config = {'displaylogo': False}),      
        dcc.Graph(id='graph4',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),
                   html.P(['Fuente: con base en datos descargados de Computrabajo e Infojobs.'],
                style={'width': '48%', 'display': 'inline-block', 'fontSize': 10, 'marginLeft': 35}),
                html.P(['Fuente: Google. ‡La línea base es el valor medio, para el día correspondiente de la semana, durante el período del 3 de enero al 6 de febrero de 2020.',\
                       ' Para más información, consultar: https://www.google.com/covid19/mobility/'],
                            style={'width': '48%', 'display': 'inline-block', 'fontSize': 10,  'marginBottom': 25, 'marginLeft': 5}),        
        
            html.Div([           
            dcc.Graph(id='graph3',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),
            dcc.Graph(id='graph5',
            style={'width': '48%', 'display': 'inline-block'},
            config = {'displaylogo': False}),
                     html.P(['Fuente: con base en datos descargados de Computrabajo e Infojobs.', '‡ Clasificación de ramas provista por el portal (no es CIIU). Solo ARG, CHL, y COL tienen información para esta variable.'],
                style={'width': '48%', 'display': 'inline-block', 'fontSize': 10, 'marginLeft': 35}),
                     html.P(['Fuente: con base en datos descargados de Computrabajo e Infojobs. ‡Durante el mes(es) y país seleccionado.'],
                            style={'width': '48%', 'display': 'inline-block', 'fontSize': 10, 'marginBottom': 25, 'marginLeft': 13}),
            ]),

            html.Div(["* Desarrollado en Python por ", html.A("Alvaro Altamirano Montoya", href='https://www.linkedin.com/in/%C3%A1lvaro-altamirano-montoya-b3857659/', target="_blank"),
                '. Las vacantes son descargadas continuamente mediante la librería BeautifulSoup, y posteriormente ordenadas en bases de datos relacionales de texto plano (csv).\
                       Estas bases de datos permiten la creación de los indicadores ilustrados en esta página. Solo se presentan datos de un portal por país.'
                          
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
        table1 = pd.read_csv(r'table1.csv', encoding='utf-8')
        data1 = go.Scatter(x=table1['semana'], y=table1['conteo'], name='Vacantes por semana',
                                 line=dict(color='royalblue', width=3), mode='lines')
        data2 =go.Scatter(x=table1['semana'], y=table1['conteo_MA'], name = 'Media móvil (3 semanas)',
                                 line=dict(color='black', width=2, dash='dot'), mode='lines')
        
        return {
        'data':  [data1, data2],
        'layout': dict(
        xaxis={
            'title': '',
            'yanchor': 'bottom', 'showline':True,'showgrid':False,'zeroline': False,
            'linewidth':1.5, 'linecolor':'black', 'showspikes':True},  
        yaxis={
            'title': 'Número en miles',
            'showline':True, 'showgrid':True,'zeroline': False,
            'linewidth':1.5, 'linecolor':'black', 'showspikes':True},
        title={
            'text': 'Nuevas vacantes publicadas en 17 países de América Latina',
            'xanchor': 'auto',
            'y': 0.9, 'x':0.07},
        legend = {
        'yanchor':'top',
        'y':0.97,
        'xanchor': "left",
        'x': 0.8
        } ), }

@app.callback(
    Output('graphregional2', 'figure'),
    [Input('xaxis-column', 'value')])

def update_graph02(data3):
        table0 = pd.read_csv(r'table0.csv', encoding='utf-8')
        fig = px.bar(table0, x="pais", y="growth", color='colorcol', 
                     color_discrete_map={'no': 'red', 'yes': '#1f77b4'},
                     template="simple_white",
                     title={'text': 'Variación % respecto al promedio de anuncios en enero-febrero',
                         'y': 0.9, 'x': 0.07})
            
        fig.update_layout(showlegend=False,
                        xaxis_title="",
                        yaxis_title="",
                        plot_bgcolor='rgba(0,0,0,0)')
        
        return  fig

        
@app.callback(
    Output('graph1', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-type', 'value')])

def update_graph(xaxis_column_name, yaxis_type):
    table4 = pd.read_csv(r'table4.csv', encoding='utf-8')
    table_g = table3.loc[table3['pais']==xaxis_column_name]
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
            'title': '',
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
    Output('graph2', 'figure'),
    [Input('xaxis-column', 'value')])

def update_graph2(xaxis_column_name):
    salarios = pd.read_csv(r'salarios.csv', encoding='utf-8')
    table_g = salarios.loc[salarios['pais']==xaxis_column_name]
    fig = px.line(table_g, x='semana', y='mean', 
                         title={'text': "Media salarial semanal de nuevos anuncios‡", 'x':0.5})

    fig.update_xaxes(showline=True, linewidth=1, linecolor='black', showspikes=True)
    aux = table_g['mean'].astype(int)
    low = aux*.60
    high = aux*1.45
    fig.update_yaxes(range=[low.min(),high.max()])
    
    fig.update_layout(
    xaxis_title="",
    yaxis_title="Moneda local corriente",
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
    google = pd.read_csv(r'google.csv', encoding='utf-8')
    google2 = google.loc[google['pais']==xaxis_column_name]
    area = px.area(google2, x="semana", y="workplaces_percent_change_from_baseline",
	       title={'text': "Tendencias de movilidad hacia lugares de trabajo", 'x':0.5},
           color_discrete_sequence=px.colors.sequential.Bluered)
    area.layout.showlegend = False
    area.update_layout(template="simple_white", 
                      xaxis_title="Semana (ISO 8601)",
                      yaxis_title="Cambio en relación con línea base (%)‡",
                      margin=dict(b=1, l=25))

    return area

@app.callback(
    Output('graph3', 'figure'),
    [Input('xaxis-column', 'value')])
        
def update_graph3(xaxis_column_name):
    rama_change = pd.read_csv(r'rama_change.csv', encoding='utf-8')
    if xaxis_column_name == 'Argentina' or xaxis_column_name == 'Chile' or xaxis_column_name == 'Colombia':
        table_rama = rama_change.loc[rama_change['pais']==xaxis_column_name].\
        sort_values(by='growth', ascending=False)
        fig = px.bar(table_rama, y='rama_de_actividad', x='growth', orientation='h',
                 template="simple_white", height=450, text='rama_de_actividad',
                  title={'text': 'Sectores de mayor (de)crecimiento % respecto a febrero-marzo',
                         'xanchor': 'center',
                         'y': 0.9, 'x': 0.5})

        fig.update_layout(showlegend=True, uniformtext_minsize=14, uniformtext_mode=False)
        fig.update_traces(textposition='inside')
    
        fig.update_layout(
        xaxis_title="variación porcentual (%)",
        yaxis_title="Ramas de actividad económica",
        yaxis={'showticklabels': False},
        plot_bgcolor='rgba(0,0,0,0)')
        
        fig.update_traces(marker_color='#1f77b4', marker_line_color='black',
                      marker_line_width=1, opacity=0.92)
        return fig
    else:
        return {}

    

@app.callback(
    Output('graph5', 'figure'),
    [Input('xaxis-column', 'value')])
        
def update_graph5(xaxis_column_name):
    rama_change_2 = pd.read_csv(r'rama_change_2.csv', encoding='utf-8')
    if xaxis_column_name == 'Argentina' or xaxis_column_name == 'Chile' or xaxis_column_name == 'Colombia':
        table_rama_2 = rama_change_2.loc[rama_change_2['pais']==xaxis_column_name].\
        sort_values(by='growth', ascending=False)
        
        fig = px.bar(table_rama_2, y='rama_de_actividad', x='growth', orientation='h',
                 template="simple_white", height=450, text='rama_de_actividad',
                  title={'text': 'Sectores de mayor (de)crecimiento % respecto al mes anterior',
                         'xanchor': 'center',
                         'y': 0.9, 'x': 0.5})

        fig.update_layout(showlegend=True, uniformtext_minsize=14, uniformtext_mode=False)
        fig.update_traces(textposition='inside')
    
        fig.update_layout(
        xaxis_title="variación porcentual (%)",
        yaxis_title="Ramas de actividad económica",
        yaxis={'showticklabels': False},
        plot_bgcolor='rgba(0,0,0,0)')
        
        fig.update_traces(marker_color='#1f77b4', marker_line_color='black',
                      marker_line_width=1, opacity=0.92)
        return fig
    
    else:
        return {}
    

if __name__ == '__main__':
    app.run_server(debug=False)


