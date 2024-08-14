# -*- coding: utf-8 -*-
import pandas as pd

# Sample DataFrame (replace this with your actual DataFrame)
data = {
    'id': [1, 2, 3],
    'age': [45, 50, 39],
    'sex': [1, 2, 1],
    'height': [170, 180, 175],
    'weight': [70, 80, 65],
    'ap_hi': [120, 130, 140],
    'ap_lo': [80, 85, 90],
    'cholesterol': [1, 2, 1],
    'gluc': [1, 2, 1],
    'smoke': [0, 1, 0],
    'alco': [0, 0, 1],
    'active': [1, 1, 0],
    'cardio': [1, 0, 1]
}

df = pd.DataFrame(data)

# Normalize cholesterol and gluc
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Display the modified DataFrame
print(df)
