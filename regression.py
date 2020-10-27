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

# Does a northward or southward facing mountain cause a larger avalanche area?
# aspect degree of 0 = pure north
# aspect degree of 180 = pure south

north1 = av_df[(av_df['aspect_degrees'] >= 315)]
north2 = av_df[(av_df['aspect_degrees'] <= 45)]
north = pd.concat([north1, north2], axis=0)
south = av_df[(av_df['aspect_degrees'] >= 135) & (av_df['aspect_degrees'] <= 225)]

m, b = np.polyfit(south['aspect_degrees'], south['area_m2'], 1)

fig, ax = plt.subplots()
ax.scatter(south['aspect_degrees'], south['area_m2'])
ax.plot(south['aspect_degrees'], m*south['aspect_degrees'] + b)
ax.set_title('South')