import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr 

url = "https://raw.githubusercontent.com/rociochavezmx/Rocio-Chavez-youtube-Files/master/Contaminacion%20Atmosferica.csv"
df= pd.read_csv(url)

#print(df)

variable1 = df['Fabricas']
variable2 = df['Habitantes']
variable3 = df["Temperatura"]
correlation_matrix = np.corrcoef(variable1,[ variable2,variable3])
print(correlation_matrix)

print(df.columns)
plt.matshow(df.corr())
plt.colorbar()
plt.show()

slope, intercept = np.polyfit(df['Contaminacion_SO2'], df['Fabricas'], 1)
plt.scatter(df['Contaminacion_SO2'], df['Fabricas'])
plt.plot(df['Contaminacion_SO2'], slope*df['Contaminacion_SO2']+ intercept, color='red')

corr, p_value = pearsonr(df['Contaminacion_SO2'], df['Fabricas'])
print("Correlation: ", corr)
print("P-value: ", p_value)
#pearson entrega la correlacion y el p-valor. es decir la significancia estadistica de la correlacion.
