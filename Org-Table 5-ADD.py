# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:48:11 2023

@author: Esra Simsek
"""

import numpy
import pandas as pd
import string
from datetime import date
from datetime import datetime, timedelta


# Read the CSV file from the website
df = pd.read_excel(r"C:\Users\Esra Simsek\Desktop\ADD-tall versions\August-2023\Daily-discharge-sitrep-monthly-data-webfile-August2023.xlsx", sheet_name='Table 5')

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

old_variable_name1 = 'AC02'
new_variable_name1 = 'Awaiting a medical decision/intervention including writing the discharge summary'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name1, new_variable_name1)

old_variable_name2 =  'AD03'
new_variable_name2 = 'Awaiting community equipment and adaptations to housing'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name2, new_variable_name2)

old_variable_name3 =  'AE04'
new_variable_name3 = 'Awaiting confirmation from community hub/single point of access that referral received and actioned'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name3, new_variable_name3)


old_variable_name4 =  'AF05'
new_variable_name4 = 'Awaiting Diagnostic test'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name4, new_variable_name4)

old_variable_name5 =  'AG06'
new_variable_name5 = 'Awaiting medicines to take home '

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name5, new_variable_name5)

old_variable_name6 =  'AH07'
new_variable_name6 = 'Awaiting referral to community single point of access'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name6, new_variable_name6)

old_variable_name7 =  'AI08'
new_variable_name7 = 'Awaiting therapy decision to discharge'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name7, new_variable_name7)

old_variable_name8 =  'AJ09'
new_variable_name8 = 'Awaiting transport'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name8, new_variable_name8)

old_variable_name9 =  'BA10'
new_variable_name9 = 'Declared as not meeting the criteria to reside at morning board round and then later in day meets the criteria to reside so discharge stopped '

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name9, new_variable_name9)

old_variable_name10 =  'BB11'
new_variable_name10 = 'Homeless/no right of recourse to public funds/no place to discharge to'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name10, new_variable_name10)

old_variable_name11 =  'BC12'
new_variable_name11 = 'Individual/family not in agreement with discharge plans'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name11, new_variable_name11)

old_variable_name12 =  'BD13'
new_variable_name12 = 'No Plan'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name12, new_variable_name12)

old_variable_name13 =  'BE14'
new_variable_name13 = 'Pathway 1: awaiting availability of resource for assessment and start of care at home'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name13, new_variable_name13)

old_variable_name14 =  'BF15'
new_variable_name14 = 'Pathway 2: awaiting availability of rehabilitation bed in community hospital or other bedded setting'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name14, new_variable_name14)

old_variable_name15 =  'BG16'
new_variable_name15 = 'Pathway 3: awaiting availability of a bed in a residential or nursing home that is likely to be a permanent placement'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name15, new_variable_name15)

old_variable_name16 =  'BH17'
new_variable_name16 = 'Remains in hospital to avoid spread of (non-Covid 19) infectious disease and because there is no other suitable location to discharge to'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name16, new_variable_name16)

old_variable_name17 =  'BI18'
new_variable_name17 = 'Repatriation/Transfer to another acute trust for specialist treatment or ongoing treatment'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name17, new_variable_name17)

old_variable_name18 =  'BJ19'
new_variable_name18 = 'Safeguarding concern preventing discharge or Court of protection'

# Replace the old variable name with the new variable name in the column
df['variable'] = df['variable'].replace(old_variable_name18, new_variable_name18)

# Define the mapping dictionary for column name changes
column_mapping = {'AA00': 'Code', 'AB01': 'Name', 'variable': 'The reasons why they continued to reside'}

# Rename the columns
df.rename(columns=column_mapping, inplace=True)

file_path= "C:\\Users\\Esra Simsek\\Desktop\\ADD-tall versions\\August-2023\\Table5-August23.csv"

df.to_csv(file_path, index=False)

