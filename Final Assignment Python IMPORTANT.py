#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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


# In[21]:


#What are the five locations with the highest number of records?
top_5 = ad.nlargest(5, 'count_of_appointments')

# Accessing values
top_values = top_5['count_of_appointments']
corresponding_locations = top_5['sub_icb_location_name']

# Printing the top 5 values and their corresponding locations
for value, location in zip(top_values, corresponding_locations):
    print("Count of Appointments:", value, "| Location:", location)


# In[22]:


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


# In[23]:


#How many locations are there in the data set?
ad_unique_locations_count = ad['sub_icb_location_code'].nunique()
print("Number of locations:", ad_unique_locations_count)

#How many locations are there in the data set?
nc_unique_locations_count = nc['sub_icb_location_name'].nunique()
print("Number of locations:", nc_unique_locations_count)


# In[24]:


# Between what dates were appointments scheduled?
ad['appointment_date'] = pd.to_datetime(ad['appointment_date'])
min_date_ad = ad['appointment_date'].min().date()
max_date_ad = ad['appointment_date'].max().date()
print(f"For ad, appointments were scheduled from {min_date_ad} to {max_date_ad}")


# In[25]:


#Which service setting reported the most appointments in North West London from 1 January to 1 June 2022?
nc_subset = nc[(nc['sub_icb_location_name'] == 'NHS North West London ICB - W2U3Z') & 
               (nc['appointment_date'] >= '01/01/2022') & 
               (nc['appointment_date'] <= '01/06/2022')]
service_setting_counts = nc_subset['service_setting'].value_counts()
print(service_setting_counts.idxmax(), service_setting_counts.max())


# In[26]:


#Which month had the highest number of appointments?
appointments_per_month = nc.groupby('appointment_month').size()
highest_month = appointments_per_month.idxmax()
highest_count = appointments_per_month.max()
print(f"The month with the highest number of appointments was {highest_month} with {highest_count} appointments.")


# In[27]:


#What was the total number of records per month?
#2021 and 2022 DON'T overlap
nc['appointment_month'] = pd.to_datetime(nc['appointment_month'])
nc_2021 = nc[nc['appointment_month'].dt.year == 2021]
nc_2022 = nc[nc['appointment_month'].dt.year == 2022]
rows_per_month_2021 = nc_2021.groupby(nc_2021['appointment_month'].dt.month).size()
rows_per_month_2022 = nc_2022.groupby(nc_2022['appointment_month'].dt.month).size()
print("Rows per month in 2021:")
print(rows_per_month_2021)
print("\nRows per month in 2022:")
print(rows_per_month_2022)


# In[8]:


nc['appointment_month'] = nc['appointment_month'].astype(str)


nc_ss = nc.groupby(['appointment_month', 'service_setting'])['count_of_appointments'].sum().reset_index()


plt.figure(figsize=(12, 6))  
sns.lineplot(x='appointment_month', y='count_of_appointments', hue='service_setting', data=nc_ss, errorbar=None)
plt.title('Number of Appointments per Month for Service Settings')
plt.xlabel('Month')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45)  
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  
plt.tight_layout()  
plt.show()


nc_ct = nc.groupby(['appointment_month', 'context_type'])['count_of_appointments'].sum().reset_index()


plt.figure(figsize=(12, 6)) 
sns.lineplot(x='appointment_month', y='count_of_appointments', hue='context_type', data=nc_ct, errorbar=None)
plt.title('Number of Appointments per Month for Context Types')
plt.xlabel('Month')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45)  
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') 
plt.tight_layout() 
plt.show()


nc_nc = nc.groupby(['appointment_month', 'national_category'])['count_of_appointments'].sum().reset_index()


plt.figure(figsize=(12, 6)) 
sns.lineplot(x='appointment_month', y='count_of_appointments', hue='national_category', data=nc_nc, errorbar=None)
plt.title('Number of Appointments per Month for National Categories')
plt.xlabel('Month')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45) 
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  
plt.tight_layout()  
plt.show()


# In[17]:


nc_august = nc[nc['appointment_month'] == '2021-08']


service_settings_list = nc_august['service_setting'].unique()
appointments_per_month_list = nc_august.groupby('service_setting')['count_of_appointments'].sum().tolist()

plt.figure(figsize=(12, 6))
sns.barplot(x=service_settings_list, y=appointments_per_month_list, palette='viridis')
plt.title('Number of Appointments in August 2021 for Service Settings')
plt.xlabel('Service Setting')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[18]:


nc_october = nc[nc['appointment_month'] == '2021-10']


service_settings_list_october = nc_october['service_setting'].unique()
appointments_per_month_list_october = nc_october.groupby('service_setting')['count_of_appointments'].sum().tolist()

plt.figure(figsize=(12, 6))
sns.barplot(x=service_settings_list_october, y=appointments_per_month_list_october, palette='viridis')
plt.title('Number of Appointments in October 2021 for Service Settings')
plt.xlabel('Service Setting')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[19]:


nc_january = nc[nc['appointment_month'] == '2022-01']

service_settings_list_january = nc_january['service_setting'].unique()
appointments_per_month_list_january = nc_january.groupby('service_setting')['count_of_appointments'].sum().tolist()


plt.figure(figsize=(12, 6))
sns.barplot(x=service_settings_list_january, y=appointments_per_month_list_january, palette='viridis')
plt.title('Number of Appointments in January 2022 for Service Settings')
plt.xlabel('Service Setting')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[20]:


nc_april = nc[nc['appointment_month'] == '2022-04']

service_settings_list_april = nc_april['service_setting'].unique()
appointments_per_month_list_april = nc_april.groupby('service_setting')['count_of_appointments'].sum().tolist()


plt.figure(figsize=(12, 6))
sns.barplot(x=service_settings_list_april, y=appointments_per_month_list_april, palette='viridis')
plt.title('Number of Appointments in April 2022 for Service Settings')
plt.xlabel('Service Setting')
plt.ylabel('Number of Appointments')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:




