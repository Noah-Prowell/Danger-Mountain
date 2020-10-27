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


def get_two_columns_mean_median(a, col1, col2, grp, mn):
    """Grabs two colums from the avalanche dataset and returns the sliced 
    dataframe, the mean dataframe, and the median dataframe.

    Args:
        a (pd dataframe): Avalanche dataset(or others)
        col1 (string): 1st column to grab
        col2 (string): 2nd column to grab
        grp (string): column to groupby
        mn (string): column to do aggregation function

    Returns:
        dataframe: dataframe with two rows
        dataframe: grouped by mean dataframe
        dataframe: grouped by median dataframe
    """
    df = a[[col1, col2]]
    mean = df.groupby([grp])[mn].mean()
    median = df.groupby([grp])[mn].median()
    return df, mean, median

# aspect degrees and area
df, mean, median = get_two_columns_mean_median(av_df, 'aspect_degrees', 'area_m2', 'aspect_degrees', 'area_m2') 
fig, ax = plt.subplots()
def log_scatter(ax, df, x, y):
    """Graphs a scatter on a log scale

    Args:
        ax (none): parameter to graph on plot
        df (dataframe): dataframe to graph
        x (string): column 1 to be on x-axis
        y (string): column2 to be on y-axis
    """
    col1 = np.array([df[x]])
    col2 = np.array([df[y]])
    ax.scatter(col1, col2)
    plt.yscale("log")
    ax.set_xlabel = x
    ax.set_ylabel = y
    return

def scatter(ax, df, x, y):
    """graphs a scatter

    Args:
        ax (none):  parameter to graph on plot
        df (dataframe): dataframe to graph
        x (string): x axis column
        y (string): y axis column
    """
    col1 = np.array([df[x]])
    col2 = np.array([df[y]])
    ax.scatter(col1, col2)
    ax.set_xlabel = x
    ax.set_ylabel = y
    return

def histogram(ax, df, x, label = 'label'):
    """graph a histogram 

    Args:
        ax (none): parameter to graph
        df (dataframe): dataframe to graph
        x (string): column for x-axis
        label (str, optional): x label. Defaults to 'label'.
    """
    ax.hist(df[x], bins = 10)
    ax.set_xlabel = label
    return

# snow types and avalanche sizes
df_snow_size, snow_size_mean, snow_size_median = get_two_columns_mean_median(av_df, 'snow_type', 'area_m2', 'snow_type', 'area_m2')


#Aspect degrees amd length
def get_two_columns(a, col1, col2):
    df = a[[col1, col2]]
    return df

df_ad_length = get_two_columns(av_df, 'aspect_degrees', 'length_m')



# Getting the natural avalance data and the human avalanche data
av_df_natural = av_df[av_df['trigger_type'] == 'NATURAL'] 
av_df_human = av_df[av_df['trigger_type'] == 'HUMAN']
av_df_unknown = av_df[av_df['trigger_type'] == 'UNKNOWN']



"""Idea: 3D graph the verticle data of 20 random avalanches in a circle 
around a central point, the min height point will be pivoted out according to the ascpect degree
then color each line and point to the level of danger corresponding with the avalanche"""


# Regression 1: If the  aspect degrees increases then the area will also increase
aspect_degrees_area = get_two_columns(av_df, 'aspect_degrees', 'area_m2')
aspect_degrees_area.dropna(inplace=True)
""" 
H0: 
"""