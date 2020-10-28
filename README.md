# Danger Mountain

The dataset I decided to use is avalanche data from the ski resorts inside of Davos, Switzerland.  The data ranged from the year 1998 up to 2019.  My data was drawn from Kaggle and was set up quite nicely to begin with.  It started with the avalanche number, the date of release, the snow type, trigger type, max and min elevation in meters, aspect degrees, length, width, perimeter length, area, size class, weight, and max danger correlation.

I changed my index to the avalanche number.  I also changed the dae_release to a date time.  And the snow type, triiger type to a catageroical.  Afer doing this I was ready to start my EDA.

link :https://www.envidat.ch/dataset/ce11efbe-4dac-4ff5-9a3d-f01e2c573292/resource/4c2b7c38-a874-45fc-9833-fdf83823067b/download/data_set_1_avalanche_observations_wi9899_to_wi1819_davos.csv

# EDA


  

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
  
  
