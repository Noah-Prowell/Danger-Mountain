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


# # Hypothesis test 1: There are more avalanches with an aspect degree less than 45 than greater than 45
# """
# the aspect degree is the angle of the face of the mountain with relation to the sun.  A 0 degree angle means that the mtn is facing
# exactly north and is very cold in the northern hemisphere.  A 180 degree angle means that the mtn is facing south
# and is a very warm slope.  
# """
# aspect_degrees = av_df[['aspect_degrees']]
# aspect_degrees.dropna(inplace=True)
# """ 
# H0: aspect_degrees < 45  
# HA: aspect_degrees > 45
# use central limit theorem to make the data normal then run a t-test on the data
# """
# def clt(df):
#     """grab a random sample mean from the given dataset

#     Args:
#         df (pd dataframe): dataframe to find the mean from

#     Returns:
#         float: the mean of a random sample
#     """
#     sample_mean = df.sample(n = 11000, axis = 0).mean()
#     return sample_mean.iloc[0]

# def normalize(df, n):
#     """create an array of random sample means

#     Args:
#         df (dataframe): dataframe to create the samples
#         n (int): number of sample means to create

#     Returns:
#         numpy array: array of sample means
#     """
#     distr =  np.array([clt(df) for i in range(n)])
#     return distr

# ad_normalized = normalize(aspect_degrees, 15000)
# # use 100 bins in histogram
# fig, ax = plt.subplots()
# def histogram(ax, x, bin, label = 'label'):
#     ax.hist(x, bins = bin)
#     ax.set_xlabel(label)
#     return 

# ad_normalized_mean = ad_normalized.mean()
# ad_normalized_var = ad_normalized.var()
# normal_appox = stats.norm(ad_normalized_mean, np.sqrt(ad_normalized_var)).cdf(45)
# # graph the pdf

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
threshold = null_distribution.ppf(1-alpha)
fig, ax = plt.subplots(1, figsize=(16, 3))

x = np.linspace(-3000, 3000, num=2500)
ax.plot(x, null_distribution.pdf(x), linewidth=3)
ax.axvline(threshold, color = 'blue', label = '95 Percent Threshold')
ax.axvline(mean_diff, color = 'green', label = 'Actual Diff in Means')
ax.fill_between(x, 0, null_distribution.pdf(x), x>threshold, color = 'blue')
ax.set_xlim(-3000,5500)
ax.set_title(f'{100*alpha}% of the area under the curve falls to the right of {round(threshold,3)}')
ax.set_xlabel();
