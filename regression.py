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

def best_fit_slope_and_intercept(xs,ys):
    m = (((np.mean(xs)*np.mean(ys)) - np.mean(xs*ys)) / ((np.mean(xs)*np.mean(xs)) - np.mean(xs*xs)))
    
    b = np.mean(ys) - m*np.mean(xs)
    
    return m, b

# m, b = best_fit_slope_and_intercept(av_df['North_South'], av_df['area_m2'])
# m2, b2 = best_fit_slope_and_intercept(av_df['elev_diff'], av_df['area_m2'])


# fig, ax = plt.subplots(2)
# ax[0].set_yscale('log')
# ax[0].scatter(av_df['North_South'], av_df['area_m2'], alpha = 0.2)
# ax[0].plot(av_df['North_South'], m*av_df['North_South'] + b, color='blue')
# ax[0].set_title('North and South')
# ax[0].set_xlabel('Degrees North (0 to 1) and Degrees South (0 to -1)')
# ax[0].set_ylabel('Area m^2')

# # ax[1].set_yscale('log')
# ax[1].scatter(av_df['elev_diff'], av_df['area_m2'], alpha = 0.2)
# ax[1].plot(av_df['elev_diff'], m2*av_df['elev_diff'] +b2, color = 'blue')
# ax[1].set_title('elev_diff')
# ax[1].set_xlabel('Difference in elevation for each avalanche')
# ax[1].set_ylabel('Area m^2')
# plt.tight_layout()
# plt.savefig('regression_scatter_plot.png')


dt = av_df[['North_South','elev_diff', 'area_m2']].dropna()
model1 = smf.quantreg(formula = 'area_m2 ~ North_South', data = dt)
model2 = smf.ols(formula = 'area_m2 ~ elev_diff', data = dt)
results1 = model1.fit()
results2 = model2.fit()

residuals1 = results1.resid
residuals2 = results2.resid

# with open('quantile_summary.txt', 'w') as fh:
#     fh.write(results1.summary().as_text())
# with open('linear_summary.txt', 'w') as fh:
#     fh.write(results2.summary().as_text())

# sns.residplot('elev_diff', 'area_m2', data = dt, color = 'blue')
# plt.title('Elevation difference residual plot')
# plt.savefig('elev_diff_resid.png')
# gplots.qqplot(residuals2, line = "s")
# plt.title('Linear qqplot')
# plt.savefig('linear_reg_qqplot.png')
# gplots.qqplot(residuals1, line = "s")
# plt.title('Quantile qqplot')
# plt.savefig('quant_reg_qqplot.png')
"""
On average a single increase in aspect degree to the north or south direction leads to an increase in area of 226.33 m^2 using 
quantile regression.
"""
""" 
On average a single increase in aspect degree to the north or south direction leads to increase in area of 1056.89 m^2 using 
ordinary least squares regression.
"""
""" 
My data violates the assumtion of normaly distributed residuals shown in the qqplot,
so an inferential linear regression is not appropriate for this data.
However the use of a quantile regression is more appropriate becuase my data is independent
and somewhat linear.
"""
