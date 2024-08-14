# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:19:52 2024

@author: Yenny SA
"""

import pandas as pd

# Sample DataFrame creation (replace this with your actual DataFrame)
data = {
    'id': [1, 2, 3],
    'age': [25, 30, 22],
    'sex': [1, 2, 1],
    'height': [170, 180, 160],  # Assuming height is in cm
    'weight': [70, 90, 50],      # Assuming weight is in kg
    'ap_hi': [120, 130, 110],
    'ap_lo': [80, 85, 70],
    'cholesterol': [1, 2, 1],
    'gluc': [1, 1, 2],
    'smoke': [0, 1, 0],
    'alco': [0, 0, 0],
    'active': [1, 1, 0],
    'cardio': [0, 1, 0]
}

df = pd.DataFrame(data)

# Calculate BMI
df['height_m'] = df['height'] / 100  # Convert height from cm to m
df['BMI'] = df['weight'] / (df['height_m'] ** 2)

# Add overweight column
df['overweight'] = (df['BMI'] > 25).astype(int)

# Drop the temporary BMI column if not needed
df.drop(columns=['height_m', 'BMI'], inplace=True)

# Display the updated DataFrame
print(df)
print(df.info())
