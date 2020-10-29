import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import statsmodels.formula.api as smf
import statsmodels.graphics.gofplots as gplots
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('ggplot')

av_df = pd.read_csv('avalanche_data_set.csv', delimiter=';')
av_df.set_index('no', inplace=True)
pd.set_option('display.max_columns', None)
av_df['date_release'] = pd.to_datetime(av_df['date_release'])
av_df['snow_type']=av_df['snow_type'].astype('category') 
av_df['trigger_type'] = av_df['trigger_type'].astype('category') 


av_df['North_South'] = [math.cos(x) for x in av_df['aspect_degrees']]
av_df['West_East'] = [math.sin(x) for x in av_df['aspect_degrees']]
av_df['elev_diff'] = av_df['max_elevation_m'] - av_df['min_elevation_m']

dt = av_df[['aspect_degrees', 'max.danger.corr', 'length_m']].dropna()

df_1 = av_df[av_df['max.danger.corr'] == 1]
df_2 = av_df[av_df['max.danger.corr'] == 2]
df_3 = av_df[av_df['max.danger.corr'] == 3]
df_4 = av_df[av_df['max.danger.corr'] == 4]
df_5 = av_df[av_df['max.danger.corr'] == 5]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df_1['max.danger.corr'],df_1['aspect_degrees'], df_1['length_m'], c = '#fe0002', s=60, alpha = .8, label = 'One')
ax.scatter(df_2['max.danger.corr'],df_2['aspect_degrees'], df_2['length_m'], c = '#d80027', s=60, alpha = .3, label = 'Two')
ax.scatter(df_3['max.danger.corr'],df_3['aspect_degrees'], df_3['length_m'], c = '#a1015d', s=60, alpha = .2, label = 'Three')
ax.scatter(df_4['max.danger.corr'],df_4['aspect_degrees'], df_4['length_m'], c = '#2a00d5', s=60, alpha = .3, label = 'Four')
ax.scatter(df_5['max.danger.corr'],df_5['aspect_degrees'], df_5['length_m'], c = '#0302fc', s=60, alpha = .8, label = 'Five')
ax.view_init(30,225)
ax.set_title('Danger rating vs. Aspect degrees(deg) vs. Length(m)')
ax.set_xlabel('Danger rating')
ax.set_ylabel('Aspect Degrees(deg)')
ax.set_zlabel('Length of avalanch(m)')
ax.legend()
plt.show()


# sns.catplot(x = 'aspect_degrees', y = 'max.danger.corr', data = dt)