# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:06:03 2020

@author: ALVAROALT
"""
import pandas as pd
import numpy as np
import locale
locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')
from datetime import datetime as dt

#Data
data = pd.read_csv(r'combined.csv')
data = data.drop_duplicates('url_oferta')

data['date_aux'] = ''
data['date_aux'] = data['fecha_online'].str.extract('((Hoy)|(Ayer))')
data['date_aux_2'] = ''
data['date_aux_2'] = data['fecha_online'].str.extract('((octubre)|(noviembre)|(diciembre))')
data.loc[data['date_aux'] =="Hoy", 'fecha_online'] = np.nan
data.loc[data['date_aux'] =="Ayer", 'fecha_online'] = np.nan

data['fecha_online'] = pd.to_datetime(data['fecha_online'],format='%d %B', errors='coerce')
data['fecha_online'] = data['fecha_online'].dt.date
data['fecha_online'] = data['fecha_online'].apply(lambda x:x.replace(year=2020))

data['fecha_online']= data['fecha_online'].astype(str)

data.loc[(data['date_aux_2'] =="diciembre") | (data['date_aux_2'] =="noviembre") | (data['date_aux_2'] =="octubre"),\
         'fecha_online'] = data['fecha_online'].str.replace('2020','2019')

data.loc[data['date_aux'] =="Ayer", 'fecha_online'] = data['date']
#Por ahora ayer y hoy se transforma a la data de descarga, luego hay que ver como componer ese slices
#hoy = int(data['date'][1][-2:])-1
#ayer= int(data['date'][1][-2:])-2

data.loc[(data['date_aux'] =="Hoy") | (data['date_aux'] =="Ayer"), 'fecha_online'] = data['date']

data['date']= pd.to_datetime(data['date']) 
data['fecha_online']= pd.to_datetime(data['fecha_online']) 

###########################
#GRAFICANDO
###########################
#data['fecha_online_w'] = pd.to_datetime(data['fecha_online']) - pd.to_timedelta(7, unit='d')
#table = data.groupby(['fecha_online']).size().reset_index().rename(columns={0:'conteo'})
#Create grouped data

table3 = data.groupby([data.fecha_online.dt.strftime('%W'), data.pais]).size().reset_index().rename(columns={0:'conteo'})
del data
#table3.loc[table3['fecha_online'] =="NaT", 'fecha_online'] = np.nan

table3['fecha_online'] = pd.to_numeric(table3['fecha_online'], errors='coerce')

table3 = table3.loc[table3['fecha_online'] < 20]


#Import week names labels
weeks = pd.read_csv(r'semanas_iso.csv')
weeks['fecha_online']=  weeks.index
table3 = table3.merge(weeks, how="left", on="fecha_online")
del weeks

table3['pais'] = table3['pais'].replace({'co': 'Colombia', 'pe': 'Perú', 'ni': 'Nicaragua',
      'bo': 'Bolivia', 'py':'Paraguay','do':'Rep. Dominicana','gt':'Guatemala',
      'sv':'El Salvador','pa':'Panamá','cr':'Costa Rica','hn':'Honduras','bra':'Brasil',
      'uy':'Uruguay','ar':'Argentina','cl':'Chile','ve':'Venezuela', 'ec':'Ecuador'})

