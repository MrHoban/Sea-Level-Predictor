import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

  # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(
      df['Year'], df['CSIRO Adjusted Sea Level'])
  years_extended = range(1880, 2051)
  line1 = [slope * x + intercept for x in years_extended]
  plt.plot(years_extended, line1, label='Line of Best Fit: 1880-2050')

  # Create second line of best fit for data from year 2000
  new_df = df[df['Year'] >= 2000]
  slope_new, intercept_new, r_value_new, p_value_new, std_err_new = linregress(
      new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
  years_extended_new = range(2000, 2051)  # Range from 2000 to 2050
  line2 = [slope_new * x + intercept_new for x in years_extended_new]
  plt.plot(years_extended_new,
           line2,
           label='Line of Best Fit: 2000-2050',
           linestyle='--')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Display legend
  plt.legend()

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png'
