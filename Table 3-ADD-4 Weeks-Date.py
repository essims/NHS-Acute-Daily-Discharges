# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:12:27 2023

@author: Esra Simsek
"""

import numpy
import pandas as pd
import string
from datetime import date
from datetime import datetime, timedelta


# Read the CSV file from the website
df = pd.read_excel(r"C:\Users\Esra Simsek\Desktop\ADD-tall versions\September-2023\Daily-discharge-sitrep-monthly-data-webfile-September2023.xlsx", sheet_name='Table 3')

df.columns = [''] * len(df.columns)


#Delete the first 2 columns
df = df.iloc[:, 2:]


def generate_column_names(num_columns):
    columns = []
    letters = list(string.ascii_uppercase)  # Get all uppercase letters as a list
    
    # Generate names using a combination of letters and numbers
    for i in range(num_columns):
        col_name = ""
        
        # Add letter(s) to the column name
        col_name += letters[i // 10]  # First letter from A to Z
        col_name += letters[i % 10]   # Second letter from A to Z
        
        # Add a number to the column name
        col_name += str((i % 100) // 10)   # Tens digit of the number
        col_name += str(i % 10)             # Units digit of the number
        
        columns.append(col_name)
    
    return columns

# Generate column names
column_names = generate_column_names(len(df.columns))



df.columns=column_names


def delete_data_before_value(df, column_name, search_value):
    # Find the index of the row containing the search value
    index = df.index[df[column_name] == search_value].tolist()[0]

    # Select the subset of the dataframe starting from the row with the search value
    df = df.iloc[index+1:]

    return df


search_value = 'Org Code'
column_name = 'AA00'

df = delete_data_before_value(df, column_name, search_value)

#print(df.columns)

length=len(df)

# Hold the first 2 columns
first_three_columns = df.iloc[:, :2]

# Unpivot the remaining columns
df = df.melt(id_vars=first_three_columns.columns.tolist())

old_variable_name1 = 'AC02', 'AF05', 'AI08', 'BB11'
new_variable_name1 = 'Number of additional bed days, patients with length of stay of 7+ days'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name1, new_variable_name1)

old_variable_name2 =  'AD03', 'AG06', 'AJ09', 'BC12'
new_variable_name2 = 'Number of additional bed days, patients with length of stay of 14+ days'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name2, new_variable_name2)

old_variable_name3 =  'AE04', 'AH07', 'BA10', 'BD13'
new_variable_name3 = 'Number of additional bed days, patients with length of stay of 21+ days'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name3, new_variable_name3)

# Define the mapping dictionary for column name changes
column_mapping = {'AA00': 'Code', 'AB01': 'Name', 'variable': 'Criteria'}

# Rename the columns
df.rename(columns=column_mapping, inplace=True)

#df.to_csv("Table3-2-Org.csv", index=False)


import datetime

def find_first_monday(year, month):
    first_day = datetime.date(year, month, 1)
    days_until_first_monday = (7 - first_day.weekday()) % 7
    first_monday = first_day + datetime.timedelta(days=days_until_first_monday)
    return first_monday

def add_seven_days(date, times=1):
    new_date = date
    for _ in range(times):
        new_date += datetime.timedelta(days=7)
    return new_date

# Replace these values with the desired year and month
year = 2023
month = 9

first_monday = find_first_monday(year, month)
result_dates = [add_seven_days(first_monday, times=i) for i in range(4)]


repetitions = length*3

formatted_dates = [d.strftime("%d-%m-%Y") for d in result_dates]

df['Period'] = [item for item in formatted_dates for _ in range(repetitions)]
df = df.rename(columns={'value': 'Value'})


file_path= "C:\\Users\\Esra Simsek\\Desktop\\deneme3.csv"

df.to_csv(file_path, index=False)

