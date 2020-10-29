# Danger Mountain

The dataset I decided to use is avalanche data from the ski resorts inside of Davos, Switzerland.  The data ranged from the year 1998 up to 2019.  My data was drawn from Kaggle and was set up quite nicely to begin with.  It started with the avalanche number, the date of release, the snow type, trigger type, max and min elevation in meters, aspect degrees, length, width, perimeter length, area, size class, weight, and max danger correlation.

I changed my index to the avalanche number.  I also changed the dae_release to a date time.  And the snow type, triiger type to a catageroical.  Afer doing this I was ready to start my EDA.

link :https://www.envidat.ch/dataset/ce11efbe-4dac-4ff5-9a3d-f01e2c573292/resource/4c2b7c38-a874-45fc-9833-fdf83823067b/download/data_set_1_avalanche_observations_wi9899_to_wi1819_davos.csv

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

4. Here are a few statistics about my data:
   - Mean aspect degrees: 151.415
   - Median aspect degrees: 125.0
   - Mean impact area: 16638.671
   - Median impact area: 5624.5

To continue my EDA I plotted a few of my variables as histograms as well as a scatter plot to help me visualize the data.

<p align="center">
    <img src="aspect_deg_hist.png" width='700'/>
</p>

<p align="center">
    <img src="danger_area_bar_scatter.png" width='700'/>
</p>

<p align="center">
    <img src="area_scatter_for_each.png" width='700'/>
</p>


# Hypothesis Test

For my hypothesis test I decided to test whether the mean area of avalanches with wet snow type is equal to the mean area with dry snow type.  <br />
<br />
Listed below is my two tail null and alternate hypothesis:
- h0: mean area of dry avalanches = mean area of wet avalanches
- ha: mean area of dry avalanches != mean area of wet avalanches <br />
or
- h0 : mean area of dry avalaches - mean area of wet avalanches = 0
- ha: mean area of dry avalaches - mean area of wet avalanches != 0
<br />
Using a welches t-test I obtained a t-value of 0.01057, a p-value of 1.66 e-13, and a standard error os 1153.24.  Looking below at the graph of my test we can see that we are 95% confident that our population mean is outside -1153.24 and 1153.24.  As shown in the graph my actuall sample mean is represented by the green line which is far outside my distribution.  
<br />
<p align="center">
    <img src="dry_v_wet.png" width='800', height = "300"/>
</p>

- The p-value = 1.6599364216596502e-13, which is less than our significance level of 0.05, so we must reject the null hypothesis.

- The probability of seeing these sample means given the null hypothesis is true is 1.6599364216596502e-13


# Avalanche data for Davos Switzerland 1999-2019
  link :https://www.envidat.ch/dataset/ce11efbe-4dac-4ff5-9a3d-f01e2c573292/resource/4c2b7c38-a874-45fc-9833-fdf83823067b/download/data_set_1_avalanche_observations_wi9899_to_wi1819_davos.csv
  
  1.Graphs:
  
    -Histogram of the aspect degrees of each avalanche
    
    -Scatter plot of aspect degrees and the danger 
    
    -Scatter of the aspect degrees and damage area
    
    -Plot snow types and avalanche size
    
    -Aspect degrees and length
    
  2.Possible regressions:
  
    -does a higher aspect degree mean a greater damage area?
    
    -Does a dry snow type cause a larger avalanche?
    
    -Does a wet snow type cause a larger avalanche?
    
  3.Statistics:
  
    -Mean avalache area
    
    -Mean aspect degrees
    
    -correlation of aspect degrees and avalanche area
  
    - Which seasons have the most natural avalanches?
  
  
