#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Initial commit: 2022 03

Adapted from "Python for Data Science" by UCSanDiegoX, an edX class
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# World Development Indicators dataset from Kaggle
data = pd.read_csv('Indicators.csv')

# select CO2 emissions for the United States
indicator = 'CO2 emissions \(metric'
country = 'USA'

# boolean masks
mask1 = data['IndicatorName'].str.contains(indicator) 
mask2 = data['CountryCode'].str.contains(country)

# df containing data of interest
subset = data[mask1 & mask2]

# font
matplotlib.rcParams['font.family'] = 'Helvetica'

# matplotlib version
plt.figure()
plt.plot(subset['Year'].values, subset['Value'].values)
# labels
plt.xlabel('Year')
plt.ylabel(subset['IndicatorName'].iloc[0])
plt.title('')
# axis limits
plt.axis([1959, 2015, 0, 25])
plt.show()

# seaborn version
plt.figure()
sns.lineplot(data=subset, x='Year', y='Value')
plt.xlabel('Year')
plt.ylabel(subset['IndicatorName'].iloc[0])
plt.axis([1959, 2015, 0, 25])