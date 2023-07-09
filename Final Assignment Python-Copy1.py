#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
import numpy as np

# Load the data sets
ad = pd.read_csv('/Users/GianniXue/Documents/actual_duration.csv')
ar = pd.read_csv('/Users/GianniXue/Documents/appointments_regional.csv')
nc = pd.read_excel('/Users/GianniXue/Documents/national_categories.xlsx')

# Sense-check new DataFrames
print('Actual Duration DataFrame:')
print('Columns:', ad.columns)
print('Number of rows and columns:', ad.shape)
print('Data types:', ad.dtypes)
print('Number of missing values:', ad.isnull().sum())

print('\nAppointments Regional DataFrame:')
print('Columns:', ar.columns)
print('Number of rows and columns:', ar.shape)
print('Data types:', ar.dtypes)
print('Number of missing values:', ar.isnull().sum())

print('\nNational Categories DataFrame:')
print('Columns:', nc.columns)
print('Number of rows and columns:', nc.shape)
print('Data types:', nc.dtypes)
print('Number of missing values:', nc.isnull().sum())

# Descriptive statistics and metadata
print('\nDescriptive statistics and metadata for Actual Duration:')
print(ad.describe())
print(ad.info())

print('\nDescriptive statistics and metadata for Appointments Regional:')
print(ar.describe())
print(ar.info())

print('\nDescriptive statistics and metadata for National Categories:')
print(nc.describe())
print(nc.info())

# Exploration
# Assuming 'sub_icb_location_name' is a column in nc DataFrame
location_counts = nc['sub_icb_location_name'].value_counts()
print("Count of locations: ", location_counts)


# In[ ]:




