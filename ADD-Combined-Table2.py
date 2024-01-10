# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:09:21 2023

@author: Esra Simsek
"""

import pandas as pd
import os



directory="C:/Users/Esra Simsek/Desktop/ADD-tall versions/ADD Time Series-Table 2"

combined_data = pd.DataFrame()

date_format = "%Y-%m-%d"

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        data = pd.read_csv(file_path, parse_dates=['date'], date_parser=lambda x: pd.to_datetime(x, format=date_format))
        combined_data = pd.concat([combined_data, data], ignore_index=True)


combined_data['date'] = pd.to_datetime(combined_data['date'])  # Convert Date column to datetime
combined_data = combined_data.sort_values(by='date')

file_path= "C:\\Users\\Esra Simsek\\Desktop\\ADD-tall versions\Time Series-ADD-Table2.csv"

combined_data.to_csv(file_path, index=False)
