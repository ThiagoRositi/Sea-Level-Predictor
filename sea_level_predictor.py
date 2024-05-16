import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)
    # Create first line of best 
    slope,intercept,_,_,_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line = slope * df['Year'] + intercept
    years1 = np.arange(1880, 2051, 1)
    future_line = slope * years1 + intercept
    plt.plot(years1, future_line, linestyle="--",color='red', label='Prediction for 2050')
    # Create second line of best fit
    twoThousand_Df = df.loc[df['Year'] >= 2000]
    slope2,intercept2,_,_,_ = linregress(twoThousand_Df['Year'], twoThousand_Df['CSIRO Adjusted Sea Level'])
    years2 = np.arange(2000, 2051, 1)
    future_line2 = slope2 * years2 + intercept2
    plt.plot(years2, future_line2, linestyle='--', color='blue', label='Prediction for 2050')
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()