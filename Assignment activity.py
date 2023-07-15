#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import necessary libraries
import pandas as pd
import numpy as np

# Load the data sets
ad = pd.read_csv("/Users/giannixue/Desktop/Python Finals/actual_duration.csv")
ar = pd.read_csv("/Users/giannixue/Desktop/Python Finals/appointments_regional.csv")
nc = pd.read_excel("/Users/giannixue/Desktop/Python Finals/national_categories.xlsx")


# In[8]:


#What are the five locations with the highest number of records?
top_5 = ad.nlargest(5, 'count_of_appointments')

# Accessing values
top_values = top_5['count_of_appointments']
corresponding_locations = top_5['sub_icb_location_name']

# Printing the top 5 values and their corresponding locations
for value, location in zip(top_values, corresponding_locations):
    print("Count of Appointments:", value, "| Location:", location)


# In[18]:


#How many service settings, context types, national categories, and appointment statuses are there?

#Service settings
num_service_setting = nc['service_setting'].nunique()
print('Number of service settings:', num_service_setting)

#Context types
num_context_type = nc['context_type'].nunique()
print('Number of context type:', num_context_type)

#National categories
num_national_categories = nc['national_category'].nunique()
print('Number of national categories:', num_national_categories)

#Appointment Statuses
num_appointment_statuses = ar['appointment_status'].nunique()
print('Number of appointment statuses:', num_appointment_statuses)


# In[11]:


#How many locations are there in the data set?
ad_unique_locations_count = ad['sub_icb_location_code'].nunique()
print("Number of locations:", ad_unique_locations_count)

#How many locations are there in the data set?
nc_unique_locations_count = nc['sub_icb_location_name'].nunique()
print("Number of locations:", nc_unique_locations_count)


# In[14]:


# Between what dates were appointments scheduled?
ad['appointment_date'] = pd.to_datetime(ad['appointment_date'])
min_date_ad = ad['appointment_date'].min().date()
max_date_ad = ad['appointment_date'].max().date()
print(f"For ad, appointments were scheduled from {min_date_ad} to {max_date_ad}")


# In[15]:


#Which service setting reported the most appointments in North West London from 1 January to 1 June 2022?
nc_subset = nc[(nc['sub_icb_location_name'] == 'NHS North West London ICB - W2U3Z') & 
               (nc['appointment_date'] >= '01/01/2022') & 
               (nc['appointment_date'] <= '01/06/2022')]
service_setting_counts = nc_subset['service_setting'].value_counts()
print(service_setting_counts.idxmax(), service_setting_counts.max())


# In[16]:


#Which month had the highest number of appointments?
appointments_per_month = nc.groupby('appointment_month').size()
highest_month = appointments_per_month.idxmax()
highest_count = appointments_per_month.max()
print(f"The month with the highest number of appointments was {highest_month} with {highest_count} appointments.")


# In[19]:


#What was the total number of records per month?
nc['appointment_month'] = pd.to_datetime(nc['appointment_month'])
nc['month'] = nc['appointment_month'].dt.month
rows_per_month = nc.groupby('month').size()
print(rows_per_month)


# In[ ]:




