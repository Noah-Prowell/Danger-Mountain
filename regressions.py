import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats
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

#hypothesis test 2:  the mean area of avalanches with wet snow type is equal to the mean area with dry snow type
"""
h0: mean area of dry avalanches= mean area of wet avalanches
or
h0 : mean area of dry avalaches - mean area of wet avalanches = 0
ha: mean area of dry avalaches - mean area of wet avalanches != 0
"""
dry = av_df[av_df['snow_type'] == 'dry']   
wet = av_df[av_df['snow_type'] == 'wet']
alpha = .05

dry_area_mean = dry.mean()[6]
wet_area_mean = wet.mean()[6]
total_area_mean = av_df.mean()[6]
mean_diff = dry_area_mean - wet_area_mean

dry_area_std = dry.std()[6]
wet_area_std = wet.std()[6]

n_wet = len(wet)
n_dry = len(dry)

tstat = (dry_area_mean - wet_area_mean)/((dry_area_std**2/n_dry) + (wet_area_std**2/n_wet))

p_val = stats.ttest_ind(dry['area_m2'].dropna(), wet['area_m2'].dropna(), equal_var = False)[1] 

st_error = np.sqrt((dry_area_std**2/len(dry)) + (wet_area_std**2/len(wet)))

null_distribution = stats.norm(0, st_error)
threshold_upper = null_distribution.ppf(1-alpha)
threshold_lower = null_distribution.ppf(alpha)
fig, ax = plt.subplots(1, figsize=(16, 3))

x = np.linspace(-3000, 3000, num=2500)
ax.plot(x, null_distribution.pdf(x), linewidth=3)
ax.axvline(threshold_upper, color = 'blue', label = '95 Percent confidence')
ax.axvline(threshold_lower, color = 'blue')
ax.axvline(mean_diff, color = 'green', label = 'Actual Diff in Means')
ax.fill_between(x, 0, null_distribution.pdf(x), x>threshold_upper, color = 'blue')
ax.fill_between(x, 0, null_distribution.pdf(x), x<threshold_lower, color = 'blue')
ax.set_xlim(-2500,5500)
ax.set_title('Distribution of Welchs t-statistic Under the Null Hypothesis')
ax.set_xlabel('Difference in sample means')
ax.set_ylabel('Distribution')
ax.legend();

plt.savefig('dry_v_wet.png')
print(f'The p-value = {p_val}, which is less than our significance level of {alpha}, so we must reject the null hypothesis.')
print(f'The probability of seeing these sample means given the null hypothesis is true is {p_val}')

