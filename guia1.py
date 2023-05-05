#Guia 1) Analisis de temperatura.

import pandas as pd #imorta panda como pd
import seaborn as sns
print(pd.__version__) #te permite ver la version de panda

df = pd.read_csv("\\Users\\yaale\\OneDrive\\Escritorio\\Analisis de datos\\iele754\\Jarufe\\2023_temperatura_aire_ceaza.csv") #para leer el archivo, hay que copiar la ruta.

print(df.head()) #print me permite ver las primeras 5 datos de la tabla.

df["time"] = pd.to_datetime(df.time, format= "%Y-%m-%d %H:%M:%S") #Te cambia la base date a un valor llamado tiempo, que viene con formato año, mes, dia

df1 = df.loc[(df["time"].dt.month==3)] #nueva variable que marca el mes tres de la mdata base
print(df1)



df2 = pd.read_csv("C:\\Users\\yaale\\OneDrive\\Escritorio\\Analisis de datos\\iele754\\Jarufe\\2020_temperatura_aire_ceaza.csv")
df2["time"] = pd.to_datetime(df2.time, format= "%Y-%m-%d %H:%M:%S")
df3 = df2.loc[(df2["time"].dt.month==3)]

print(df3)

sns.kdeplot(df1.prom)
sns.kdeplot(df3.prom)