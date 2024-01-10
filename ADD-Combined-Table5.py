# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:54:34 2023

@author: Esra Simsek
"""

import pandas as pd
import os

directory="C:/Users/Esra Simsek/Desktop/ADD-tall versions/ADD Time Series-Table 5"

combined_data = pd.DataFrame()

# Loop through the CSV files in the specified directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        data = pd.read_csv(file_path)
        
        # Assuming the "period" column contains date data in the format 'dd/mm/yyyy'
        data['Month-Year'] = pd.to_datetime(data['Period'], format='%d/%m/%Y', errors='coerce')
        
        data = data.dropna(subset=['Month-Year'])  # Remove rows with missing dates
        
        # Extract the month and year and save it to the "Period" column
        data['Period'] = data['Month-Year'].dt.strftime('%B %Y')
        
        combined_data = pd.concat([combined_data, data], ignore_index=True)

# Sort the combined data by the Month-Year column
combined_data = combined_data.sort_values(by='Month-Year')

# Remove the 'Month-Year' column if you don't need it in the final output
combined_data = combined_data.drop(columns=['Month-Year'])


file_path= "C:\\Users\\Esra Simsek\\Desktop\\ADD-tall versions\Time Series-ADD-Table5.csv"

combined_data.to_csv(file_path, index=False)
