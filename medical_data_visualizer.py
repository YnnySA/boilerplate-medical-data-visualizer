# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
# Convertir la altura de metros a centímetros
df["height_meters"] = df["height"] / 100
# Calcular el BMI según lo indicado 
df["BMI"] = df["weight"] / (df["height_meters"]**2)
# Determinar el sobrepeso y añadirla como columna al df
df['overweight'] = (df["BMI"] > 25).astype(int)
# Quitar las columnas temporales de heigt_meters y BMI
df.drop(columns = ["height_meters", "BMI"], inplace=True)

# 3
#Normalizar el colesterol ("choresterol")
df["cholesterol"] = (
    df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
)
# Normalizar la gluco ("gluc")
df["gluc"] = (
    df["gluc"].apply(lambda x: 0 if x==1 else 1)
)

# 4
def draw_cat_plot():
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
