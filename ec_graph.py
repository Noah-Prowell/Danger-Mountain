import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import statsmodels.formula.api as smf
import statsmodels.graphics.gofplots as gplots
import seaborn as sns
plt.style.use('ggplot')

av_df = pd.read_csv('avalanche_data_set.csv', delimiter=';')
av_df.set_index('no', inplace=True)
pd.set_option('display.max_columns', None)
av_df['date_release'] = pd.to_datetime(av_df['date_release'])
av_df['snow_type']=av_df['snow_type'].astype('category') 
av_df['trigger_type'] = av_df['trigger_type'].astype('category') 

# Does a northward or southward facing mountain cause a larger avalanche area?
# aspect degree of 0 = pure north
# aspect degree of 180 = pure south


av_df['North_South'] = [math.cos(x) for x in av_df['aspect_degrees']]
av_df['West_East'] = [math.sin(x) for x in av_df['aspect_degrees']]
av_df['elev_diff'] = av_df['max_elevation_m'] - av_df['min_elevation_m']
