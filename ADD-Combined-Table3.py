# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:16:52 2023

@author: Esra Simsek
"""

import pandas as pd
import os
import re


directory="C:/Users/Esra Simsek/Desktop/ADD-tall versions/ADD Time Series-Table 3"

combined_data = pd.DataFrame()

def extract_date(text):
    match = re.search(r'\d{2}-\d{2}-\d{4}', text)
    if match:
        return pd.to_datetime(match.group(), format='%d-%m-%Y')
    else:
        return None

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        data = pd.read_csv(file_path)
        data['Date'] = data['period'].apply(extract_date)
        data = data.dropna(subset=['Date'])  # Remove rows with missing dates
        data = data.sort_values(by='Date')
        combined_data = pd.concat([combined_data, data], ignore_index=True)

# Remove the "Date" column
combined_data = combined_data.drop(columns=['Date'])

file_path= "C:\\Users\\Esra Simsek\\Desktop\\ADD-tall versions\Time Series-ADD-Table3.csv"

combined_data.to_csv(file_path, index=False)

