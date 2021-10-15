# Import modules
import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read dataset in the variable data
data = pd.read_csv("country_data.csv")

# Output the first five rows of data
print(data.head())

# Get "Life Expectancy" column and store it in a variable named life_expectancy
life_expectancy = data["Life Expectancy"]

# Find the quartiles of life_expectancy and store the result in a variable names life_expentancy_quartiles
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])

# Output life_expectancy_quartiles
print(life_expectancy_quartiles)

# Plot a Histogram of life_expectancy
plt.hist(life_expectancy)
plt.show()

# Get "GDP" column and store it in a variable named gdp
gdp = data["GDP"]

# Calculate the median of gdp and save the result in a variable called median_gdp
median_gdp = np.quantile(gdp, 0.5)

# Display median_gdp
print(median_gdp)

# Get rows from data that have a GDP less than or equal to the median (median_gdp) and store the result in the variable low_gdp
low_gdp = data[data['GDP'] <= median_gdp]

# Get rows from data that have a GDP greater than the median (median_gdp) and store the result in the variable high_gdp
high_gdp = data[data['GDP'] > median_gdp]

# Find the quartiles of "Life Expectancy" column of low_gdp and save the results in a variable called low_gdp_quartiles
low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.5, 0.75])

# Find the quartiles of "GDP" column of high_gdp and save the results in a variable called high_gdp_quartiles
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'], [0.25, 0.5, 0.75])

# Output low_gdp_quartiles
print(low_gdp_quartiles)

# Output high_gdp_quartiles
print(high_gdp_quartiles)

# Plot Histograms of high_gdp["Life Expectancy"] and low_gdp["Life Expectancy"]
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()