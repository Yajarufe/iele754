import pandas as pd #imorta panda como pd
import seaborn as sns

df = pd.read_csv("C:\\Users\\yaale\\OneDrive\\Escritorio\\Analisis de datos\\iele754\\Jarufe\\covid-19.csv")

print(df.head(5))

vals = list(df.columns)[5:-1] #permite generar una lista desde las columnas 5 en adelante

ids = list(df.columns)[:5]
df_cases_tidy = pd.melt(df, value_vars=vals, id_vars=ids)
print(df_cases_tidy)

df_cases_tidy=df_cases_tidy.dropna() #elimina los dna de todas las columnas
print(df_cases_tidy)
list(df_cases_tidy.dtypes)
df_cases_tidy["variable"] = pd.to_datetime(df_cases_tidy["variable"], format= "%Y-%m-%d") #esta linea permite transformar ña columna variables de valores a un datetime
print(df_cases_tidy.variable.dtype)
df_cases_tidy.dtypes

df_cases_tidy_month=df_cases_tidy[(df_cases_tidy["variable"] >= "2020-03-01") & (df_cases_tidy["variable"] <= "2020-06-30")]
#esta linea te permite filtrar los datos desde las fechas que amrcaste en comillas
print(df_cases_tidy_month)

df_cases_tidy_month.sort_values(by="variable").tail #sortvalue te permite ordenar las fechas de los datos
