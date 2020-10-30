# Danger Mountain
Disclaimer: Do not cause avalanches on the mountain and measure them to get more robust data.  Leave that to the professionals.

The dataset I decided to use is avalanche data from Davos, Switzerland.  The data ranged from the year 1998 up to 2019.  It is a record of every avalanche that happened in the area.  There is no exact hour and minute time stamp but there is a date that the avalanche occured at.  The months range from October at the earliest and June at the latest with everything inbetween.

# My Data and Data Cleaning
My data started with the following columns: avalanche number, the date of release, the snow type, trigger type, max and min elevation in meters, aspect degrees, length, width, perimeter length, area, size class, weight, and max danger correlation.

I changed my index to the avalanche number.  I also changed the date_release to a date time.  I changed the snow type and trigger type to a catageroical.  Afer doing this I was ready to start my EDA.

# EDA
1. Snow types
   - dry
   - wet
   - mixed
   - unknown
2. Trigger types
   - Human
   - Natural
   - Unknown
3. Different columns described
   - Aspect degrees:
     - A degree of the face of the mountain in relation to the sun.
   - Max danger
     - A ranking of 1-5 of the danger of the avalanche 1 being the worst.
   - Size class
     - A ranking of 1-5 of the size of the avalanche 1 being the smallest.
   - Area
     - The final area the avalanche covers  

4. Here are a few statistics about my data:
   - Mean aspect degrees: 151.415<sup>o</sup>
   - Median aspect degrees: 125.0<sup>o</sup>
   - Mean impact area: 16638.671 m<sup>2</sup>
   - Median impact area: 5624.5 m<sup>2</sup>

To continue my EDA I plotted a few of my variables to help me visualize the data.

<p align="center">
    <img src="graphs/aspect_deg_hist_new.png" width='700'/>
</p>

<p align="center">
    <img src="graphs/danger_area_bar_scatter.png" width='700'/>
</p>

<p align="center">
    <img src="graphs/area_scatter_for_each.png" width='700'/>
</p>
<br />
<p align="center">
    <img src="graphs/danger_deg_len.png" size = '800x800'/>
</p>


# Which is larger: Dry or Wet Avalanches?

For my hypothesis test I decided to test whether the mean area of avalanches with wet snow type is equal to the mean area with dry snow type.  <br />
<br />
Listed below is my two tail null and alternate hypothesis:
- H0: mean area of dry avalanches = mean area of wet avalanches
- HA: mean area of dry avalanches != mean area of wet avalanches <br />
or
- H0 : mean area of dry avalaches - mean area of wet avalanches = 0
- HA: mean area of dry avalaches - mean area of wet avalanches != 0
<br />
Using a welches t-test I obtained a t-value of 0.01057, a p-value of 1.66 e-13, and a standard error of 1153.24.  Looking below at the graph of my test we can see that we are greater than 95% confident that our sample mean is outside -1153.24 and 1153.24.  As shown in the graph my actuall sample mean is represented by the green line which is far outside my distribution.  
<br />
<p align="center">
    <img src="graphs/dry_v_wet.png" width='750', height = "300"/>
</p>
<br />

- The p-value = 1.6599364216596502e-13, which is less than our significance level of 0.05, so we must reject the null hypothesis.
- The probability of seeing these sample means given the null hypothesis is true is 1.6599364216596502e-13

<br />

# My questions and How I Tried to Answer Them
I conducted two regressions on my data.  First I wanted to see if a mountain with a northern and southern facing direction caused a larger avalanche.  Secondly I wanted to see if a large difference in elevation would cause a larger avalanche vs a smaller difference.    <br />
My first step to do this regression is to visualize the data to get a better idea of what I am working with.  
<br />
<p align="center">
    <img src="graphs/regression_scatter_plot.png" width='700'/>
</p>
<br />
As you can see above my data is not very good to be running regressions on.  It definitly violates some assumtions for a linear regression.  So for my north and south regression I used a quantile regression instead so that I do not violate the assumtions of a linear regression.  The assumptions of a quantile regression are linearity, no multicolinearity, and independence.  The quantile regression was a more appropraite model because my data is not very highly correlated and is not normally distributed.  
<br />
<br />
For my second regression the data is a little better to not violate the assumtions of a linear regression although it is far from perfect.  Below are two qqplots for each of my regressions showing that neither of my regressions data follow a normal distrubtion perfectly.  
<br />
<br />
First is the north and south quantile regression
<p align="center">
    <img src="graphs/quant_reg_qqplot.png" width='700'/>
</p>
<br />
Next is the difference in elevation linear regression
<p align="center">
    <img src="graphs/linear_reg_qqplot.png" size = '800x600'/>
</p>
<br />
To further show how my second regression violates the assumtions for a linear regression, below is a residuals plot that shows how much heteroscedasticity is contained in my data.
<p align="center">
    <img src="graphs/elev_diff_resid.png" size = '700x400'/>
</p>
<br />
Below is the summary table for my quantile regression, the effect on area from mountains tha face north and south. 

<br />
<p align="center">
    <img src="graphs/quantile_summary.png" size = '700x400'/>
</p>

<br />
Conclusion: On average a single increase in aspect degree to the north or south direction leads to an increase in area of 226.33 meters<sup>2</sup> using quantile regression.  My p-value is right on the cusp of the .05 significance level for rejecting the null hypothesis.  Which again can be seen in the confidence interval as it is very close to containing zero.  
<br />
Next is the summary table for my linear regression, the effect on area from difference in elevation.

<br />
<p align="center">
    <img src="graphs/linear_summary.png" size = '700x400'/>
</p>

<br />
Conclusion: On average a single increase is the difference in elevation leads to an increase in avalanche area of 198.6 meters<sup>2</sup>.  In this regression my data is at least a little bit correlated with each other.  But is not very normal according to the Durbin-Watson test.  Ignoring that my p-value is so small it is basically zero meaning my data is significant and there is a very small chance that my 95% confidence interval will contain zero.

# Conclusion
After conducting this experiment I thought about what possible exogenous or external factors that could have effected my test.  some possibilities are a changing climate possibly from pollution or the rise in the earths temperature.  Another could be a rise in erratic weather that cause huge snow dumps and ergo an increase in avalanches.  In other words there are many other factors that are not strictly expressed in the data that could have affected my experiment.     
<br />
All in all no nobel prize will be won from this dataset, but hopefully you will have learned something about avalanches.

# Appendix

- Dataset link :https://www.envidat.ch/dataset/ce11efbe-4dac-4ff5-9a3d-f01e2c573292/resource/4c2b7c38-a874-45fc-9833-fdf83823067b/download/data_set_1_avalanche_observations_wi9899_to_wi1819_davos.csv

