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
    #Crear un DataFrame para cat con la función melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    #Convertir la columna "value" en str
    df_cat["value"] = df_cat["value"].astype(str)
    
    # 6
    #Agrupar y reformatear la Data
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    df_cat = df_cat.rename(columns={'total': 'total'})
       
    # 7
    # Crear un gráfico categórico usando seaborn
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar', height=5, aspect=1)

    # 8
    # Obtener la figura de salida y almacenarla en una variable fig
    fig = fig.fig

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    # Limpiar los datos de la variable df_heat
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    # Calcular la matrix de correlación
    corr = df_heat.corr()
    
    # 13
    # Generar una máscara para el triángulo ascendente y almacenar en la variable mask
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 14
    # Cagar la figura de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    # Graficar la matrix de correlación
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', linewidths=0.5)

            
       # Títulos
    plt.title('Heat Map of Correlation Matrix')
    plt.show()

    # 16
    fig.savefig('heatmap.png')
    return fig
  
