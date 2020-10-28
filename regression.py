import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import statsmodels.formula.api as smf
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


def best_fit_slope_and_intercept(xs,ys):
    m = (((np.mean(xs)*np.mean(ys)) - np.mean(xs*ys)) / ((np.mean(xs)*np.mean(xs)) - np.mean(xs*xs)))
    
    b = np.mean(ys) - m*np.mean(xs)
    
    return m, b

# m, b = best_fit_slope_and_intercept(av_df['North_South'], av_df['area_m2'])
# m2, b2 = best_fit_slope_and_intercept(av_df['West_East'], av_df['area_m2'])


# fig, ax = plt.subplots(2)
# ax[0].set_yscale('log')
# ax[0].scatter(av_df['North_South'], av_df['area_m2'], alpha = 0.2)
# ax[0].plot(av_df['North_South'], m*av_df['North_South'] + b, color='blue')
# ax[0].set_title('North and South')
# ax[0].set_xlabel('Degrees North (0 to 1) and Degrees South (0 to -1)')
# ax[0].set_ylabel('Area m^2')

# ax[1].set_yscale('log')
# ax[1].scatter(av_df['West_East'], av_df['area_m2'], alpha = 0.2)
# ax[1].plot(av_df['West_East'], m2*av_df['West_East'] +b2, color = 'blue')
# ax[1].set_title('East and West')
# ax[1].set_xlabel('Degrees East (0 to 1) and Degrees West (0 to -1)')
# ax[1].set_ylabel('Area m^2')
# plt.tight_layout()
# plt.savefig('regression_scatter_plot.png')


dt = av_df[['North_South','West_East', 'area_m2']].dropna()
model = smf.quantreg(formula = 'area_m2 ~ North_South + West_East', data = dt).fit()

