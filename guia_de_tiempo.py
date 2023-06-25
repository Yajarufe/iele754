#modelo arima
#Eercicio1
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA



url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto20/NumeroVentiladores_T.csv"
df = pd.read_csv(url)
print(df)

#ejercicio2
df.head()

#ejercicio3
df.isnull().values.any()
df_limpio = df.dropna()
#ejercicio 4

df_limpio.loc[:, 'Ventiladores'] = pd.to_datetime(df_limpio['Ventiladores'], format="%Y-%m-%d")
tipo_datos = df_limpio.dtypes
print(tipo_datos)

#ejercicio5

valor_medio = df_limpio['disponibles'].mean()
print(valor_medio)

#ejercicio 6

plt.hist(df_limpio['disponibles'])
plt.xlabel("Valores")
plt.ylabel("frecuencia")
plt.title("histograma de ventiladores dsiponibles")
plt.show()

#ejercicio 7

correlacion = df_limpio['total'].corr(df_limpio['disponibles'])
print(correlacion)

#ejercicio 8
 
df_limpio.plot(x='Ventiladores', y='total')
plt.show()

#ejercicio 9

descomposicion = seasonal_decompose(df_limpio['total'],
                                    model='additive', period=1)
descomposicion.plot()

plt.show()

#ejercicio 10

print(df_limpio.columns)

df_limpio.reset_index(inplace=True, drop=True)

modelo = ARIMA(df_limpio['Ventiladores'], order=(5,1,0))
modelo_ajustado = modelo.fit()
print(modelo_ajustado)