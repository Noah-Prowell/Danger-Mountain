import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('ggplot')

av_df = pd.read_csv('avalanche_data_set.csv', delimiter=';')
av_df.set_index('no', inplace=True)
pd.set_option('display.max_columns', None)
av_df['date_release'] = pd.to_datetime(av_df['date_release'])
av_df['snow_type']=av_df['snow_type'].astype('category') 
av_df['trigger_type'] = av_df['trigger_type'].astype('category') 

def get_two_columns(a, col1, col2):
    df = a[[col1, col2]]
    return df

"""Idea: 3D graph the verticle data of 20 random avalanches in a circle 
around a central point, the min height point will be pivoted out according to the ascpect degree
then color each line and point to the level of danger corresponding with the avalanche"""


# Regression 1: If the  aspect degrees is greater than 90 then the area of the avalanche will be greater than below 90
aspect_degrees_area = get_two_columns(av_df, 'aspect_degrees', 'area_m2')
aspect_degrees_area.dropna(inplace=True)
""" 
H0: aspect_degrees > 90  
HA: aspect_degrees < 90
"""

