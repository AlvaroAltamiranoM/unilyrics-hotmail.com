# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:58:07 2019

@author: ALVAROALT
"""

#concatenate all csv files in folder:
import os
import pandas as pd

for path, subdirs, files in os.walk(r'C:\Users\ALVAROALT\Documents\Python Scripts\series'):
    for name in files:
        print(files)
combined_csv = pd.concat([pd.read_csv(f) for f in files],ignore_index = True)
combined_csv[['date', 'url_oferta', 'fecha_online', 'pais', 'cantidad_de_vacantes']].to_csv( "combined.csv", encoding='utf-8', index=False)



