#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 09:37:46 2018

@author: ksingh
"""

from geopy.geocoders import Nominatim
import pandas as pd

neighbourhood = pd.read_csv('Data.csv')

title = neighbourhood['Title']
title.astype(str)
title.to_frame(name=None)

geolocator = Nominatim()
location = geolocator.geocode(title[1], timeout=200)
print (location, location.latitude, location.longitude)
   
def eval_results(x):
    try:
        return(x.latitude, x.longitude)
    except:
        return(None, None)
        

df = pd.DataFrame(title)
 

df['coordinates'] = df['Title'].apply(geolocator.geocode, timeout = 1000).apply(lambda x: eval_results(x))


df.to_csv('coordinates.csv', index=False)




