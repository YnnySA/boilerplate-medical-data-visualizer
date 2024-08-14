# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:10:20 2024

@author: Yenny SA
"""
import pandas as pd

df = pd.DataFrame({
       'A': [1, 2, 3],
       'B': [4, 5, 6]
   })


# Eliminar la columna 'B' directamente en df
df.drop('B', axis=1, inplace=True)

print(df)
   