#Guia 2) Clean data covid and plot cases.

import pandas as pd #imorta panda como pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("C:\\Users\\yaale\\OneDrive\\Escritorio\\Analisis de datos\\iele754\\Jarufe\\covid-19.csv")

print(df.head(5))

vals = list(df.columns)[5:-1] #permite generar una lista desde las columnas 5 en adelante

ids = list(df.columns)[:5]
df_cases_tidy = pd.melt(df, value_vars=vals, id_vars=ids)
print(df_cases_tidy)

df_cases_tidy=df_cases_tidy.dropna() #elimina los dna de todas las columnas
print(df_cases_tidy)

list(df_cases_tidy.dtypes)
df_cases_tidy["variable"] = pd.to_datetime(df_cases_tidy["variable"])
df_cases_tidy["variable"] = pd.to_datetime(df_cases_tidy["variable"], format= "%Y-%m-%d") #esta linea permite transformar ña columna variables de valores a un datetime
print(df_cases_tidy.variable.dtype)
df_cases_tidy.dtypes

df_cases_tidy_month=df_cases_tidy[(df_cases_tidy["variable"] >= "2020-03-01") & (df_cases_tidy["variable"] <= "2020-06-30")]
#esta linea te permite filtrar los datos desde las fechas que amrcaste en comillas
print(df_cases_tidy_month)

df_cases_tidy_month.sort_values(by="variable").tail #sortvalue te permite ordenar las fechas de los datos

df_cases_tidy_month_Lascondes = df_cases_tidy_month[df_cases_tidy_month["Comuna"]== "Las Condes"].sort_values(by="variable")
df_cases_tidy_month_Lascondes
df_cases_tidy_month_Lobarnechea = df_cases_tidy_month[df_cases_tidy_month["Comuna"]== "Lo Barnechea"].sort_values(by="variable")
df_cases_tidy_month_Lobarnechea

df3= df_cases_tidy_month_Lascondes.groupby(pd.Grouper(key = "variable", freq= "W")).mean()

sns.lineplot(data=df_cases_tidy_month_Lascondes, x ="variable", y = "value")
sns.lineplot(data= df3, x = "variable" , y= "value")


plt.hist(df_cases_tidy, bins = 100, densi1ty = True)
