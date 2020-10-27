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

#hypothesis test 2:  the number of avalanches with wet snow type is equal to the number with dry snow type
"""
h0: # avalanches dry = # of avalanches wet
ha: # avalanches dry != # of avalanches wet
or
h0 : avalaches dry - avalanches wet = 0
ha: avalaches dry - of avalanches wet != 0
"""
dry = av_df[av_df['snow_type'] == 'dry']   
wet = av_df[av_df['snow_type'] == 'wet']

alpha = .05
shared_freq = (len(dry)+len(wet))/ len(av_df)
variance = (11925*shared_freq*(1-shared_freq))/(len(dry)*len(wet))
difference_in_count = stats.norm(0, np.sqrt(variance))
threshold = difference_in_count.ppf(1-alpha)

fig, ax = plt.subplots(1, figsize=(16, 3))

x = np.linspace(-1, 1, num=2500)
ax.plot(x, difference_in_count.pdf(x), linewidth=3)
ax.axvline(threshold)
ax.fill_between(x, 0, difference_in_count.pdf(x), x>threshold, color = 'blue')
ax.set_xlim(-.025, .025)
ax.set_title("Distribution of Difference in Sample Frequencies Assuming $H_0$");
